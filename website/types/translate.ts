import { AUTOMATIC, ENGLISH, Language } from "./language"

import { Request } from "./request"
import { Result } from "./result"

export interface TranslationResult extends Result {
    dest_lang: Language
    translation: string
}

export interface ClientTranslationResult extends TranslationResult {
    default?: boolean
}

export const DEFAULT_TRANSLATION_RESULT: ClientTranslationResult = {
    service: "...",
    source: "",
    source_lang: AUTOMATIC,
    dest_lang: ENGLISH,
    translation: "",
    default: true
}

export const DEFAULT_TRANSLATION_REQUEST: Request<ClientTranslationResult> = {
    success: true,
    data: DEFAULT_TRANSLATION_RESULT
}