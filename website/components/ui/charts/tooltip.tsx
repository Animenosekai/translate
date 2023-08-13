import { getDateWithGranularity } from "utils/date";
import { useChartData } from "contexts/chartData";
import { useLanguage } from "contexts/language";
import { useServicesColor } from "contexts/servicesColor";

export const CustomTooltip = ({ active, payload, label }) => {
    const { servicesColor } = useServicesColor();
    const { strings } = useLanguage();
    const { granularity, unit } = useChartData();
    if (active && payload && payload.length) {
        // console.log(payload)
        payload.sort((a: { value: number; }, b: { value: number; }) => {
            return b.value - a.value;
        });
        return (
            <div className="flex flex-col p-3 bg-white bg-opacity-75 rounded">
                <span className="text-lg">{getDateWithGranularity(new Date(label * 1000), granularity, strings.labels.months)}</span>
                <div className="flex flex-col">
                    {
                        payload.map((item, index) => {
                            return <div className="flex flex-row gap-2" key={index} style={{
                                color: servicesColor[item.name]
                            }}>
                                <span>{item.name}:</span>
                                <span>{item.value}</span>
                                <span>{unit}</span>
                            </div>
                        })
                    }
                </div>
            </div>
        );
    }

    return null;
};