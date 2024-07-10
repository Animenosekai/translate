export const range = (size: number, startAt: number = 0): ReadonlyArray<number> => {
    if (size <= 0 || !size) {
        return []
    }
    return [...Array(size).keys()].map(i => i + startAt);
}