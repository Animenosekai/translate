import { Dispatch, HTMLAttributes, SetStateAction, useState } from "react"
import { LanguageDetailsResult, SearchResultContainer } from "types/languageDetails"

export interface LanguageElementProps extends HTMLAttributes<HTMLDivElement> {
    language: SearchResultContainer
}

export const LanguageElement = ({ language, ...props }: LanguageElementProps) => {
    return <div className="p-3 w-full h-12 bg-white bg-opacity-50 transition hover:bg-slate-50 cursor-pointer group" {...props}>
        <span className="font-medium text-gray-700 group-hover:text-gray-900">{`${language.string} (${language.language.id})`}</span>
    </div>
}


export const LanguagePicker = ({ text, setShowModal, setLanguage, setDetails, ...props }: { text?: string, setShowModal: Dispatch<SetStateAction<boolean>>, setLanguage: Dispatch<SetStateAction<string>>, setDetails: Dispatch<SetStateAction<LanguageDetailsResult>> }) => {
    const [query, setQuery] = useState(text)
    const test = {
        string: "English",
        similarity: 90,
        language: {
            id: "eng",
            alpha2: "en",
            alpha3b: "eng",
            alpha3t: "eng",
            alpha3: "eng",
            name: "English",
            foreign: { en: "English" },
            extra: null
        }
    }

    return <div className={"flex items-center justify-center w-screen h-screen top-0 left-0 fixed z-10 bg-white bg-opacity-70 animate-enter-modal"} onClick={() => { setShowModal(false); }}>
        <div className="flex flex-col rounded md:w-1/2 w-3/4 2xl:w-1/3 shadow-lg" onClick={el => { el.stopPropagation() }}>
            <input autoFocus value={query} onChange={ev => setQuery(ev.target.value)} placeholder="Type a language..." type="text" className="w-full h-10 p-3 outline-none rounded border-[1px]" />
            <div className="w-full rounded h-full mt-3 overflow-hidden">
                <LanguageElement language={test} onClick={() => { setLanguage(test.language.id); setDetails(test.language); setShowModal(false); }} />
            </div>
        </div>
    </div>
}