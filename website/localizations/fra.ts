import EnglishLocalization, { DocumentationElement } from "./eng";

import { TemplateString } from "utils/string";

class FrenchLocalization extends EnglishLocalization {
    language: string = "fra";
    alpha2: string = "fr";
    name: string = "Français";
    docsTranslated: boolean = true
    placeholders = {
        translationTextArea: 'Entrez le texte à traduire...',
    }
    buttons = {
        translate: 'Traduire'
    }
    heading = {
        otherTranslations: "Autres traductions",
        timeTakenForTranslation: "Temps pris à traduire",
        errorsCount: "Nombre d'erreurs",
    }
    labels = {
        source: "Source",
        transliterationBy: new TemplateString("Translitération de {service}"),
        spellcheckBy: new TemplateString("Correction par {service}"),
        translationFailure: "Erreur",
        months: ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"],
        granularities: ["Heure", "Jour", "Mois", "Année"]
    }
    pages = {
        translate: "Traduction",
        documentation: "Documentation",
        stats: "Statistiques"
    }
    notifications: { copied: string; } = {
        copied: "Copié dans le presse-papier"
    }

    documentation: DocumentationElement[] = [
        { name: "README" },
        {
            name: "Documentation Python",
            children: [
                { name: "README" },
                { name: "Installation" },
                { name: "References" },
                { name: "Plugins" }
            ]
        },
        {
            name: "Utilisation par CLI",
            children: [
                { name: "README" },
                { name: "JSON" },
                { name: "Shell" },
                { name: "Serveur" },
                { 
                    name: "Documentation du Serveur", 
                    children: [
                        { name: "Pour commencer" },
                        {
                            name: "Sections",
                            children: [
                                { name: "Language" },
                                { name: "Translation" }
                            ]
                        }
                    ]
                },
            ]
        },
        {
            name: "Utilisation du site"
        },
        {
            name: "Documentation d'API",
            children: [
                { name: "README" },
                { name: "Pour commencer" },
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

export default FrenchLocalization