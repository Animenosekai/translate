import { Granularity } from "types/granularity"

export const getDateWithGranularity = (date: Date, granularity: Granularity, monthsLocalization: string[] = null): string => {
    if (monthsLocalization === null) {
        monthsLocalization = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    }
    switch (granularity) {
        case "hour":
            return date.getHours() + ":00";
        case "day":
            return date.toLocaleDateString();
        case "month":
            return monthsLocalization[date.getMonth()];
        case "year":
            return date.getFullYear().toString();
        default:
            return date.toLocaleDateString();
    }
}