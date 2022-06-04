import { Request } from "./base"

export interface TranslateRequest extends Request {
    data: TranslateResult
}

export interface TranslateResult {
    service: string
    source: string
    sourceLang: string
    destLang: string
    result: string
}
