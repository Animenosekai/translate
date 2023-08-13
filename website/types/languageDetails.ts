import { Request } from "./base"

type languages = "af" | "am" | "ar" | "az" | "be" | "bg" | "bn" | "bs" | "ca" | "ceb" | "co" | "cs" | "cy" | "da" | "de" | "el" | "en" | "eo" | "es" | "et" | "eu" | "fa" | "fi" | "fr" | "fy" | "ga" | "gd" | "gl" | "gu" | "ha" | "haw" | "hi" | "hmn" | "hr" | "ht" | "hu" | "hy" | "id" | "ig" | "is" | "it" | "he" | "ja" | "jv" | "ka" | "kk" | "km" | "kn" | "ko" | "ku" | "ky" | "la" | "lb" | "lo" | "lt" | "lv" | "mg" | "mi" | "mk" | "ml" | "mn" | "mr" | "ms" | "mt" | "my" | "ne" | "nl" | "no" | "ny" | "or" | "pa" | "pl" | "ps" | "pt" | "ro" | "ru" | "sd" | "si" | "sk" | "sl" | "sm" | "sn" | "so" | "sq" | "sr" | "st" | "su" | "sv" | "sw" | "ta" | "te" | "tg" | "th" | "tl" | "tr" | "ug" | "uk" | "ur" | "uz" | "vi" | "xh" | "yi" | "yo" | "zh" | "zu"

export interface LanguageDetailsRequest extends Request {
    data: LanguageDetailsResult
}

export interface LanguageSearchRequest extends Request {
    data: {
        languages: SearchResultContainer[]
    }
}

export interface SearchResultContainer {
    string: string,
    similarity: number,
    language: LanguageDetailsResult
}

export interface LanguageDetailsResult {
    id: string
    similarity: number,
    alpha2: string
    alpha3b: string
    alpha3t: string
    alpha3: string
    name: string
    inForeignLanguages: { [key in languages]?: string }
    extra: Extra
}

export interface Extra {
    scope?: string
    type?: string
}


export const AutomaticDetailsRequest: SearchResultContainer = {
    string: "Automatic",
    similarity: 100,
    language: {
        "id": "auto",
        "name": "Automatic",
        "similarity": 100,
        "alpha2": "auto",
        "alpha3b": null,
        "alpha3t": null,
        "alpha3": "auto",
        "extra": {
            "type": "Living",
            "scope": "Individual"
        },
        "inForeignLanguages": {
            "af": "Outomatiese",
            "sq": "Automatik",
            "am": "አውቶማቲክ",
            "ar": "تلقائي",
            "hy": "Ավտոմատ",
            "az": "Avtomatik",
            "eu": "Automatiko",
            "be": "Аўтаматычны",
            "bn": "স্বয়ংক্রিয়",
            "bs": "Automatski",
            "bg": "Автоматичен",
            "ca": "Automàtica",
            "ceb": "Awtomatiko",
            "ny": "Basi",
            "co": "Automaticu",
            "hr": "Automatski",
            "cs": "Automatický",
            "da": "Automatisk",
            "nl": "Automatisch",
            "eo": "Aŭtomata",
            "et": "Automaatne",
            "tl": "Awtomatiko",
            "fi": "Automaattinen",
            "fr": "Automatique",
            "fy": "Automatysk",
            "gl": "Automático",
            "ka": "ავტომატური",
            "de": "Automatisch",
            "el": "Αυτόματο",
            "gu": "સ્વચાલિત",
            "ht": "Otomatik",
            "ha": "Atomatik",
            "haw": "Otomatoma",
            "hi": "स्वचालित",
            "hmn": "Tsis Siv Neeg",
            "hu": "Automatikus",
            "is": "Sjálfvirkt",
            "ig": "Akpaka",
            "id": "Otomatis",
            "ga": "Uathoibríoch",
            "it": "Automatico",
            "ja": "自動",
            "kn": "ಸ್ವಯಂಚಾಲಿತ",
            "kk": "Автоматты",
            "km": "ដោយស្វ័យប្រវត្តិ",
            "ko": "자동적 인",
            "ku": "Otomatîkî",
            "ky": "Автоматтык",
            "lo": "ອັດຕະໂນມັດ",
            "la": "Automatic",
            "lv": "Automātiska",
            "lt": "Automatinis",
            "lb": "Automatesch",
            "mk": "Автоматски",
            "mg": "Mandeha Ho Azy",
            "ms": "Automatik",
            "ml": "ഓട്ടോമാറ്റിക്",
            "mt": "Awtomatiku",
            "mi": "Aunoa",
            "mr": "स्वयंचलित",
            "mn": "Автомат",
            "my": "အလိုအလျောက်",
            "ne": "स्वचालित",
            "no": "Automatisk",
            "or": "ସ୍ୱୟଂଚାଳିତ |",
            "ps": "اتوماتیک",
            "fa": "خودکار",
            "pl": "Automatyczny",
            "pt": "Automática",
            "pa": "ਆਟੋਮੈਟਿਕ",
            "ro": "Automat",
            "ru": "Автоматический",
            "sm": "Otometi",
            "gd": "Fèin-Ghluasadach",
            "sr": "Аутоматски",
            "st": "Ka Boiketsetso",
            "sn": "Otomatiki",
            "sd": "خودڪار",
            "si": "ස්වයංක්‍රීය",
            "sk": "Automatický",
            "sl": "Samodejno",
            "so": "Otomatik Ah",
            "es": "Automática",
            "su": "Otomatis",
            "sw": "Moja Kwa Moja",
            "sv": "Automatisk",
            "tg": "Худкор",
            "ta": "தானியங்கி",
            "te": "ఆటోమేటిక్",
            "th": "อัตโนมัติ",
            "tr": "Otomatik",
            "uk": "Автоматичний",
            "ur": "خودکار",
            "ug": "ئاپتوماتىك",
            "uz": "Avtomatik",
            "vi": "Tự Động",
            "cy": "Awtomatig",
            "xh": "Ngokuzenzekelayo",
            "yi": "אויטאָמאַטיש",
            "yo": "Laifọwọyi",
            "zu": "Okuzenzakalelayo",
            "zh": "自动",
            "he": "אוֹטוֹמָטִי",
            "jv": "Otomatis",
            "en": "Automatic"
        }
    }
}