export const generateColorURL = (id: string) => {
    return `url(#${generateColorID(id)})`
}

export const generateColorID = (id: string) => {
    return `color__${id.replace(" ", "-")}`
}