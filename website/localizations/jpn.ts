import EnglishLocalization, { DocumentationElement } from "./eng";

import { TemplateString } from "utils/string";

class JapaneseLocalization extends EnglishLocalization {
    language: string = "jpn";
    alpha2: string = "ja";
    name: string = "日本語";
    docsTranslated: boolean = true
    placeholders = {
        translationTextArea: '翻訳する文章を入力してください...',
    }
    buttons = {
        translate: '翻訳'
    }
    heading = {
        otherTranslations: "他の翻訳",
        timeTakenForTranslation: "翻訳する時間",
        errorsCount: "エラー数",
    }
    labels = {
        source: "Source",
        transliterationBy: new TemplateString("{service} からの音訳"),
        spellcheckBy: new TemplateString("{service} からのスペルチェック"),
        translationFailure: "エラー",
        months: ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
        granularities: ["時間", "日", "月", "年"]
    }
    pages = {
        translate: "翻訳",
        documentation: "ドキュメント",
        stats: "統計"
    }
    notifications: { copied: string; } = {
        copied: "クリップボードにコピーしました"
    }

    documentation: DocumentationElement[] = [
        { name: "README" },
        {
            name: "Pythonドキュメント",
            children: [
                { name: "README" },
                { name: "Installation" },
                { name: "References" },
                { name: "Plugins" }
            ]
        },
        {
            name: "CLIでの利用",
            children: [
                { name: "README" },
                { name: "JSON" },
                { name: "Shell" },
                { name: "Server" },
                {
                    name: "サーバーのドキュメント",
                    children: [
                        { name: "はじめに" },
                        {
                            name: "セクション",
                            children: [
                                { name: "Language" },
                                { name: "Translation" }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            name: "サイトでの利用"
        },
        {
            name: "APIドキュメント",
            children: [
                { name: "README" },
                { name: "はじめに" },
                { name: "Objects" },
                { name: "Rate Limits" },
                {
                    name: "セクション",
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

export default JapaneseLocalization