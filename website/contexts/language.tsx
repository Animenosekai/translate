import React, { createContext, useContext, useState } from "react";

import EnglishLocalization from "../localizations/eng";

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
            default:
                setLanguageData(new EnglishLocalization());
        }
    }

    // SETTING THE VALUES
    return <LanguageContext.Provider value={{
        strings,
        setLanguage
    }}>
        {children}
    </LanguageContext.Provider>
}