import * as languages from "../localizations";

import React, { createContext, useContext, useEffect, useState } from "react";

import EnglishLocalization from "../localizations/eng";
import FrenchLocalization from "localizations/fra";
import JapaneseLocalization from "localizations/jpn";
import Localization from "localizations/base";
import SpanishLocalization from "localizations/spa";

export const LanguageContext = createContext<{
    strings: Localization
    setLanguage: (language: string) => void
}>({ strings: EnglishLocalization, setLanguage: (a) => { } });

export const useLanguage = () => useContext(LanguageContext);

export const LanguageContextConsumer = LanguageContext.Consumer;

export interface LanguageContextProps {
    children
}

export const LanguageContextProvider = ({ children }: LanguageContextProps) => {
    // HOOKS DEFINITION
    const [strings, setLanguageData] = useState<Localization>(EnglishLocalization);

    const setLanguage = (language: string) => {
        window.localStorage.setItem("ui-language", language);

        for (const lang in languages) {
            const newLang = languages[lang]
            if (language === newLang.language) {
                return setLanguageData(newLang);
            }
        }
        return setLanguageData(EnglishLocalization);
    }

    useEffect(() => {
        setLanguage(window.localStorage.getItem("ui-language") || "eng");
    }, [])

    // SETTING THE VALUES
    return <LanguageContext.Provider value={{
        strings,
        setLanguage
    }}>
        {children}
    </LanguageContext.Provider>
}