import { Request } from "./base"

export interface SpellcheckRequest extends Request {
    data: SpellcheckResult
}

export interface SpellcheckResult {
    service: string
    source: string
    sourceLang: string
    result: string
}
