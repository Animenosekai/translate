import { Language } from "./language"
import { Result } from "./result"

export interface TranslationResult extends Result {
    dest_lang: Language
    translation: string
}
