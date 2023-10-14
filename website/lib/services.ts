export const services: {
    [key: string]: string
} = {
    "Google": "https://translate.google.com",
    "Yandex": "https://translate.yandex.com",
    "Microsoft Translate": "https://translator.microsoft.com",
    "Reverso": "https://www.reverso.net/text-translation",
    "Microsoft Bing": "https://www.bing.com/translator",
    "Libre": "https://libretranslate.com",
    "Translate.com": "https://www.translate.com",
    "MyMemory": "https://mymemory.translated.net",
    "DeepL": "https://www.deepl.com/translator"
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
