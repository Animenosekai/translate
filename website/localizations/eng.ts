import { TemplateString } from "utils/string";

export interface DocumentationElement {
    name: string
    children?: DocumentationElement[]
}

class EnglishLocalization {
    language: string = "eng";
    alpha2: string = "en";
    name: string = "English";
    docsTranslated: boolean = true
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


    documentation: DocumentationElement[] = [
        { name: "README" },
        {
            name: "Python Documentation",
            children: [
                { name: "README" },
                { name: "Installation" },
                { name: "References" },
                { name: "Plugins" }
            ]
        },
        {
            name: "CLI Usage",
            children: [
                { name: "README" },
                { name: "JSON" },
                { name: "Shell" },
                { name: "Server" },
                {
                    name: "Server Documentation",
                    children: [
                        { name: "Getting Started" },
                        {
                            name: "Sections",
                            children: [
                                { name: "Language" },
                                { name: "Translation" }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            name: "Website Usage"
        },
        {
            name: "API Documentation",
            children: [
                { name: "README" },
                { name: "Getting Started" },
                { name: "Objects" },
                { name: "Rate Limits" },
                {
                    name: "Sections",
                    children: [
                        { name: "Language" },
                        { name: "Translation" },
                        { name: "Stars" },
                        { name: "Stats" }
                    ]
                }
            ]
        }
    ]
}

export default EnglishLocalization