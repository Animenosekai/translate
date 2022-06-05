import { LanguageDetailsResult } from "./languageDetails"
import { Request } from "./base"

export interface TranslateRequest extends Request {
    data: TranslateResult
}

export interface TranslateResult {
    service: string
    source: string
    sourceLanguage: LanguageDetailsResult
    destinationLanguage: LanguageDetailsResult
    result: string
}
