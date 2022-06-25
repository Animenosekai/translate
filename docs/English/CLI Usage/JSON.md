# JSON

You can also integrate translatepy into other languages using its JSON-formatted command line interface.

You will need to call the wanted action with its arguments.

## Results

Results are outputted using the `as_dict` method from the response models.

Those are the best representation of the different models and classes used throughout translatepy.

The `success` field will be added to them, to indicate that the action successfully ran.

If `success` is `false`, look at [Errors](#errors)

## `translate`

> To translate anything

```swift
🧃❯ translatepy translate -h                            
usage: translatepy translate [-h] --text TEXT --dest-lang DEST_LANG [--source-lang SOURCE_LANG]

optional arguments:
  -h, --help            show this help message and exit
  --text TEXT, -t TEXT  text to translate
  --dest-lang DEST_LANG, -d DEST_LANG
                        destination language
  --source-lang SOURCE_LANG, -s SOURCE_LANG
                        source language
```

### Arguments

- `--text (-t)` is the text you want to translate.
- `--dest-lang (-d)` is the language you want to translate the text in.
- `--source-lang (-s)` is the language you think your text is in. If not provided it will be set to `auto` and will try to detect it.

### Example

```swift
🧃❯ translatepy translate -t "Hello world" -d "japanese"
```

<details>
    <summary>Result</summary>

```json
{
    "success": true,
    "service": "Google",
    "source": "Hello world",
    "result": "こんにちは世界",
    "destinationLanguage": {
        "id": "jpn",
        "name": "Japanese",
        "similarity": 100.00000000000003,
        "alpha2": "ja",
        "alpha3b": "jpn",
        "alpha3t": "jpn",
        "alpha3": "jpn",
        "extra": {
            "type": "Living",
            "scope": "Individual"
        },
        "inForeignLanguages": {
            "af": "Japanese",
            "sq": "Japonez",
            "am": "ጃፓንኛ",
            "ar": "اليابانية",
            "hy": "Ճապոնական",
            "az": "Yapon",
            "eu": "Japanese",
            "be": "Японскі",
            "bn": "জাপানি",
            "bs": "Japanski",
            "bg": "Японски",
            "ca": "Japonès",
            "ceb": "Japanese",
            "ny": "Phokoso",
            "co": "Ghjappunese",
            "hr": "Japanski",
            "cs": "Japonský",
            "da": "Japansk",
            "nl": "Japans",
            "eo": "Japana",
            "et": "Jaapani",
            "tl": "Japanese",
            "fi": "Japanilainen",
            "fr": "Japonais",
            "fy": "Japansk",
            "gl": "Xaponés",
            "ka": "იაპონელი",
            "de": "Japanisch",
            "el": "Ιαπωνικά",
            "gu": "જાપાની",
            "ht": "Japonè",
            "ha": "Japanisanci",
            "haw": "Kepanī",
            "hi": "जापानी",
            "hmn": "Puskawg",
            "hu": "Japán",
            "is": "Japönsku",
            "ig": "Japanese",
            "id": "Jepang",
            "ga": "Seapánach",
            "it": "Giapponese",
            "ja": "日本語",
            "kn": "ಜಪಾನೀಸ್",
            "kk": "Жапон",
            "km": "ជនជាតិជប៉ុន",
            "ko": "일본어",
            "ku": "Japonî",
            "ky": "Жапончо",
            "lo": "ຍີ່ປຸ່ນ",
            "la": "Iaponica",
            "lv": "Japāņu",
            "lt": "Japonų",
            "lb": "Japanesch",
            "mk": "Јапонски",
            "mg": "Anarana",
            "ms": "Jepun",
            "ml": "ജാപ്പനീസ്",
            "mt": "Ġappuniż",
            "mi": "Hapani",
            "mr": "जपानी",
            "mn": "Япон",
            "my": "ဂျပန်",
            "ne": "जापानी",
            "no": "Japansk",
            "or": "ଜାପାନୀ",
            "ps": "جاپاني",
            "fa": "ژاپنی",
            "pl": "Język Japoński",
            "pt": "Japonesa",
            "pa": "ਜਪਾਨੀ",
            "ro": "Japonez",
            "ru": "Японский Язык",
            "sm": "Iapani",
            "gd": "Iapanach",
            "sr": "Јапански",
            "st": "Japanese",
            "sn": "Chijapanese",
            "sd": "جاپاني",
            "si": "ජපන්",
            "sk": "Japonský",
            "sl": "Japonski",
            "so": "Japanese",
            "es": "Japonesa",
            "su": "Jepang",
            "sw": "Kijapani",
            "sv": "Japansk",
            "tg": "Японй",
            "ta": "ஜப்பானிய",
            "te": "Japanese",
            "th": "ญี่ปุ่น",
            "tr": "Japonca",
            "uk": "Японці",
            "ur": "جاپانی",
            "ug": "Japanese",
            "uz": "Yapon",
            "vi": "Tiếng Nhật",
            "cy": "Japan",
            "xh": "Isijaphani",
            "yi": "יאַפּאַניש",
            "yo": "Ede Japan",
            "zu": "Ijaphane",
            "zh": "日本",
            "he": "יַפָּנִית",
            "jv": "Jepang",
            "en": "Japanese"
        }
    },
    "sourceLanguage": {
        "id": "eng",
        "name": "English",
        "similarity": 100,
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "extra": {
            "type": "Living",
            "scope": "Individual"
        },
        "inForeignLanguages": {
            "af": "Engels",
            "sq": "Anglisht",
            "am": "እንግሊዝኛ",
            "ar": "الإنجليزية",
            "hy": "Անգլերեն",
            "az": "Ingilis",
            "eu": "Ingelesez",
            "be": "Англійская",
            "bn": "ইংরেজি",
            "bs": "Engleski",
            "bg": "Английски",
            "ca": "Anglès",
            "ceb": "Iningles",
            "ny": "Chingerezi",
            "co": "Inglese",
            "hr": "Engleski",
            "cs": "Angličtina",
            "da": "Engelsk",
            "nl": "Engels",
            "eo": "Angla",
            "et": "Inglise",
            "tl": "Ingles",
            "fi": "Englanti",
            "fr": "Anglais",
            "fy": "Ingelsk",
            "gl": "Inglés",
            "ka": "ინგლისური",
            "de": "Englisch",
            "el": "Αγγλικά",
            "gu": "અંગ્રેજી",
            "ht": "Anglè",
            "ha": "Turanci",
            "haw": "Pelekania",
            "hi": "अंग्रेज़ी",
            "hmn": "Askiv",
            "hu": "Angol",
            "is": "Enska",
            "ig": "Bekee",
            "id": "Inggris",
            "ga": "Béarla",
            "it": "Inglese",
            "ja": "英語",
            "kn": "ಆಂಗ್ಲ",
            "kk": "Қазақша",
            "km": "ភាសាអង់គ្លេស",
            "ko": "영어",
            "ku": "Îngilîzî",
            "ky": "Англисче",
            "lo": "ອັງກິດ",
            "la": "Anglicus",
            "lv": "Angļu",
            "lt": "Anglų",
            "lb": "Englesch",
            "mk": "Англиски",
            "mg": "Anglisy",
            "ms": "Bahasa Inggeris",
            "ml": "ഇംഗ്ലീഷ്",
            "mt": "Bl-Ingliż",
            "mi": "Ingarihi",
            "mr": "इंग्रजी",
            "mn": "Англи Хэл",
            "my": "အင်္ဂလိပ်",
            "ne": "अंग्रेजी",
            "no": "Engelsk",
            "or": "ଇଂରାଜୀ",
            "ps": "انګلیسي",
            "fa": "انګلیسي...",
            "pl": "Język Angielski",
            "pt": "Inglês",
            "pa": "ਅੰਗਰੇਜ਼ੀ",
            "ro": "Engleză",
            "ru": "Английский",
            "sm": "Igilisi",
            "gd": "Sasannach",
            "sr": "Енглески Језик",
            "st": "English",
            "sn": "Chirungu",
            "sd": "انگريزي",
            "si": "ඉංග්රීසි",
            "sk": "Angličtina",
            "sl": "Angleščina",
            "so": "Ingiriisi",
            "es": "Inglesa",
            "su": "Inggris",
            "sw": "Kiingereza",
            "sv": "Engelsk",
            "tg": "Англисӣ",
            "ta": "ஆங்கிலம்",
            "te": "ఆంగ్ల",
            "th": "อังกฤษ",
            "tr": "Ingilizce",
            "uk": "Англійська",
            "ur": "انگریزی",
            "ug": "English",
            "uz": "Inglizcha",
            "vi": "Tiếng Anh",
            "cy": "Saesneg",
            "xh": "Isingesi",
            "yi": "ענגליש",
            "yo": "Gẹẹsi",
            "zu": "Isingisi",
            "zh": "英语",
            "he": "אנגלית",
            "jv": "Inggris",
            "en": "English"
        }
    }
}
```

</details>
<br>

## `transliterate`

> To transliterate (get the pronunciation) of anything

```swift
🧃❯ translatepy transliterate -h
usage: translatepy transliterate [-h] --text TEXT [--dest-lang DEST_LANG] [--source-lang SOURCE_LANG]

optional arguments:
  -h, --help            show this help message and exit
  --text TEXT, -t TEXT  text to transliterate
  --dest-lang DEST_LANG, -d DEST_LANG
                        destination language
  --source-lang SOURCE_LANG, -s SOURCE_LANG
                        source language
```

### Arguments

- `--text (-t)` is the text you want to transliterate.
- `--dest-lang (-d)` is the language you want to transliterate the text in.
- `--source-lang (-s)` is the language you think your text is in. If not provided it will be set to `auto` and will try to detect it.

### Example

```swift
🧃❯ translatepy transliterate -t "おはようございます" -d "english"
```

<details>
  <summary>Result</summary>
  
```json
{
    "success": true,
    "service": "Google",
    "source": "おはようございます",
    "result": "Ohayōgozaimasu",
    "destinationLanguage": {
        "id": "eng",
        "name": "English",
        "similarity": 99.99999999999999,
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "extra": {
            "type": "Living",
            "scope": "Individual"
        },
        "inForeignLanguages": {
            "af": "Engels",
            "sq": "Anglisht",
            "am": "እንግሊዝኛ",
            "ar": "الإنجليزية",
            "hy": "Անգլերեն",
            "az": "Ingilis",
            "eu": "Ingelesez",
            "be": "Англійская",
            "bn": "ইংরেজি",
            "bs": "Engleski",
            "bg": "Английски",
            "ca": "Anglès",
            "ceb": "Iningles",
            "ny": "Chingerezi",
            "co": "Inglese",
            "hr": "Engleski",
            "cs": "Angličtina",
            "da": "Engelsk",
            "nl": "Engels",
            "eo": "Angla",
            "et": "Inglise",
            "tl": "Ingles",
            "fi": "Englanti",
            "fr": "Anglais",
            "fy": "Ingelsk",
            "gl": "Inglés",
            "ka": "ინგლისური",
            "de": "Englisch",
            "el": "Αγγλικά",
            "gu": "અંગ્રેજી",
            "ht": "Anglè",
            "ha": "Turanci",
            "haw": "Pelekania",
            "hi": "अंग्रेज़ी",
            "hmn": "Askiv",
            "hu": "Angol",
            "is": "Enska",
            "ig": "Bekee",
            "id": "Inggris",
            "ga": "Béarla",
            "it": "Inglese",
            "ja": "英語",
            "kn": "ಆಂಗ್ಲ",
            "kk": "Қазақша",
            "km": "ភាសាអង់គ្លេស",
            "ko": "영어",
            "ku": "Îngilîzî",
            "ky": "Англисче",
            "lo": "ອັງກິດ",
            "la": "Anglicus",
            "lv": "Angļu",
            "lt": "Anglų",
            "lb": "Englesch",
            "mk": "Англиски",
            "mg": "Anglisy",
            "ms": "Bahasa Inggeris",
            "ml": "ഇംഗ്ലീഷ്",
            "mt": "Bl-Ingliż",
            "mi": "Ingarihi",
            "mr": "इंग्रजी",
            "mn": "Англи Хэл",
            "my": "အင်္ဂလိပ်",
            "ne": "अंग्रेजी",
            "no": "Engelsk",
            "or": "ଇଂରାଜୀ",
            "ps": "انګلیسي",
            "fa": "انګلیسي...",
            "pl": "Język Angielski",
            "pt": "Inglês",
            "pa": "ਅੰਗਰੇਜ਼ੀ",
            "ro": "Engleză",
            "ru": "Английский",
            "sm": "Igilisi",
            "gd": "Sasannach",
            "sr": "Енглески Језик",
            "st": "English",
            "sn": "Chirungu",
            "sd": "انگريزي",
            "si": "ඉංග්රීසි",
            "sk": "Angličtina",
            "sl": "Angleščina",
            "so": "Ingiriisi",
            "es": "Inglesa",
            "su": "Inggris",
            "sw": "Kiingereza",
            "sv": "Engelsk",
            "tg": "Англисӣ",
            "ta": "ஆங்கிலம்",
            "te": "ఆంగ్ల",
            "th": "อังกฤษ",
            "tr": "Ingilizce",
            "uk": "Англійська",
            "ur": "انگریزی",
            "ug": "English",
            "uz": "Inglizcha",
            "vi": "Tiếng Anh",
            "cy": "Saesneg",
            "xh": "Isingesi",
            "yi": "ענגליש",
            "yo": "Gẹẹsi",
            "zu": "Isingisi",
            "zh": "英语",
            "he": "אנגלית",
            "jv": "Inggris",
            "en": "English"
        }
    },
    "sourceLanguage": {
        "id": "jpn",
        "name": "Japanese",
        "similarity": 100,
        "alpha2": "ja",
        "alpha3b": "jpn",
        "alpha3t": "jpn",
        "alpha3": "jpn",
        "extra": {
            "type": "Living",
            "scope": "Individual"
        },
        "inForeignLanguages": {
            "af": "Japanese",
            "sq": "Japonez",
            "am": "ጃፓንኛ",
            "ar": "اليابانية",
            "hy": "Ճապոնական",
            "az": "Yapon",
            "eu": "Japanese",
            "be": "Японскі",
            "bn": "জাপানি",
            "bs": "Japanski",
            "bg": "Японски",
            "ca": "Japonès",
            "ceb": "Japanese",
            "ny": "Phokoso",
            "co": "Ghjappunese",
            "hr": "Japanski",
            "cs": "Japonský",
            "da": "Japansk",
            "nl": "Japans",
            "eo": "Japana",
            "et": "Jaapani",
            "tl": "Japanese",
            "fi": "Japanilainen",
            "fr": "Japonais",
            "fy": "Japansk",
            "gl": "Xaponés",
            "ka": "იაპონელი",
            "de": "Japanisch",
            "el": "Ιαπωνικά",
            "gu": "જાપાની",
            "ht": "Japonè",
            "ha": "Japanisanci",
            "haw": "Kepanī",
            "hi": "जापानी",
            "hmn": "Puskawg",
            "hu": "Japán",
            "is": "Japönsku",
            "ig": "Japanese",
            "id": "Jepang",
            "ga": "Seapánach",
            "it": "Giapponese",
            "ja": "日本語",
            "kn": "ಜಪಾನೀಸ್",
            "kk": "Жапон",
            "km": "ជនជាតិជប៉ុន",
            "ko": "일본어",
            "ku": "Japonî",
            "ky": "Жапончо",
            "lo": "ຍີ່ປຸ່ນ",
            "la": "Iaponica",
            "lv": "Japāņu",
            "lt": "Japonų",
            "lb": "Japanesch",
            "mk": "Јапонски",
            "mg": "Anarana",
            "ms": "Jepun",
            "ml": "ജാപ്പനീസ്",
            "mt": "Ġappuniż",
            "mi": "Hapani",
            "mr": "जपानी",
            "mn": "Япон",
            "my": "ဂျပန်",
            "ne": "जापानी",
            "no": "Japansk",
            "or": "ଜାପାନୀ",
            "ps": "جاپاني",
            "fa": "ژاپنی",
            "pl": "Język Japoński",
            "pt": "Japonesa",
            "pa": "ਜਪਾਨੀ",
            "ro": "Japonez",
            "ru": "Японский Язык",
            "sm": "Iapani",
            "gd": "Iapanach",
            "sr": "Јапански",
            "st": "Japanese",
            "sn": "Chijapanese",
            "sd": "جاپاني",
            "si": "ජපන්",
            "sk": "Japonský",
            "sl": "Japonski",
            "so": "Japanese",
            "es": "Japonesa",
            "su": "Jepang",
            "sw": "Kijapani",
            "sv": "Japansk",
            "tg": "Японй",
            "ta": "ஜப்பானிய",
            "te": "Japanese",
            "th": "ญี่ปุ่น",
            "tr": "Japonca",
            "uk": "Японці",
            "ur": "جاپانی",
            "ug": "Japanese",
            "uz": "Yapon",
            "vi": "Tiếng Nhật",
            "cy": "Japan",
            "xh": "Isijaphani",
            "yi": "יאַפּאַניש",
            "yo": "Ede Japan",
            "zu": "Ijaphane",
            "zh": "日本",
            "he": "יַפָּנִית",
            "jv": "Jepang",
            "en": "Japanese"
        }
    }
}
```

</details>

## `spellcheck`

> To spellcheck anything

```swift
🧃❯ translatepy spellcheck -h
usage: translatepy spellcheck [-h] --text TEXT [--source-lang SOURCE_LANG]

optional arguments:
  -h, --help            show this help message and exit
  --text TEXT, -t TEXT  text to spellcheck
  --source-lang SOURCE_LANG, -s SOURCE_LANG
                        source language
```

### Arguments

- `--text (-t)` is the text you want to spellcheck.
- `--source-lang (-s)` is the language you think your text is in. If not provided it will be set to `auto` and will try to detect it.

### Example

```swift
🧃❯ translatepy spellcheck -t "Hw are you ?"
```

<details>
  <summary>Result</summary>

```json
{
    "success": true,
    "service": "Reverso",
    "source": "Hw are you ?",
    "result": "How are you?",
    "sourceLanguage": {
        "id": "eng",
        "name": "English",
        "similarity": 100,
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "extra": {
            "type": "Living",
            "scope": "Individual"
        },
        "inForeignLanguages": {
            "af": "Engels",
            "sq": "Anglisht",
            "am": "እንግሊዝኛ",
            "ar": "الإنجليزية",
            "hy": "Անգլերեն",
            "az": "Ingilis",
            "eu": "Ingelesez",
            "be": "Англійская",
            "bn": "ইংরেজি",
            "bs": "Engleski",
            "bg": "Английски",
            "ca": "Anglès",
            "ceb": "Iningles",
            "ny": "Chingerezi",
            "co": "Inglese",
            "hr": "Engleski",
            "cs": "Angličtina",
            "da": "Engelsk",
            "nl": "Engels",
            "eo": "Angla",
            "et": "Inglise",
            "tl": "Ingles",
            "fi": "Englanti",
            "fr": "Anglais",
            "fy": "Ingelsk",
            "gl": "Inglés",
            "ka": "ინგლისური",
            "de": "Englisch",
            "el": "Αγγλικά",
            "gu": "અંગ્રેજી",
            "ht": "Anglè",
            "ha": "Turanci",
            "haw": "Pelekania",
            "hi": "अंग्रेज़ी",
            "hmn": "Askiv",
            "hu": "Angol",
            "is": "Enska",
            "ig": "Bekee",
            "id": "Inggris",
            "ga": "Béarla",
            "it": "Inglese",
            "ja": "英語",
            "kn": "ಆಂಗ್ಲ",
            "kk": "Қазақша",
            "km": "ភាសាអង់គ្លេស",
            "ko": "영어",
            "ku": "Îngilîzî",
            "ky": "Англисче",
            "lo": "ອັງກິດ",
            "la": "Anglicus",
            "lv": "Angļu",
            "lt": "Anglų",
            "lb": "Englesch",
            "mk": "Англиски",
            "mg": "Anglisy",
            "ms": "Bahasa Inggeris",
            "ml": "ഇംഗ്ലീഷ്",
            "mt": "Bl-Ingliż",
            "mi": "Ingarihi",
            "mr": "इंग्रजी",
            "mn": "Англи Хэл",
            "my": "အင်္ဂလိပ်",
            "ne": "अंग्रेजी",
            "no": "Engelsk",
            "or": "ଇଂରାଜୀ",
            "ps": "انګلیسي",
            "fa": "انګلیسي...",
            "pl": "Język Angielski",
            "pt": "Inglês",
            "pa": "ਅੰਗਰੇਜ਼ੀ",
            "ro": "Engleză",
            "ru": "Английский",
            "sm": "Igilisi",
            "gd": "Sasannach",
            "sr": "Енглески Језик",
            "st": "English",
            "sn": "Chirungu",
            "sd": "انگريزي",
            "si": "ඉංග්රීසි",
            "sk": "Angličtina",
            "sl": "Angleščina",
            "so": "Ingiriisi",
            "es": "Inglesa",
            "su": "Inggris",
            "sw": "Kiingereza",
            "sv": "Engelsk",
            "tg": "Англисӣ",
            "ta": "ஆங்கிலம்",
            "te": "ఆంగ్ల",
            "th": "อังกฤษ",
            "tr": "Ingilizce",
            "uk": "Англійська",
            "ur": "انگریزی",
            "ug": "English",
            "uz": "Inglizcha",
            "vi": "Tiếng Anh",
            "cy": "Saesneg",
            "xh": "Isingesi",
            "yi": "ענגליש",
            "yo": "Gẹẹsi",
            "zu": "Isingisi",
            "zh": "英语",
            "he": "אנגלית",
            "jv": "Inggris",
            "en": "English"
        }
    }
}
```

</details>

## `language`

> To get the language of anything

```swift
🧃❯ translatepy language -h                 
usage: translatepy language [-h] --text TEXT

optional arguments:
  -h, --help            show this help message and exit
  --text TEXT, -t TEXT  text to check the language
```

### Arguments

- `--text (-t)` is the text you want to get the language of.

### Example

```swift
🧃❯ translatepy language -t "おはようございます"
```

<details>
  <summary>Result</summary>

```json
{
    "success": true,
    "service": "Google",
    "source": "おはようございます",
    "result": {
        "id": "jpn",
        "name": "Japanese",
        "similarity": 100,
        "alpha2": "ja",
        "alpha3b": "jpn",
        "alpha3t": "jpn",
        "alpha3": "jpn",
        "extra": {
            "type": "Living",
            "scope": "Individual"
        },
        "inForeignLanguages": {
            "af": "Japanese",
            "sq": "Japonez",
            "am": "ጃፓንኛ",
            "ar": "اليابانية",
            "hy": "Ճապոնական",
            "az": "Yapon",
            "eu": "Japanese",
            "be": "Японскі",
            "bn": "জাপানি",
            "bs": "Japanski",
            "bg": "Японски",
            "ca": "Japonès",
            "ceb": "Japanese",
            "ny": "Phokoso",
            "co": "Ghjappunese",
            "hr": "Japanski",
            "cs": "Japonský",
            "da": "Japansk",
            "nl": "Japans",
            "eo": "Japana",
            "et": "Jaapani",
            "tl": "Japanese",
            "fi": "Japanilainen",
            "fr": "Japonais",
            "fy": "Japansk",
            "gl": "Xaponés",
            "ka": "იაპონელი",
            "de": "Japanisch",
            "el": "Ιαπωνικά",
            "gu": "જાપાની",
            "ht": "Japonè",
            "ha": "Japanisanci",
            "haw": "Kepanī",
            "hi": "जापानी",
            "hmn": "Puskawg",
            "hu": "Japán",
            "is": "Japönsku",
            "ig": "Japanese",
            "id": "Jepang",
            "ga": "Seapánach",
            "it": "Giapponese",
            "ja": "日本語",
            "kn": "ಜಪಾನೀಸ್",
            "kk": "Жапон",
            "km": "ជនជាតិជប៉ុន",
            "ko": "일본어",
            "ku": "Japonî",
            "ky": "Жапончо",
            "lo": "ຍີ່ປຸ່ນ",
            "la": "Iaponica",
            "lv": "Japāņu",
            "lt": "Japonų",
            "lb": "Japanesch",
            "mk": "Јапонски",
            "mg": "Anarana",
            "ms": "Jepun",
            "ml": "ജാപ്പനീസ്",
            "mt": "Ġappuniż",
            "mi": "Hapani",
            "mr": "जपानी",
            "mn": "Япон",
            "my": "ဂျပန်",
            "ne": "जापानी",
            "no": "Japansk",
            "or": "ଜାପାନୀ",
            "ps": "جاپاني",
            "fa": "ژاپنی",
            "pl": "Język Japoński",
            "pt": "Japonesa",
            "pa": "ਜਪਾਨੀ",
            "ro": "Japonez",
            "ru": "Японский Язык",
            "sm": "Iapani",
            "gd": "Iapanach",
            "sr": "Јапански",
            "st": "Japanese",
            "sn": "Chijapanese",
            "sd": "جاپاني",
            "si": "ජපන්",
            "sk": "Japonský",
            "sl": "Japonski",
            "so": "Japanese",
            "es": "Japonesa",
            "su": "Jepang",
            "sw": "Kijapani",
            "sv": "Japansk",
            "tg": "Японй",
            "ta": "ஜப்பானிய",
            "te": "Japanese",
            "th": "ญี่ปุ่น",
            "tr": "Japonca",
            "uk": "Японці",
            "ur": "جاپانی",
            "ug": "Japanese",
            "uz": "Yapon",
            "vi": "Tiếng Nhật",
            "cy": "Japan",
            "xh": "Isijaphani",
            "yi": "יאַפּאַניש",
            "yo": "Ede Japan",
            "zu": "Ijaphane",
            "zh": "日本",
            "he": "יַפָּנִית",
            "jv": "Jepang",
            "en": "Japanese"
        }
    }
}
```

</details>

## Errors

Some errors will also be formatted to be usable.

For example, `UnknownLanguage` errors will have the following format :

```json
🧃❯ translatepy translate -t "hello world" -d "中国"              

{
    "success": false,
    "guessedLanguage": "中国語",
    "similarity": 81.6496580927726,
    "exception": "UnknownLanguage",
    "error": "Couldn't recognize the given language (中国)\nDid you mean: 中国語 (Similarity: 81.65%)?"
}
```

The other errors will have the following format :

```json
{
    "success": false,
    "exception": "<error class>",
    "error": "<error message>"
}
```
