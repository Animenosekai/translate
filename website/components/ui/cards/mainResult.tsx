import { Card, Loading, Tooltip } from "@nextui-org/react";
import { TransliterateRequest, TransliterateResult } from "types/transliterate";
import { useEffect, useState } from "react";

import ContentLoader from "react-content-loader";
import { EditIcon } from "components/icons/edit";
import { LanguageDetailsResult } from "types/languageDetails";
import { LanguagePicker } from "../modals/languagePicker";
import { Service } from "lib/services";
import { ServiceElement } from "components/common/service";
import { SourceTextArea } from "../textareas/source";
import { TTSIcon } from "components/icons/tts";
import { TTSRequest } from "types/tts";
import { TranslateRequest } from "types/translate";
import { request } from "lib/request";
import { useLanguage } from "contexts/language";

const THROTTLE = 1000;

export const TTSButton = ({ text, sourceLang, ...props }: { text: string, sourceLang: LanguageDetailsResult }) => {
    const [tts, setTTS] = useState(false);
    const [audio, setAudio] = useState<HTMLAudioElement>(null);

    useEffect(() => {
        if (!audio) { return }
        audio.play();
    }, [audio])

    useEffect(() => {
        if (tts) {
            request<TTSRequest>("/tts", {
                params: {
                    text: text,
                    lang: sourceLang.id
                }
            })
                .then(response => {
                    if (!response.success) { return }
                    const buffer = Buffer.from(response.data.base64, 'base64')
                    const blob = new Blob([buffer])
                    setAudio(new Audio(URL.createObjectURL(blob)))
                })
            setTTS(false);
        }
    }, [tts]);
    return <div className="ml-auto" {...props}>
        <button className="opacity-80 hover:opacity-100 transition active:scale-95" onClick={() => setTTS(true)}>
            <TTSIcon />
        </button>
    </div>
}

export const MainResultLoader = (props) => {
    return <div className="w-1/3 mb-2 p-1 mx-1 min-w-[300px]">
        <Card clickable shadow={false}>
            <ContentLoader
                speed={2}
                height={70}
                viewBox="0 0 320 70"
                backgroundColor="#f3f3f3"
                foregroundColor="#ecebeb"
                {...props}
            >
                <rect x="0" y="0" rx="3" ry="3" width={180 + (Math.random() * 100)} height="20" />
                <rect x="0" y="50" rx="3" ry="3" width={80 + (Math.random() * 50)} height="20" />
            </ContentLoader>
        </Card>
    </div>
}
export const MainResultCard = ({ text, language, service, loading, onNewTranslation, ...props }: { text: string, language: LanguageDetailsResult, service?: Service, loading?: boolean, onNewTranslation?: (text: string, language: LanguageDetailsResult) => any }) => {
    const { strings } = useLanguage();
    const [currentText, setCurrentText] = useState<string>(text);
    const [currentLanguage, setCurrentLanguage] = useState<LanguageDetailsResult>(language);
    const [showModal, setShowModal] = useState<boolean>(false);
    const [currentTimeout, setCurrentTimeout] = useState(null);
    const [transliteration, setTransliteration] = useState<TransliterateResult>(null);

    console.log("MainResultCard", { text, language, service, loading, onNewTranslation, props })

    useEffect(() => {
        if (!service) { return }
        request<TransliterateRequest>("/transliterate", {
            params: {
                text: currentText,
                dest: language.id
            }
        })
            .then(value => {
                if (value.success && value.data.result != currentText) {
                    setTransliteration(value.data);
                } else {
                    setTransliteration(null);
                }
            })
            .catch(_ => {
                setTransliteration(null);
            })
    }, [currentText])

    useEffect(() => {
        if (currentLanguage.id != language.id) {
            return onNewTranslation && onNewTranslation(currentText, currentLanguage);
        }
    }, [currentLanguage])


    useEffect(() => {
        if (!onNewTranslation || currentText == text) { return }
        clearTimeout(currentTimeout);
        setCurrentTimeout(setTimeout(() => {
            return onNewTranslation(currentText, currentLanguage);
        }, THROTTLE))
    }, [currentText]);

    useEffect(() => {
        setCurrentText(text);
    }, [text])

    useEffect(() => {
        setCurrentLanguage(language);
    }, [language])

    return <Card color={service ? "primary" : "default"}>
        <h3>
            <div className="text-black">
                {
                    showModal && <LanguagePicker
                        setLanguage={setCurrentLanguage}
                        setShowModal={setShowModal}
                        text={currentLanguage?.inForeignLanguages[strings.alpha2] ? currentLanguage.inForeignLanguages[strings.alpha2] : currentLanguage.name} />
                }
            </div>
            <div className="flex flex-row group w-max cursor-pointer" onClick={el => { setShowModal(true); }}>
                <span className="font-medium text-sm">
                    {/* {currentLanguage?.inForeignLanguages[currentLanguage.alpha2] ? currentLanguage.inForeignLanguages[currentLanguage.alpha2] : currentLanguage.name} */}
                    {currentLanguage?.inForeignLanguages[strings.alpha2] ? currentLanguage.inForeignLanguages[strings.alpha2] : currentLanguage.name}
                </span>
                <EditIcon className="scale-[.7] -mt-[.2rem] transition opacity-50 group-hover:opacity-80" />
            </div>
        </h3>
        {
            service
                ? <div className="flex flex-row space-x-1">
                    <p className="mt-3 mb-5">{currentText}</p>
                    {
                        loading
                            ? <Loading type="points-opacity" color={"white"} size="sm" />
                            // ? <Loading type="points-opacity" color={"white"} size="xs" />
                            : ""
                    }
                </div>
                : <SourceTextArea value={currentText} onChange={el => setCurrentText(el.target.value)} />
        }
        <Card.Footer>
            <div className="w-11/12 flex flex-row">
                <ServiceElement service={service} />
                {
                    transliteration && <div className="opacity-70 flex flex-row">
                        {"・"}
                        <div className="h-5">
                            <Tooltip content={strings.labels.transliterationBy.format({ service: transliteration.service })} rounded hideArrow placement="right" style={{
                                color: "white",
                                width: "100%"
                            }} contentColor="primary">
                                <span className="italic w-full">{transliteration.result}</span>
                            </Tooltip>
                        </div>
                    </div>
                }
            </div>
            <TTSButton text={currentText} sourceLang={language} />
        </Card.Footer>
    </Card>
}

export const MainResult = ({ result, onNewTranslation, ...props }: {
    result: TranslateRequest, onNewTranslation?: (translation: {
        text: string,
        dest: string,
        source: string
    }) => any
}) => {

    const [loading, setLoading] = useState(result.loading);
    useEffect(() => {
        setLoading(result.loading);
    }, [result])

    const service = new Service(result.data.service)
    console.log("result", result)
    return <div className="flex lg:flex-row flex-col lg:space-x-10 lg:space-y-0 space-y-5 mb-10">
        <MainResultCard text={result.data.source} language={result.data.sourceLanguage} onNewTranslation={(text, lang) => {
            if (!onNewTranslation) {
                return console.log("source", text, lang)
            }
            setLoading(true);
            return onNewTranslation({
                text,
                source: lang.id,
                dest: result.data.destinationLanguage.id,
            })
        }} />
        <MainResultCard loading={loading} text={result.data.result} language={result.data.destinationLanguage} service={service} onNewTranslation={(text, lang) => {
            if (!onNewTranslation) {
                return console.log("dest", text, lang)
            }
            setLoading(true);
            return onNewTranslation({
                text: result.data.source,
                source: result.data.sourceLanguage.id,
                dest: lang.id,
            })
        }} />
    </div>
}