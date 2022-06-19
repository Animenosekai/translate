import { Area, AreaChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import React, { useEffect, useState } from "react";
import { generateColorID, generateColorURL } from "utils/color";

import { CustomTooltip } from "./tooltip";
import { Granularity } from "types/granularity";
import { Pagination } from '@nextui-org/react';
import { generateRandomColor } from "utils/random";
import { getDateWithGranularity } from "utils/date";
import { request } from "lib/request";
import { useLanguage } from "contexts/language";
import { useServicesColor } from "contexts/servicesColor";

const granularities: Array<Granularity> = [
    "hour",
    "day",
    "month",
    "year"
]

export const Chart = ({ endpoint }: { endpoint: string }) => {
    const [granularity, setGranularity] = useState<Granularity>(granularities[0]);
    const [data, setData] = useState<{ services: string[], results: { __timestamp__: number, [key: string]: any }[] }>(null);
    const [resizeCounter, setResizeCounter] = useState<number>(0);
    const { servicesColor, addColor } = useServicesColor();
    const { strings } = useLanguage();

    useEffect(() => {
        const listener = () => {
            setResizeCounter(c => c + 1);
        }
        window.addEventListener("resize", listener)
        return () => {
            return window.removeEventListener("resize", listener)
        }
    }, [])

    useEffect(() => {
        request(endpoint, {
            method: "GET",
            params: {
                granularity
            }
        }).then(response => {
            if (response.success) {
                setData(response.data);
            }
            // console.log(data);
        }).catch(error => {
            // console.log(error);
        })
    }, [endpoint, granularity]);


    useEffect(() => {
        document.querySelectorAll("#chart-pagination").forEach(el => {
            let counter = 0;
            el.querySelectorAll("span").forEach(span => {
                span.textContent = strings.labels.granularities[counter].slice(0, 1).toUpperCase();
                counter++;
            })
        })
    }, [strings]);

    return <div className="flex flex-col">
        <div className="m-4 self-end">
            <Pagination id="chart-pagination" shadow onChange={page => { setGranularity(granularities[page - 1]) }} total={granularities.length} controls={false} />
        </div>

        <ResponsiveContainer width="80%" height={400} key={resizeCounter}>

            <AreaChart data={data?.results}
                margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
                <defs>
                    {
                        data?.services.map((service, index) => {
                            if (!servicesColor[service]) {
                                const newColor = generateRandomColor();
                                servicesColor[service] = newColor
                                addColor(service, newColor);
                            }
                            return <linearGradient key={index} id={generateColorID(service)}
                                x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor={servicesColor[service]} stopOpacity={0.8} />
                                <stop offset="95%" stopColor={servicesColor[service]} stopOpacity={0.2} />
                            </linearGradient>
                        })
                    }
                </defs>
                <XAxis dataKey="__timestamp__" tickFormatter={value => {
                    // console.log(value, index)
                    const newDate = new Date(value * 1000)
                    return getDateWithGranularity(newDate, granularity, strings.labels.months)
                }} />
                <YAxis />
                <CartesianGrid strokeDasharray="3 3" />
                <Tooltip content={CustomTooltip} />
                {
                    data?.services.map((service, index) => {
                        const colorURL = generateColorURL(service)
                        return <Area type="monotone" dataKey={service} stroke={colorURL} fill={colorURL} key={index} />
                    })
                }
            </AreaChart>
        </ResponsiveContainer>
    </div>
}
