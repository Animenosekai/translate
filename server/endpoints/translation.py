from datetime import datetime

from bson import ObjectId
from nasse.timer import Timer
from server.db import client
import translatepy
from translatepy.server.translation import (BaseTranslator, FlaskResponse,
                                            Language, List, NoResult, Queue,
                                            Response, Thread, Translator,
                                            UnknownLanguage, UnknownTranslator,
                                            json, t)

timings = client.translatepy.timings


def log_time(service: BaseTranslator, time: float, storage: dict):
    print("{service} took {time} seconds".format(service=service, time=time))
    storage[str(service)] = time


errors = client.translatepy.errors


def log_error(service: str, error: str):
    print("{service} failed: {error}".format(service=service, error=error))
    new_id = ObjectId()
    errors[new_id] = {
        "_id": new_id,
        "service": service,
        "error": error,
        "timestamp": datetime.utcnow()
    }


def stream_fix(text: str, dest: str, source: str = "auto", translators: List[str] = None, foreign: bool = True):
    current_translator = t
    if translators is not None:
        try:
            current_translator = Translator(translators)
        except UnknownTranslator as err:
            return Response(
                data={
                    "guessed": str(err.guessed_translator),
                    "similarity": err.similarity,
                },
                message="translatepy could not find the given translator",
                error="UNKNOWN_TRANSLATOR",
                code=400
            )

    try:
        dest = Language(dest)
        source = Language(source)
        # result = current_translator.translate(text=text, destination_language=dest, source_language=source)
    except UnknownLanguage as err:
        return Response(
            data={
                "guessed": str(err.guessed_language),
                "similarity": err.similarity,
            },
            message=str(err),
            error="UNKNOWN_LANGUAGE",
            code=400
        )

    def _translate(translator: BaseTranslator):
        result = translator.translate(
            text=text, destination_language=dest, source_language=source
        )
        if result is None:
            raise NoResult("{service} did not return any value".format(service=translator.__repr__()))
        return result

    def _fast_translate(queue: Queue, translator, index: int, timing_storage: dict):
        try:
            with Timer() as timer:
                translator = current_translator._instantiate_translator(translator, current_translator.services, index)
                result = _translate(translator)
            log_time(translator, timer.time, timing_storage)
            queue.put({
                "success": True,
                "error": None,
                "message": None,
                "data": result.as_dict(camelCase=True, foreign=foreign)
            })
        except Exception as err:
            service = str(translator) if isinstance(translator, BaseTranslator) else translator.__name__
            error = str(err.__class__.__name__)
            log_error(service, error)
            queue.put({
                "success": False,
                "error": error,
                "message": "; ".join(err.args),
                "data": {
                    "service": service,
                }
            })

    _queue = Queue()
    threads = []
    new_id = ObjectId()
    timings[new_id] = {
        "_id": new_id,
        "timings": {},
        "timestamp": datetime.utcnow(),
    }
    new_timing_storage = timings[new_id]["timings"]
    for index, service in enumerate(current_translator.services):
        thread = Thread(target=_fast_translate, args=(_queue, service, index, new_timing_storage))
        thread.start()
        threads.append(thread)

    def handler():
        while True:
            try:
                result = _queue.get(threads=threads)  # wait for a value and return it
            except ValueError:
                break
            if result is None:
                break

            yield "data: {result}\n\n".format(result=json.dumps(result, ensure_ascii=False))

    return FlaskResponse(handler(), mimetype="text/event-stream", headers={
        "X-TRANSLATEPY-ID": str(new_id), "X-TRANSLATEPY-VERSION": translatepy.__version__
    })
