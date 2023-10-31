import { Card, CardBody, CardFooter, CardHeader } from "@nextui-org/card";
import { Language, getLanguageName } from "types/language";
import { RichSpellcheckResult, SpellcheckResult } from "types/spellcheck";
import { useEffect, useState } from "react";

import { ClientTranslationResult } from "types/translate";
import ContentLoader from "react-content-loader";
import { CopyIcon } from "components/icons/copy";
// import { CopyNotification } from "../notifications/copy";
import { EditIcon } from "components/icons/edit";
import { LanguagePicker } from "../modals/languagePicker";
import { Loading } from "components/common/loading";
import { Request } from "types/request";
import { Service } from "lib/services";
import { ServiceElement } from "components/common/service";
import { SourceTextArea } from "../textareas/source";
// import { Spinner } from "@nextui-org/spinner"
import { TextToSpeechButton } from "../buttons/tts";
// import {Spinner} from "@nextui-org/l";
import { Tooltip } from "@nextui-org/tooltip"
import { TransliterationResult } from "types/transliterate";
import classNames from "classnames";
import { request } from "lib/request";
import { useLanguage } from "contexts/language";

const THROTTLE = 1000;

export const MainResultLoader = (props) => {
    return <div className="w-1/3 mb-2 p-1 mx-1 min-w-[300px]">
        <Card isPressable>
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
export const MainResultCard = ({ text, language, service, loading, onNewTranslation, onCopyNotification, spellchecked, ...props }: {
    text: string,
    language: Language,
    service?: Service,
    loading?: boolean,
    onNewTranslation?: (text: string, language: Language) => any,
    onCopyNotification?: () => any,
    spellchecked?: SpellcheckResult
}) => {
    const { strings } = useLanguage();
    const [currentText, setCurrentText] = useState<string>(text);
    const [currentLanguage, setCurrentLanguage] = useState<Language>(language);
    const [showModal, setShowModal] = useState<boolean>(false);
    const [currentTimeout, setCurrentTimeout] = useState<any>(undefined);
    const [transliteration, setTransliteration] = useState<TransliterationResult | undefined>(undefined);

    useEffect(() => {
        if (service && language) { // transliterate
            request<Request<TransliterationResult>>("/transliterate", {
                params: {
                    text: currentText,
                    dest_lang: language.id
                }
            })
                .then(value => {
                    if (value.success && value.data.transliteration != currentText) {
                        setTransliteration(value.data);
                    } else {
                        setTransliteration(undefined);
                    }
                })
                .catch(_ => {
                    setTransliteration(undefined);
                })
        }

    }, [currentText])

    useEffect(() => {
        if (currentLanguage && language && currentLanguage.id != language.id) {
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

    return <Card className={classNames({
        "bg-primary text-white": service,
        "bg-white text-black": !service
    }, "w-auto flex-grow px-2 py-1")}>
        <CardHeader className="pb-0">
            <div className="text-black">
                {
                    showModal && <LanguagePicker
                        automatic={!service}
                        setLanguage={setCurrentLanguage}
                        setShowModal={setShowModal}
                        text={getLanguageName(currentLanguage, strings)} />
                }
            </div>
            <div className="flex flex-row group w-max cursor-pointer" onClick={el => { setShowModal(true); }}>
                <span className="font-medium text-sm">
                    {/* {currentLanguage?.inForeignLanguages[currentLanguage.alpha2] ? currentLanguage.inForeignLanguages[currentLanguage.alpha2] : currentLanguage.name} */}
                    {getLanguageName(currentLanguage, strings)}
                </span>
                <EditIcon className="scale-[.7] -mt-[.2rem] transition opacity-50 group-hover:opacity-80" />
            </div>
        </CardHeader>
        <CardBody className="px-3 py-0">
            {
                service
                    ? <div className="flex flex-row space-x-1">
                        <p className="mt-3 mb-5">{currentText}</p>
                        {
                            loading
                                ? <Loading />
                                // ? <Spinner type="points-opacity" color={"white"} size="sm" />
                                // ? <Spinner type="points-opacity" color={"white"} size="xs" />
                                : ""
                        }
                    </div>
                    : <SourceTextArea value={currentText} onChange={el => setCurrentText(el.target.value)} />
            }
        </CardBody>
        <CardFooter>
            <div className="w-10/12 flex flex-row">
                <ServiceElement service={service} />
                {
                    spellchecked && <div className="opacity-70 flex flex-row">
                        {"・"}
                        <div className="h-5">
                            <Tooltip content={strings.labels.spellcheckBy.format({ service: spellchecked.service })} placement="right" style={{
                                color: "white",
                                width: "100%"
                            }} color="primary">
                                <span onClick={() => {
                                    setCurrentText(spellchecked.corrected);
                                }} className="italic w-full text-black">{spellchecked.corrected}</span>
                            </Tooltip>
                        </div>
                    </div>
                }
                {
                    transliteration && <div className="opacity-70 flex flex-row">
                        {"・"}
                        <div className="h-5">
                            <Tooltip content={strings.labels.transliterationBy.format({ service: transliteration.service })} placement="right" style={{
                                color: "white",
                                width: "100%"
                            }} color="primary">
                                <span className="italic w-full">{transliteration.transliteration}</span>
                            </Tooltip>
                        </div>
                    </div>
                }
            </div>
            <div className="ml-auto flex flex-row space-x-2">
                <TextToSpeechButton text={currentText} source_lang={language} />
                {
                    service
                        ? <CopyIcon onClick={() => {
                            navigator.clipboard.writeText(currentText);
                            if (onCopyNotification) {
                                onCopyNotification();
                            }
                        }} className="opacity-70 hover:opacity-100 transition active:scale-95 cursor-pointer" />
                        : ""
                }
            </div>
        </CardFooter>
    </Card>
}

export const MainResult = ({ result, onNewTranslation, onCopyNotification, loading, setLoading, ...props }: {
    result: ClientTranslationResult,
    onNewTranslation?: (translation: {
        text: string,
        dest_lang: string,
        source_lang: string
    }) => any,
    onCopyNotification?: () => any,
    loading: boolean,
    setLoading: (boolean) => any
}) => {
    const [spellchecked, setSpellchecked] = useState<SpellcheckResult | RichSpellcheckResult | undefined>(undefined);
    const service = new Service(result.service)
    return <div className="flex lg:flex-row flex-col lg:space-x-10 lg:space-y-0 space-y-5 mb-10 justify-evenly content-stretch flex-wrap">
        <MainResultCard
            spellchecked={spellchecked}
            onCopyNotification={onCopyNotification}
            text={result.source}
            language={result.source_lang}
            onNewTranslation={(text, lang) => {
                if (!onNewTranslation) {
                    // return console.log("source_lang", text, lang)
                    return
                }
                setLoading(true);
                request<Request<SpellcheckResult>>("/spellcheck", {
                    params: {
                        text: text,
                        source_lang: lang.id
                    }
                })
                    .then(value => {
                        if (value.success && value.data.corrected != text) {
                            setSpellchecked(value.data);
                        } else {
                            setSpellchecked(undefined);
                        }
                    })
                    .catch(_ => {
                        setSpellchecked(undefined);
                    })
                return onNewTranslation({
                    text,
                    source_lang: lang.id,
                    dest_lang: result.dest_lang.id,
                })
            }} />
        <MainResultCard
            onCopyNotification={onCopyNotification}
            loading={loading}
            text={result.translation}
            language={result.dest_lang}
            service={service}
            onNewTranslation={(text, lang) => {
                if (!onNewTranslation) {
                    // return console.log("dest_lang", text, lang)
                    return
                }
                setLoading(true);
                return onNewTranslation({
                    text: result.source,
                    source_lang: result.source_lang.id,
                    dest_lang: lang.id,
                })
            }} />
    </div>
}