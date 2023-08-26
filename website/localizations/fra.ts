import EnglishLocalization from "./eng";
import Localization from "./base";
import { TemplateString } from "utils/string";

export const FrenchLocalization: Localization = {
    ...EnglishLocalization,
    language: "fra",
    name: "Français",
    foreign: "french",
    placeholders: {
        translationTextArea: 'Entrez le texte à traduire...',
    },
    buttons: {
        translate: 'Traduire'
    },
    headings: {
        otherTranslations: "Autres traductions"
    },
    labels: {
        source: "Source",
        transliterationBy: new TemplateString("Translitération de {service}"),
        spellcheckBy: new TemplateString("Correction par {service}"),
        translationFailure: "Erreur"
    },
    pages: {
        translate: "Traduction",
        documentation: "Documentation"
    },
    notifications: {
        copied: "Copié dans le presse-papier"
    },

}

export default FrenchLocalization