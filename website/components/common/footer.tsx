import * as localizations from "../../localizations";

import { useLanguage } from "contexts/language";

export const Footer = () => {
    const { strings, setLanguage } = useLanguage();
    return <footer className="fixed bottom-0 flex justify-between w-full m-auto py-5 px-10">
        <div className="space-x-8">
            <a className="opacity-40 text-black hover:opacity-70 transition" target="_blank" rel="noreferrer" href="https://github.com/Animenosekai/translate">GitHub</a>
            <select value={strings.language} className="appearance-none bg-transparent outline-none cursor-pointer opacity-40 hover:opacity-70 transition" name="language" onChange={ev => setLanguage(ev.target.value)}>
                {
                    Object.keys(localizations).map((lang, key) => {
                        return <option value={lang} key={key}>{(new localizations[lang]()).name}</option>
                    })
                }
            </select>
        </div>
    </footer>
}
