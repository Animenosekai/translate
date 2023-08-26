import { Result } from "./result";
import { TranslationResult } from "./translate";

export interface HTMLTranslationResult extends Result {
    result: string
    nodes: HTMLTranslationNode[]
}

export interface HTMLTranslationNode {
    node: string
    result?: TranslationResult
    position: number
}
