import EnglishLocalization from "./eng";
import Localization from "./base";
import TemplateString from "utils/string";

export const JapaneseLocalization: Localization = {
    ...EnglishLocalization,
    language: "jpn",
    name: "日本語",
    foreign: "japanese",
    placeholders: {
        translationTextArea: '翻訳する文章を入力してください...',
    },
    buttons: {
        translate: '翻訳'
    },
    headings: {
        otherTranslations: "他の翻訳"
    },
    labels: {
        source: "Source",
        transliterationBy: new TemplateString("{service} からの音訳"),
        spellcheckBy: new TemplateString("{service} からのスペルチェック"),
        translationFailure: "エラー"
    },
    pages: {
        translate: "翻訳",
        documentation: "ドキュメント"
    },
    notifications: {
        copied: "クリップボードにコピーしました"
    }
}

export default JapaneseLocalization