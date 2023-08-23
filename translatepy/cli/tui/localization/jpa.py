"""
The japanese translation

Copyright
---------
Animenosekai
    Original Author, MIT License
"""

from translatepy.cli.tui.localization.base import Localization


class JapaneseLocalization(Localization):
    """
    The japanese translation for the TUI
    """
    __native__ = "日本語"

    input = "入力"
    result = "結果"
    service = "{service}から"
    language = "言語"
    language_notice = "言語変化を有効するには再起動して下さい"
    options = "設定"
    quit = "終了"
    theme = "テーマ"

    name = "名前"
    value = "内容"

    min = "低"
    average = "平均"
    max = "高"

    cancel = "戻る"
    quit_confirmation = "本当に終了しますか？"

    filter = "フィルター"

    action_translate = "翻訳"
    action_transliterate = "音訳"
    action_spellcheck = "スペル確認"
    action_language = "言語"
    action_example = "例文"
    action_dictionary = "辞書"
    action_text_to_speech = "読み上げ"
