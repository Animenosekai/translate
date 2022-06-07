import EnglishLocalization from "./eng";
import { TemplateString } from "utils/string";

class JapaneseLocalization extends EnglishLocalization {
    language: string = "jpn";
    alpha2: string = "ja";
    name: string = "日本語";
    placeholders = {
        translationTextArea: '翻訳する文章を入力してください...',
    }
    buttons = {
        translate: '翻訳'
    }
    heading = {
        otherTranslations: "他の翻訳",
    }
    labels = {
        source: "Source",
        transliterationBy: new TemplateString("{service} からの音訳"),
        translationFailure: "エラー",
    }
    pages = {
        translate: "翻訳",
        documentation: "ドキュメンテーション",
        stats: "統計"
    }
    notifications: { copied: string; } = {
        copied: "クリップボードにコピーしました"
    }
}

export default JapaneseLocalization