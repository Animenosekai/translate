export interface Vector {
    id: string
    string: string
    value: string
}

export interface SearchResult {
    vector: Vector
    similarity: number
}

export interface LanguageSearchResult {
    string: string
    similarity: number
    language: string
}