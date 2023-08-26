import { Language } from "./language"
import { Result } from "./result"

export interface SpellcheckResult extends Result {
    corrected: string
    rich: boolean
}

export interface SpellcheckMistake {
    start: number
    end: number
    corrected: string
    message?: string
    rule?: string
}

export interface RichSpellcheckResult extends Result {
    mistakes: SpellcheckMistake[]
    corrected: string
    rich: boolean
}