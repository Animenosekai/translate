import Localization from "./base";
import { TemplateString } from "utils/string";

export const EnglishLocalization: Localization = {
    language: "eng",
    name: "English",
    placeholders: {
        translationTextArea: 'Enter your text to translate...',
    },
    buttons: {
        translate: 'Translate'
    },
    headings: {
        otherTranslations: "Other translations"
    },
    labels: {
        source: "Source",
        transliterationBy: new TemplateString("Transliteration by {service}"),
        spellcheckBy: new TemplateString("Spellchecked by {service}"),
        translationFailure: "Failed"
    },
    pages: {
        translate: "Translate",
        documentation: "Documentation"
    },
    notifications: {
        copied: "Copied to clipboard"
    },
    documentation: [
        {
            name: "Python Documentation",
            children: [
                { name: "Installation" },
                { name: "References" },
                { name: "Models" },
                { name: "Plugins" }
            ]
        },
        {
            name: "CLI Usage",
            children: [
                { name: "JSON" },
                { name: "Shell" },
                { name: "TUI" },
                { name: "Server" }
            ]
        },
        {
            name: "Website Usage",
            children: [
                { name: "Home" },
                { name: "Translation" },
                { name: "Stats" },
                { name: "Settings" },
                { name: "Privacy Policy" }
            ]
        },
        {
            name: "API Documentation",
            children: [
                { name: "Getting Started" },
                { name: "Objects" },
                {
                    name: "Sections",
                    children: [
                        { name: "Language" },
                        { name: "Work" }
                    ]
                }
            ]
        }
    ]
}

export default EnglishLocalization