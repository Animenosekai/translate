import { ClientTranslationResult, DEFAULT_TRANSLATION_REQUEST, DEFAULT_TRANSLATION_RESULT } from 'types/translate'
import { SubResult, SubResultLoader } from 'components/ui/cards/subResult'
import { useEffect, useState } from 'react'

import Configuration from 'config'
import { CopyNotification } from 'components/ui/notifications/copy'
import { MainResult } from 'components/ui/cards/mainResult'
import type { NextPage } from 'next'
import { SEO } from 'components/common/seo'
import { generateRandomID } from 'utils/random'
import { prepare } from 'lib/request'
import { services } from 'lib/services'
import { useLanguage } from 'contexts/language'
import { useRouter } from 'next/router'

const Translate: NextPage = () => {
    const { strings } = useLanguage();
    const router = useRouter();
    const [loading, setLoading] = useState<boolean>(true);
    const [toLoad, setToLoad] = useState(Object.keys(services).length);
    const [results, setResults] = useState<ClientTranslationResult[]>([DEFAULT_TRANSLATION_RESULT]);

    let URLParams: URLSearchParams
    if (typeof window !== "undefined") {
        URLParams = new URLSearchParams(location.search);
    } else {
        URLParams = new URLSearchParams();
    }
    const [currentTranslation, setCurrentTranslation] = useState<{
        text: string,
        source_lang: string,
        dest_lang: string
    }>({
        text: URLParams.get("text") ?? "",
        source_lang: URLParams.get("source_lang") || "auto",
        dest_lang: URLParams.get("dest_lang") || "eng"
    })
    const [streamID, setStreamID] = useState<string | undefined>(undefined);

    useEffect(() => {
        const currentID = streamID;
        setTimeout(() => {
            if (!currentID || currentID != streamID) { return }

            // console.log("Connecting to stream...", currentID, streamID);
            // console.log(`Translate: ${currentTranslation.text} from ${currentTranslation.source_lang} to ${currentTranslation.dest_lang}`);

            const { finalPath } = prepare("/stream", {
                params: {
                    text: currentTranslation.text,
                    dest_lang: currentTranslation.dest_lang,
                    source_lang: currentTranslation.source_lang
                }
            })
            const stream = new EventSource(Configuration.request.host + finalPath)

            setResults([{ ...DEFAULT_TRANSLATION_RESULT, source: currentTranslation.text }])
            setLoading(true);
            setToLoad(Object.keys(services).length);

            stream.addEventListener("translation", (event) => {
                const data = JSON.parse(event.data);

                setResults(results => {
                    setLoading(false);
                    return [...results.filter(el => !el.default), data]
                })
                setToLoad(toLoad => toLoad - 1)
            })

            stream.addEventListener("counter", (event) => {
                const data = JSON.parse(event.data);
                setToLoad(data)
            })

            stream.onerror = (event) => {
                if (event.eventPhase === EventSource.CLOSED) {
                    stream.close();
                }
                setToLoad(0);
            }

        }, 200)
    }, [streamID]);

    useEffect(() => {
        if (!currentTranslation.text) { return }
        router.push(`/translate?text=${encodeURIComponent(currentTranslation.text)}&source_lang=${encodeURIComponent(currentTranslation.source_lang)}&dest_lang=${encodeURIComponent(currentTranslation.dest_lang)}`, undefined, { shallow: true })
        const currentID = generateRandomID(12);
        setStreamID(currentID);
    }, [currentTranslation])


    const [showCopyNotification, setShowCopyNotification] = useState(false);
    const [notificationTimeout, setNotificationTimeout] = useState<any>(undefined);

    const copyNotificationDuration = 3000

    useEffect(() => {
        if (showCopyNotification) {
            clearTimeout(notificationTimeout);
            setNotificationTimeout(setTimeout(() => {
                setShowCopyNotification(false);
            }, copyNotificationDuration))
        }
    }, [showCopyNotification])

    const showCopyNotificationHandler = () => {
        setShowCopyNotification(true);
    }

    return <div className='h-full'>
        <SEO title={`translation of "${currentTranslation.text}" from ${currentTranslation.source_lang} to ${currentTranslation.dest_lang}`} description='Use multiple services to translate your texts!' />
        {
            showCopyNotification && <CopyNotification duration={copyNotificationDuration} />
        }
        <div className="sm:p-16 p-5">
            {
                <MainResult
                    loading={loading}
                    setLoading={setLoading}
                    onCopyNotification={showCopyNotificationHandler}
                    onNewTranslation={setCurrentTranslation}
                    result={results ? results[0] : DEFAULT_TRANSLATION_RESULT} />
            }
            <div className="mx-3 mt-16">
                <h2 className="font-semibold text-xl mb-5">{strings.headings.otherTranslations}</h2>
                <div className='flex flex-row flex-wrap w-full justify-start content-around gap-5'>
                    {
                        results.slice(1).map((result, index) => {
                            return <SubResult
                                onCopyNotification={showCopyNotificationHandler}
                                key={index}
                                result={result}
                            />
                        })
                    }
                    {
                        toLoad > 0
                            ? Array(toLoad).fill(0).map((_, i) => <SubResultLoader key={i} />)
                            : ""
                    }
                </div>
            </div>
        </div>
    </div>
}

export default Translate
