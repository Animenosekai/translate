import EnglishLocalization from "./eng";
import Localization from "./base";
import { TemplateString } from "utils/string";

export const SpanishLocalization: Localization = {
    ...EnglishLocalization,
    language: "spa",
    foreign: "spanish",
    name: "Español",
    placeholders: {
        translationTextArea: 'Introduce el texto a traducir...',
    },
    buttons: {
        translate: 'Traducir'
    },
    headings: {
        otherTranslations: "Otras traducciones"
    },
    labels: {
        source: "Fuente",
        transliterationBy: new TemplateString("Transliteración de {service}"),
        spellcheckBy: new TemplateString("Corrección de {service}"),
        translationFailure: "Error"
    },
    pages: {
        translate: "Traducción",
        documentation: "Documentación"
    },
    notifications: {
        copied: "Copiado al portapapeles"
    }
}

export default SpanishLocalization