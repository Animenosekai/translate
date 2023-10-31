import { ClientTranslationResult } from "./translate";
import { Result } from "./result";

export interface HTMLClientTranslationResult extends Result {
    result: string
    nodes: HTMLTranslationNode[]
}

export interface HTMLTranslationNode {
    node: string
    result?: ClientTranslationResult
    position: number
}
