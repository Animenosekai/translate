import React, { createContext, useContext, useEffect, useState } from "react";

import EnglishLocalization from "../localizations/eng";
import FrenchLocalization from "localizations/fra";
import JapaneseLocalization from "localizations/jpn";

export const LanguageContext = createContext<{
    strings: EnglishLocalization
    setLanguage: (language: string) => void
}>(undefined);

export const useLanguage = () => useContext(LanguageContext);

export const LanguageContextConsumer = LanguageContext.Consumer;

export interface LanguageContextProps {
    children
}

export const LanguageContextProvider = ({ children }: LanguageContextProps) => {
    // HOOKS DEFINITION
    const [strings, setLanguageData] = useState<EnglishLocalization>(new EnglishLocalization());

    const setLanguage = (language: string) => {
        switch (language) {
            case "eng":
                setLanguageData(new EnglishLocalization());
                break;
            case "fra":
                setLanguageData(new FrenchLocalization());
                break;
            case "jpn":
                setLanguageData(new JapaneseLocalization());
                break;
            default:
                setLanguageData(new EnglishLocalization());
        }
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