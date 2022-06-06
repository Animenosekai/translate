import { AutomaticDetailsRequest, LanguageDetailsRequest, LanguageDetailsResult, LanguageSearchRequest, SearchResultContainer } from "types/languageDetails"
import { Dispatch, HTMLAttributes, SetStateAction, useEffect, useState } from "react"

import { request } from "lib/request"
import { useLanguage } from "contexts/language"

export interface LanguageElementProps extends HTMLAttributes<HTMLDivElement> {
    language: SearchResultContainer
}

export const LanguageElement = ({ language, ...props }: LanguageElementProps) => {
    return <div className="p-3 w-full h-12 bg-white bg-opacity-100 transition hover:bg-slate-50 cursor-pointer group" {...props}>
        <span className="font-medium text-gray-700 group-hover:text-gray-900">{`${language.string} (${language.language.id})`}</span>
    </div>
}


export const LanguagePicker = ({ text, setShowModal, setLanguage, automatic, ...props }: { text?: string, setShowModal: Dispatch<SetStateAction<boolean>>, setLanguage: Dispatch<SetStateAction<LanguageDetailsResult>>, automatic?: boolean }) => {
    const { strings } = useLanguage();
    const [query, setQuery] = useState(text)
    const [results, setResults] = useState<SearchResultContainer[]>([])
    const [autoResult, setAutoResult] = useState<SearchResultContainer>(AutomaticDetailsRequest);

    useEffect(() => {
        if (!query) { return }
        request<LanguageSearchRequest>("/language/search", {
            params: {
                lang: query,
                limit: 5
            }
        })
            .then(value => {
                if (value.success) { setResults(value.data.languages) }
            })
    }, [query])

    useEffect(() => {
        setAutoResult({
            ...AutomaticDetailsRequest,
            string: AutomaticDetailsRequest.language.inForeignLanguages[strings.alpha2] ? AutomaticDetailsRequest.language.inForeignLanguages[strings.alpha2] : AutomaticDetailsRequest.language.name
        })
    }, [automatic, strings])

    return <div className={"flex items-center justify-center w-screen h-screen top-0 left-0 fixed z-10 bg-white bg-opacity-80 animate-enter-modal"} onClick={() => { setShowModal(false); }}>
        <div className="flex flex-col rounded md:w-1/2 w-3/4 2xl:w-1/3" onClick={el => { el.stopPropagation() }}>
            <input autoFocus value={query} onKeyUp={(ev) => {
                if (ev.key == "Enter" || ev.keyCode === 13) {
                    setLanguage(results[0].language)
                    setShowModal(false)
                }
            }} onChange={ev => setQuery(ev.target.value)} placeholder="Type a language..." type="text" className="w-full h-10 p-3 outline-none rounded border-[1px] shadow-lg" />

            {
                automatic
                    ? <div className="w-full rounded h-full mt-3 overflow-hidden shadow-lg border-[1px]">
                        <LanguageElement language={autoResult} onClick={() => { setLanguage(autoResult.language); setShowModal(false); }} />
                    </div>
                    : ""
            }

            <div className="w-full rounded h-full mt-3 overflow-hidden shadow-lg border-[1px]">
                {
                    results.map((language, key) => {
                        return <LanguageElement key={key} language={language} onClick={() => { setLanguage(language.language); setShowModal(false); }} />
                    })
                }
            </div>
        </div>
    </div >
}