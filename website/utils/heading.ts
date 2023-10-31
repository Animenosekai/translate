const ignoredCharacters = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "{", "}", "[", "]", "|", "\\", "/", ":", ";", "\"", "'", "<", ">", ",", ".", "?"]

export const headingLink = (name: string, registry?: string[]) => {
    if (!registry) {
        registry = []
    }
    let result = ""
    for (const c of name.toLowerCase().replace(" ", "-")) {
        if (ignoredCharacters.includes(c) || (c === "-" && result.endsWith("-"))) {
            continue
        }
        result += c
    }
    result = result.replace(" ", "-")
    const linkCount = registry.filter(val => val == result).length
    registry.push(result)
    if (linkCount > 0) {
        return `${result}-${linkCount}`
    }
    return result
}