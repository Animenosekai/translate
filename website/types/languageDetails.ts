import { Request } from "./base"

type languages = "af" | "am" | "ar" | "az" | "be" | "bg" | "bn" | "bs" | "ca" | "ceb" | "co" | "cs" | "cy" | "da" | "de" | "el" | "en" | "eo" | "es" | "et" | "eu" | "fa" | "fi" | "fr" | "fy" | "ga" | "gd" | "gl" | "gu" | "ha" | "haw" | "hi" | "hmn" | "hr" | "ht" | "hu" | "hy" | "id" | "ig" | "is" | "it" | "he" | "ja" | "jv" | "ka" | "kk" | "km" | "kn" | "ko" | "ku" | "ky" | "la" | "lb" | "lo" | "lt" | "lv" | "mg" | "mi" | "mk" | "ml" | "mn" | "mr" | "ms" | "mt" | "my" | "ne" | "nl" | "no" | "ny" | "or" | "pa" | "pl" | "ps" | "pt" | "ro" | "ru" | "sd" | "si" | "sk" | "sl" | "sm" | "sn" | "so" | "sq" | "sr" | "st" | "su" | "sv" | "sw" | "ta" | "te" | "tg" | "th" | "tl" | "tr" | "ug" | "uk" | "ur" | "uz" | "vi" | "xh" | "yi" | "yo" | "zh" | "zu"

export interface LanguageDetailsRequest extends Request {
    data: LanguageDetailsResult
}

export interface LanguageSearchRequest extends Request {
    data: {
        languages: SearchResultContainer[]
    }
}

export interface SearchResultContainer {
    string: string,
    similarity: number,
    language: LanguageDetailsResult
}

export interface LanguageDetailsResult {
    id: string
    alpha2: string
    alpha3b: string
    alpha3t: string
    alpha3: string
    name: string
    inForeignLanguages: { [key in languages]?: string }
    extra: Extra
}

export interface Extra {
    scope?: string
    type?: string
}
