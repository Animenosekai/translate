import React, { createContext, useContext, useState } from "react";

export const ServicesColorContext = createContext<{
    servicesColor: { [key: string]: string }
    addColor: (service: string, color: string) => void
}>(undefined);

export const useServicesColor = () => useContext(ServicesColorContext);

export const ServicesColorContextConsumer = ServicesColorContext.Consumer;

export interface ServicesColorContextProps {
    children
}

export const ServicesColorContextProvider = ({ children }: ServicesColorContextProps) => {

    const [servicesColor, setServicesColor] = useState<{ [key: string]: string }>({});

    const addColor = (service: string, color: string) => {
        setServicesColor({
            ...servicesColor,
            [service]: color
        })
    }

    // SETTING THE VALUES
    return <ServicesColorContext.Provider value={{
        servicesColor,
        addColor
    }}>
        {children}
    </ServicesColorContext.Provider>
}