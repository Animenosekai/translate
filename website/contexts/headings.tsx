import React, { createContext, useContext, useState } from "react";

export const HeadingsContext = createContext<{
    headings: string[]
    setHeadings: React.Dispatch<React.SetStateAction<string[]>>
}>({ headings: [], setHeadings: (a) => { } });

export const useHeadings = () => useContext(HeadingsContext);

export const HeadingsContextConsumer = HeadingsContext.Consumer;

export interface HeadingsContextProps {
    children
}

export const HeadingsContextProvider = ({ children }: HeadingsContextProps) => {
    const [headings, setHeadings] = useState<string[]>([]);


    // SETTING THE VALUES
    return <HeadingsContext.Provider value={{
        headings,
        setHeadings
    }}>
        {children}
    </HeadingsContext.Provider>
}