import { TemplateString } from "utils/string"

export interface DocumentationElement {
    name: string
    children?: DocumentationElement[]
}

export interface LocalizationPlaceholders {
    translationTextArea: string
}

export interface LocalizationButtons {
    translate: string
}

export interface LocalizationHeadings {
    otherTranslations: string
}

export interface LocalizationLabels {
    source: string
    transliterationBy: TemplateString
    spellcheckBy: TemplateString
    translationFailure: string
}

export interface LocalizationPages {
    translate: string
    documentation: string
}

export interface LocalizationNotifications {
    copied: string
}

export interface Localization {
    language: string
    name: string
    foreign?: string // the key in `Language.foreign`
    welcome: string
    placeholders: LocalizationPlaceholders
    buttons: LocalizationButtons
    headings: LocalizationHeadings
    labels: LocalizationLabels
    pages: LocalizationPages
    notifications: LocalizationNotifications
    documentation: DocumentationElement[]
}

export default Localization