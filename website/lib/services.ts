export const services: {
    [key: string]: string
} = {
    "Bing Translate": "https://www.bing.com/translator",
    "DeepL Android": "https://www.deepl.com/en/mobile-apps/",
    "DeepL Web": "https://www.deepl.com/translator",
    "Google Translate": "https://translate.google.com",
    "Google Translate (batchexecute)": "https://translate.google.com",
    "Google Translate (API)": "https://translate.google.com",
    "Libre Translate": "https://libretranslate.com",
    "MyMemory": "https://mymemory.translated.net",
    "Reverso": "https://www.reverso.net/text-translation",
    "Translate.com": "https://www.translate.com",
    "Yandex Translate": "https://translate.yandex.com",
    "Microsoft Translate": "https://www.microsoft.com/en-us/translator/",
    "Microsoft Translate (API)": "https://www.microsoft.com/en-us/translator/",
    "Microsoft Translate (SwiftKey)": "https://www.microsoft.com/en-us/translator/",
    "Microsoft Translate (TranslateArray)": "https://www.microsoft.com/en-us/translator/",
    "QCRI": "https://mt.qcri.org/api",
    "PONS": "https://en.pons.com/text-translation",
    "Papago": "https://papago.naver.com"
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
        const link = services[name]
        this.link = link ? link : ""
    }
}
