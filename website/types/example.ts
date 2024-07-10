import { Result } from "./result"

export interface ExampleResult extends Result {
    example: string
    reference: string
    positions: number[]
}
