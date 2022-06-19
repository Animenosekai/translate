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
        timeTakenForTranslation: "Time taken for translation",
        errorsCount: "Errors count",
    }
    labels = {
        source: "Source",
        transliterationBy: new TemplateString("Transliteration by {service}"),
        spellcheckBy: new TemplateString("Spellchecked by {service}"),
        translationFailure: "Failed",
        months: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        granularities: ["Hour", "Day", "Month", "Year"]
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