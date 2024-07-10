import Configuration from "config";
import EnglishLocalization from "./eng";
import Localization from "./base";
import { TemplateString } from "utils/string";

export const FrenchLocalization: Localization = {
    ...EnglishLocalization,
    language: "fra",
    name: "Français",
    foreign: "french",
    welcome: `Bienvenue sur translatepy ! 🎐
    Si vous souhaiter savoir comment ce site fonctionne, vous pouvez visiter la page GitHub du projet : https://github.com/Animenosekai/translate
    Si vous souhaiter comprendre commment les requêtes fonctionnent, vous pouvez les retrouver dans les docs : ${Configuration.origin}/documentation

    ✨ Bonne journée`,
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