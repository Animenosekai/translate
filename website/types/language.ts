import { Result } from "./result"

export interface Language {
    alpha3: string
    id: string
    alpha3b?: string
    alpha3t?: string
    alpha2?: string
    extra?: Extra
    foreign?: Foreign
    name: string
}

export interface Extra {
    scope: string
    type: string
}

export interface Foreign {
    afrikaans: string
    dutch: string
    bosnian: string
    croatian: string
    czech: string
    slovak: string
    danish: string
    norwegian: string
    swedish: string
    indonesian: string
    javanese: string
    sundanese: string
    albanian: string
    amharic: string
    arabic: string
    armenian: string
    azerbaijani: string
    basque: string
    belarusian: string
    bengali: string
    bulgarian: string
    burmese: string
    catalan: string
    chinese: string
    esperanto: string
    estonian: string
    finnish: string
    french: string
    galician: string
    georgian: string
    german: string
    gujarati: string
    haitian: string
    hebrew: string
    hindi: string
    hungarian: string
    icelandic: string
    irish: string
    italian: string
    japanese: string
    kannada: string
    kazakh: string
    khmer: string
    kirghiz: string
    korean: string
    lao: string
    latin: string
    latvian: string
    lithuanian: string
    luxembourgish: string
    macedonian: string
    malagasy: string
    malay: string
    maltese: string
    maori: string
    marathi: string
    moderngreek: string
    mongolian: string
    nepali: string
    panjabi: string
    persian: string
    polish: string
    portuguese: string
    romanian: string
    russian: string
    scottishgaelic: string
    serbian: string
    sinhala: string
    slovenian: string
    spanish: string
    swahili: string
    tagalog: string
    tajik: string
    tamil: string
    telugu: string
    thai: string
    turkish: string
    ukrainian: string
    urdu: string
    uzbek: string
    vietnamese: string
    welsh: string
    xhosa: string
    yiddish: string
    zulu: string
}

export interface LanguageResult extends Result { }
