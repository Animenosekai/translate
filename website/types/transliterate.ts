import { LanguageDetailsResult } from "./languageDetails"
import { Request } from "./base"

export interface TransliterateRequest extends Request {
    data: TransliterateResult
}

export interface TransliterateResult {
    service: string
    source: string
    sourceLanguage: LanguageDetailsResult
    destinationLanguage: LanguageDetailsResult
    result: string
}
