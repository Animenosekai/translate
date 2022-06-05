import EnglishLocalization from "./eng";
import { TemplateString } from "utils/string";

class FrenchLocalization extends EnglishLocalization {
    language: string = "fra";
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
        translationFailure: "Erreur",
    }
    pages = {
        translate: "Traduction",
        documentation: "Documentation",
        stats: "Statistiques"
    }
}

export default FrenchLocalization