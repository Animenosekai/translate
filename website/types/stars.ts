import { Request } from "./base"

export interface StarRequest extends Request {
    data: StarredTranslation
}

export interface StarredTranslationLanguage {
    source: string
    dest: string
}

export interface StarredTranslation {
    _id: string
    language: StarredTranslationLanguage
    source: string
    result: string
    services: string[]
    users: number
}