import { LanguageDetailsResult } from "./languageDetails"
import { Request } from "./base"

export interface TranslateRequest extends Request {
    data: TranslationResult
}

export interface TranslationResult {
    services: string[]
    source: string
    sourceLanguage: string[]
    destinationLanguage: LanguageDetailsResult
    result: string
}
