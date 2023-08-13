import { Request } from "./base"

export interface LanguageRequest extends Request {
    data: LanguageResult
}

export interface LanguageResult {
    service: string
    source: string
    result: string
}