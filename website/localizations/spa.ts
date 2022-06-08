import EnglishLocalization from "./eng";
import { TemplateString } from "utils/string";

class SpanishLocalization extends EnglishLocalization {
    language: string = "spa";
    alpha2: string = "es";
    name: string = "Español";
    placeholders = {
        translationTextArea: 'Introduce el texto a traducir...',
    }
    buttons = {
        translate: 'Traducir'
    }
    heading = {
        otherTranslations: "Otras traducciones",
    }
    labels = {
        source: "Fuente",
        transliterationBy: new TemplateString("Transliteración de {service}"),
        spellcheckBy: new TemplateString("Corrección de {service}"),
        translationFailure: "Error",
    }
    pages = {
        translate: "Traducción",
        documentation: "Documentación",
        stats: "Estadística"
    }
    notifications: { copied: string; } = {
        copied: "Copiado al portapapeles"
    }
}

export default SpanishLocalization