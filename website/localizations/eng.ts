import { TemplateString } from "utils/string";

class EnglishLocalization {
    language: string = "eng";
    alpha2: string = "en";
    name: string = "English";
    placeholders = {
        translationTextArea: 'Enter your text to translate...',
    }
    buttons = {
        translate: 'Translate'
    }
    heading = {
        otherTranslations: "Other translations",
    }
    labels = {
        source: "Source",
        transliterationBy: new TemplateString("Transliteration by {service}"),
        translationFailure: "Failed",
    }
    pages = {
        translate: "Translate",
        documentation: "Documentation",
        stats: "Stats"
    }
    notifications = {
        copied: "Copied to clipboard"
    }
}

export default EnglishLocalization