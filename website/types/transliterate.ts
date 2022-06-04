import { Request } from "./base"

export interface TransliterateRequest extends Request {
    data: TransliterateResult
}

export interface TransliterateResult {
    service: string
    source: string
    sourceLang: string
    destLang: string
    result: string
}
