import React, { createContext, useContext, useState } from "react";

import { Granularity } from "types/granularity";

export const ChartDataContext = createContext<{
    granularity: Granularity
    setGranularity: (granularity: Granularity) => any
    unit: string
    yLabel: string
}>(undefined);

export const useChartData = () => useContext(ChartDataContext);

export const ChartDataContextConsumer = ChartDataContext.Consumer;

export interface ChartDataContextProps {
    unit: string
    yLabel: string
    children
}

export const ChartDataContextProvider = ({ children, unit, yLabel }: ChartDataContextProps) => {
    const [granularity, setGranularity] = useState<Granularity>("hour");
    const [chartUnit, setUnit] = useState<string>(unit);
    const [chartYLabel, setYLabel] = useState<string>(yLabel);


    // SETTING THE VALUES
    return <ChartDataContext.Provider value={{
        granularity,
        setGranularity,
        unit: chartUnit,
        yLabel: chartYLabel
    }}>
        {children}
    </ChartDataContext.Provider>
}