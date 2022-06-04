import { Request } from "./base"

export interface TranslateRequest extends Request {
    data: TranslationResult
}

export interface TranslationResult {
    services: string[]
    source: string
    sourceLang: string[]
    destLang: string
    result: string
}
