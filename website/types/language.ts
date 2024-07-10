import Localization from "localizations/base"
import { Result } from "./result"

export interface Language {
    alpha3: string
    id: string
    alpha3b?: string
    alpha3t?: string
    alpha2?: string
    extra?: Extra
    foreign?: Foreign
    name: string
}

export const getLanguageName = (lang: Language, localization: Localization) => {
    if (!lang) {
        return ""
    }
    return (localization.foreign && lang.foreign) ? lang.foreign[localization.foreign] : lang.name
}



export interface Extra {
    scope: string
    type: string
}

export interface Foreign {
    afrikaans: string
    dutch: string
    bosnian: string
    croatian: string
    czech: string
    slovak: string
    danish: string
    norwegian: string
    swedish: string
    indonesian: string
    javanese: string
    sundanese: string
    albanian: string
    amharic: string
    arabic: string
    armenian: string
    azerbaijani: string
    basque: string
    belarusian: string
    bengali: string
    bulgarian: string
    burmese: string
    catalan: string
    chinese: string
    esperanto: string
    estonian: string
    finnish: string
    french: string
    galician: string
    georgian: string
    german: string
    gujarati: string
    haitian: string
    hebrew: string
    hindi: string
    hungarian: string
    icelandic: string
    irish: string
    italian: string
    japanese: string
    kannada: string
    kazakh: string
    khmer: string
    kirghiz: string
    korean: string
    lao: string
    latin: string
    latvian: string
    lithuanian: string
    luxembourgish: string
    macedonian: string
    malagasy: string
    malay: string
    maltese: string
    maori: string
    marathi: string
    moderngreek: string
    mongolian: string
    nepali: string
    panjabi: string
    persian: string
    polish: string
    portuguese: string
    romanian: string
    russian: string
    scottishgaelic: string
    serbian: string
    sinhala: string
    slovenian: string
    spanish: string
    swahili: string
    tagalog: string
    tajik: string
    tamil: string
    telugu: string
    thai: string
    turkish: string
    ukrainian: string
    urdu: string
    uzbek: string
    vietnamese: string
    welsh: string
    xhosa: string
    yiddish: string
    zulu: string
}

export interface LanguageResult extends Result { }

export const AUTOMATIC: Language = {
    alpha3: "auto",
    id: "auto",
    alpha2: "auto",
    alpha3b: undefined,
    alpha3t: undefined,
    extra: {
        scope: "individual",
        type: "living"
    },
    foreign: {
        albanian: "Automatik",
        malay: "Automatik",
        azerbaijani: "Avtomatik",
        uzbek: "Avtomatik",
        bosnian: "Automatski",
        croatian: "Automatski",
        czech: "Automatický",
        slovak: "Automatický",
        danish: "Automatisk",
        norwegian: "Automatisk",
        swedish: "Automatisk",
        dutch: "Automatisch",
        german: "Automatisch",
        haitian: "Otomatik",
        turkish: "Otomatik",
        hindi: "स्वचालित",
        nepali: "स्वचालित",
        indonesian: "Otomatis",
        javanese: "Otomatis",
        sundanese: "Otomatis",
        persian: "خودکار",
        urdu: "خودکار",
        portuguese: "Automática",
        spanish: "Automática",
        afrikaans: "Outomatiese",
        amharic: "አውቶማቲክ",
        arabic: "تلقائي",
        armenian: "Ավտոմատ",
        basque: "Automatiko",
        belarusian: "Аўтаматычны",
        bengali: "স্বয়ংক্রিয়",
        bulgarian: "Автоматичен",
        burmese: "အလိုအလျောက်",
        catalan: "Automàtica",
        chinese: "自动",
        esperanto: "Aŭtomata",
        estonian: "Automaatne",
        finnish: "Automaattinen",
        french: "Automatique",
        galician: "Automático",
        georgian: "ავტომატური",
        gujarati: "સ્વચાલિત",
        hebrew: "אוֹטוֹמָטִי",
        hungarian: "Automatikus",
        icelandic: "Sjálfvirkt",
        irish: "Uathoibríoch",
        italian: "Automatico",
        japanese: "自動",
        kannada: "ಸ್ವಯಂಚಾಲಿತ",
        kazakh: "Автоматты",
        khmer: "ដោយស្វ័យប្រវត្តិ",
        kirghiz: "Автоматтык",
        korean: "자동적 인",
        lao: "ອັດຕະໂນມັດ",
        latin: "Automatic",
        latvian: "Automātiska",
        lithuanian: "Automatinis",
        luxembourgish: "Automatesch",
        macedonian: "Автоматски",
        malagasy: "Mandeha Ho Azy",
        maltese: "Awtomatiku",
        maori: "Aunoa",
        marathi: "स्वयंचलित",
        moderngreek: "Αυτόματο",
        mongolian: "Автомат",
        panjabi: "ਆਟੋਮੈਟਿਕ",
        polish: "Automatyczny",
        romanian: "Automat",
        russian: "Автоматический",
        scottishgaelic: "Fèin-Ghluasadach",
        serbian: "Аутоматски",
        sinhala: "ස්වයංක්‍රීය",
        slovenian: "Samodejno",
        swahili: "Moja Kwa Moja",
        tagalog: "Awtomatiko",
        tajik: "Худкор",
        tamil: "தானியங்கி",
        telugu: "ఆటోమేటిక్",
        thai: "อัตโนมัติ",
        ukrainian: "Автоматичний",
        vietnamese: "Tự Động",
        welsh: "Awtomatig",
        xhosa: "Ngokuzenzekelayo",
        yiddish: "אויטאָמאַטיש",
        zulu: "Okuzenzakalelayo"
    },
    name: "Automatic"
}

export const ENGLISH: Language = {
    alpha3: "eng",
    id: "eng",
    alpha3b: "eng",
    alpha3t: "eng",
    alpha2: "en",
    extra: {
        scope: "individual",
        type: "living"
    },
    foreign: {
        afrikaans: "Engels",
        dutch: "Engels",
        bosnian: "Engleski",
        croatian: "Engleski",
        czech: "Angličtina",
        slovak: "Angličtina",
        danish: "Engelsk",
        norwegian: "Engelsk",
        swedish: "Engelsk",
        indonesian: "Inggris",
        javanese: "Inggris",
        sundanese: "Inggris",
        albanian: "Anglisht",
        amharic: "እንግሊዝኛ",
        arabic: "الإنجليزية",
        armenian: "Անգլերեն",
        azerbaijani: "Ingilis",
        basque: "Ingelesez",
        belarusian: "Англійская",
        bengali: "ইংরেজি",
        bulgarian: "Английски",
        burmese: "အင်္ဂလိပ်",
        catalan: "Anglès",
        chinese: "英语",
        esperanto: "Angla",
        estonian: "Inglise",
        finnish: "Englanti",
        french: "Anglaise",
        galician: "Inglés",
        georgian: "ინგლისური",
        german: "Englisch",
        gujarati: "અંગ્રેજી",
        haitian: "Anglè",
        hebrew: "אנגלית",
        hindi: "अंग्रेज़ी",
        hungarian: "Angol",
        icelandic: "Enska",
        irish: "Béarla",
        italian: "Inglese",
        japanese: "英語",
        kannada: "ಆಂಗ್ಲ",
        kazakh: "Қазақша",
        khmer: "ភាសាអង់គ្លេស",
        kirghiz: "Англисче",
        korean: "영어",
        lao: "ອັງກິດ",
        latin: "Anglicus",
        latvian: "Angļu",
        lithuanian: "Anglų",
        luxembourgish: "Englesch",
        macedonian: "Англиски",
        malagasy: "Anglisy",
        malay: "Bahasa Inggeris",
        maltese: "Bl-Ingliż",
        maori: "Ingarihi",
        marathi: "इंग्रजी",
        moderngreek: "Αγγλικά",
        mongolian: "Англи Хэл",
        nepali: "अंग्रेजी",
        panjabi: "ਅੰਗਰੇਜ਼ੀ",
        persian: "انګلیسي...",
        polish: "Język Angielski",
        portuguese: "Inglês",
        romanian: "Engleză",
        russian: "Английский",
        scottishgaelic: "Sasannach",
        serbian: "Енглески Језик",
        sinhala: "ඉංග්රීසි",
        slovenian: "Angleščina",
        spanish: "Inglesa",
        swahili: "Kiingereza",
        tagalog: "Ingles",
        tajik: "Англисӣ",
        tamil: "ஆங்கிலம்",
        telugu: "ఆంగ్ల",
        thai: "อังกฤษ",
        turkish: "Ingilizce",
        ukrainian: "Англійська",
        urdu: "انگریزی",
        uzbek: "Inglizcha",
        vietnamese: "Tiếng Anh",
        welsh: "Saesneg",
        xhosa: "Isingesi",
        yiddish: "ענגליש",
        zulu: "Isingisi"
    },
    name: "English"
}