import EnglishLocalization from "./eng";
import { TemplateString } from "utils/string";

class FrenchLocalization extends EnglishLocalization {
    language: string = "fra";
    alpha2: string = "fr";
    name: string = "Français";
    placeholders = {
        translationTextArea: 'Entrez le texte à traduire...',
    }
    buttons = {
        translate: 'Traduire'
    }
    heading = {
        otherTranslations: "Autres traductions",
    }
    labels = {
        source: "Source",
        transliterationBy: new TemplateString("Translitération de {service}"),
        spellcheckBy: new TemplateString("Correction par {service}"),
        translationFailure: "Erreur",
    }
    pages = {
        translate: "Traduction",
        documentation: "Documentation",
        stats: "Statistiques"
    }
    notifications: { copied: string; } = {
        copied: "Copié dans le presse-papier"
    }
}

export default FrenchLocalization