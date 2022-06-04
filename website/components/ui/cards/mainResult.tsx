import { Card, Tooltip } from "@nextui-org/react";
import { useEffect, useState } from "react";

import { EditIcon } from "components/icons/edit";
import { LanguageDetailsResult } from "types/languageDetails";
import { LanguagePicker } from "../modals/languagePicker";
import Link from "next/link";
import { Service } from "lib/services";
import { ServiceElement } from "components/common/service";
import { SourceTextArea } from "../textareas/source";
import { TTSIcon } from "components/icons/tts";
import { TranslateRequest } from "types/translate";
import { TransliterateResult } from "types/transliterate";

const THROTTLE = 1000;

export const TTSButton = ({ text, sourceLang, ...props }) => {
    const [tts, setTTS] = useState(false);
    useEffect(() => {
        if (tts) {
            console.log("Should play audio")
            setTTS(false);
        }
    }, [tts]);
    return <div className="ml-auto" {...props}>
        <button className="opacity-80 hover:opacity-100 transition active:scale-95" onClick={() => setTTS(true)}>
            <TTSIcon />
        </button>
    </div>
}

export const MainResultCard = ({ text, language, service, onNewTranslation, ...props }: { text: string, language: string, service?: Service, onNewTranslation?: (text: string, language: string) => any }) => {
    const [currentText, setCurrentText] = useState<string>(text);
    const [currentLanguage, setCurrentLanguage] = useState<string>(language);
    const [langDetails, setLangDetails] = useState<LanguageDetailsResult>(null)
    const [showModal, setShowModal] = useState<boolean>(false);
    const [currentTimeout, setCurrentTimeout] = useState(null);
    const [transliteration, setTransliteration] = useState<TransliterateResult>(
        service
            ? {
                service: "Google",
                source: "Hello World",
                sourceLang: "eng",
                destLang: "jpa",
                result: "Kon'nichiwa Sekai"
            }
            : null
    );

    const retrieveLanguageDetails = () => {
        setLangDetails(
            service
                ? {
                    id: "jpa",
                    alpha2: "ja",
                    alpha3b: "jpa",
                    alpha3t: "jpa",
                    alpha3: "jpa",
                    name: "Japanese",
                    foreign: { ja: "日本語" },
                    extra: null
                }
                : {
                    id: "eng",
                    alpha2: "en",
                    alpha3b: "eng",
                    alpha3t: "eng",
                    alpha3: "eng",
                    name: "English",
                    foreign: { en: "English" },
                    extra: null
                })
    }

    useEffect(() => {
        if (currentLanguage != language) {
            return onNewTranslation && onNewTranslation(currentText, currentLanguage);
        }
        return retrieveLanguageDetails();
    }, [currentLanguage])


    useEffect(() => {
        if (!onNewTranslation || currentText == text) { return }
        clearTimeout(currentTimeout);
        setCurrentTimeout(setTimeout(() => {
            return onNewTranslation(currentText, currentLanguage);
        }, THROTTLE))
    }, [currentText]);

    return <Card color={service ? "primary" : "default"}>
        <h3>
            <div className="text-black">
                {
                    showModal && <LanguagePicker
                        setLanguage={setCurrentLanguage}
                        setDetails={setLangDetails}
                        setShowModal={setShowModal}
                        text={
                            langDetails
                                ? (langDetails.foreign[langDetails.alpha2] ? langDetails.foreign[langDetails.alpha2] : langDetails.name)
                                : currentLanguage
                        } />
                }
            </div>
            <div className="flex flex-row group w-max cursor-pointer" onClick={el => { setShowModal(true); }}>
                <span className="font-medium text-sm">
                    {
                        langDetails
                            ? (langDetails.foreign[langDetails.alpha2] ? langDetails.foreign[langDetails.alpha2] : langDetails.name)
                            : currentLanguage
                    }
                </span>
                <EditIcon className="scale-[.7] -mt-[.2rem] transition opacity-50 group-hover:opacity-80" />
            </div>
        </h3>
        {
            service
                ? <p className="mt-3 mb-5">{currentText}</p>
                : <SourceTextArea value={currentText} onChange={el => setCurrentText(el.target.value)} />
        }
        <Card.Footer>
            <ServiceElement service={service} />
            {
                transliteration && <div className="opacity-70 flex flex-row">
                    {"・"}
                    <div className="h-5">
                        <Tooltip content={`Transliteration by ${transliteration.service}`} rounded hideArrow placement="right" style={{
                            color: "white"
                        }} contentColor="primary">
                            <span className="italic w-full">{transliteration.result}</span>
                        </Tooltip>
                    </div>
                </div>
            }
            <TTSButton text={currentText} sourceLang={language} />
        </Card.Footer>
    </Card>
}

export const MainResult = ({ result, ...props }: { result: TranslateRequest }) => {
    const service = new Service(result.data.service)
    return <div className="flex lg:flex-row flex-col lg:space-x-10 lg:space-y-0 space-y-5 mb-10">
        <MainResultCard text={result.data.source} language={result.data.sourceLang} onNewTranslation={(text, lang) => { console.log("text:" + text + "|lang:" + lang) }} />
        <MainResultCard text={result.data.result} language={result.data.destLang} service={service} onNewTranslation={(text, lang) => { console.log("text:" + text + "|lang:" + lang) }} />
    </div>
}