export const links: {
    [key: string]: string
} = {
    "Bing Translate": "",
    "DeepL Android": "",
    "DeepL Web": "",
    "Google Translate": "https://translate.google.com",
    "Google Translate (batchexecute)": "https://translate.google.com",
    "Google Translate (API)": "https://translate.google.com",
    "Libre": "",
    "MyMemory": "",
    "Reverso": "",
    "Translate.com": "",
    "Yandex Translate": "",
    "Microsoft Translate": "",
    "Microsoft Translate (API)": "",
    "Microsoft Translate (SwiftKey)": "",
    "Microsoft Translate (TranslateArray)": "",
    "QCRI": "",
    "PONS": "",
    "Papago": ""
}

/**
 * A class representing a translation service
 * 
 * This automatically gets the service homepage to credit the translation.
 */
export class Service {
    name: string
    link: string

    constructor(name) {
        this.name = name
        const link = links[name]
        this.link = link ? link : ""
    }
}
