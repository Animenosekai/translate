import { Language } from "./language"
import { Result } from "./result"

export interface TransliterationResult extends Result {
    dest_lang: Language
    transliteration: string
}
