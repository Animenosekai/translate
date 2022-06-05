import { LanguageDetailsResult } from "./languageDetails"
import { Request } from "./base"

export interface TranslateRequest extends Request {
    data: TranslateResult
    loading?: boolean // this only exists client-side
}

export interface TranslateResult {
    service: string
    source: string
    sourceLanguage: LanguageDetailsResult
    destinationLanguage: LanguageDetailsResult
    result: string
}


export const DefaultTranslateRequest: TranslateRequest = {
    success: true,
    data: {
        service: "...",
        source: "",
        sourceLanguage: {
            "id": "auto",
            "alpha2": "auto",
            "alpha3b": "auto",
            "alpha3t": "auto",
            "alpha3": "auto",
            "name": "Automatic",
            "inForeignLanguages": {},
            "extra": {}
        },
        destinationLanguage: {
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English",
            "inForeignLanguages": {},
            "extra": {
                "type": "Living",
                "scope": "Individual"
            }
        },
        result: "",
    },
}