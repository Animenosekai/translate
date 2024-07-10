"""
The french translation

Copyright
---------
Animenosekai
    Original Author, MIT License
"""

from translatepy.cli.tui.localization.base import Localization


class FrenchLocalization(Localization):
    """
    The french translation for the TUI
    """
    __native__ = "Français"

    input = "Entrée"
    result = "Résultat"
    service = "de {service}"
    language = "Langage"
    language_notice = "Vous devez relancer l'application pour que les changements prennent effet"
    options = "Options"
    quit = "Quitter"
    theme = "Thème"

    name = "Nom"
    value = "Valeur"

    min = "Min"
    average = "Moy"
    max = "Max"

    cancel = "Revenir"
    quit_confirmation = "Voulez-vous vraiment quitter ?"

    filter = "Filtre"

    action_translate = "Traduction"
    action_transliterate = "Translitération"
    action_spellcheck = "Correcteur ortho."
    action_language = "Langue"
    action_example = "Example"
    action_dictionary = "Dictionnaire"
    action_text_to_speech = "Synthèse voc."
