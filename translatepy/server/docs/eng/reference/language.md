# *module* **language**

> [Source: ../../../../language.py @ line 0](../../../../language.py#L0)

Handles the languages management on `translatepy`

## Imports

- [../../../../exceptions.py](../../../../exceptions.py): As `exceptions`

- [../../../../utils/lru.py](../../../../utils/lru.py): As `lru`

- [../../../../utils/vectorize.py](../../../../utils/vectorize.py): As `vectorize`

## *const* **Number**

> [Source: ../../../../language.py @ line 17](../../../../language.py#L17)

Represents a number

## *class* **LanguageExtra**

> [Source: ../../../../language.py @ line 21-34](../../../../language.py#L21-L34)

Extra data given on supported languages

### *attr* LanguageExtra.**scope**

> [Source: ../../../../language.py @ line 23](../../../../language.py#L23)

> Type: `cain.types.Enum`

Language scope

> **Note**
> Can be one of "individual", "macrolanguage", "special"

### *attr* LanguageExtra.**type**

> [Source: ../../../../language.py @ line 28](../../../../language.py#L28)

> Type: `cain.types.Enum`

Language type

> **Note**
> Can be one of "ancient", "constructed", "extinct", "historical", "living", "special"

## *class* **Foreign**

> [Source: ../../../../language.py @ line 37-208](../../../../language.py#L37-L208)

The language name in foreign languages

### *attr* Foreign.**afrikaans**

> [Source: ../../../../language.py @ line 39](../../../../language.py#L39)

> Type: `str`

The language name in afrikaans

### *attr* Foreign.**albanian**

> [Source: ../../../../language.py @ line 41](../../../../language.py#L41)

> Type: `str`

The language name in albanian

### *attr* Foreign.**amharic**

> [Source: ../../../../language.py @ line 43](../../../../language.py#L43)

> Type: `str`

The language name in amharic

### *attr* Foreign.**arabic**

> [Source: ../../../../language.py @ line 45](../../../../language.py#L45)

> Type: `str`

The language name in arabic

### *attr* Foreign.**armenian**

> [Source: ../../../../language.py @ line 47](../../../../language.py#L47)

> Type: `str`

The language name in armenian

### *attr* Foreign.**azerbaijani**

> [Source: ../../../../language.py @ line 49](../../../../language.py#L49)

> Type: `str`

The language name in azerbaijani

### *attr* Foreign.**basque**

> [Source: ../../../../language.py @ line 51](../../../../language.py#L51)

> Type: `str`

The language name in basque

### *attr* Foreign.**belarusian**

> [Source: ../../../../language.py @ line 53](../../../../language.py#L53)

> Type: `str`

The language name in belarusian

### *attr* Foreign.**bengali**

> [Source: ../../../../language.py @ line 55](../../../../language.py#L55)

> Type: `str`

The language name in bengali

### *attr* Foreign.**bosnian**

> [Source: ../../../../language.py @ line 57](../../../../language.py#L57)

> Type: `str`

The language name in bosnian

### *attr* Foreign.**bulgarian**

> [Source: ../../../../language.py @ line 59](../../../../language.py#L59)

> Type: `str`

The language name in bulgarian

### *attr* Foreign.**burmese**

> [Source: ../../../../language.py @ line 61](../../../../language.py#L61)

> Type: `str`

The language name in burmese

### *attr* Foreign.**catalan**

> [Source: ../../../../language.py @ line 63](../../../../language.py#L63)

> Type: `str`

The language name in catalan

### *attr* Foreign.**chinese**

> [Source: ../../../../language.py @ line 65](../../../../language.py#L65)

> Type: `str`

The language name in chinese

### *attr* Foreign.**croatian**

> [Source: ../../../../language.py @ line 67](../../../../language.py#L67)

> Type: `str`

The language name in croatian

### *attr* Foreign.**czech**

> [Source: ../../../../language.py @ line 69](../../../../language.py#L69)

> Type: `str`

The language name in czech

### *attr* Foreign.**danish**

> [Source: ../../../../language.py @ line 71](../../../../language.py#L71)

> Type: `str`

The language name in danish

### *attr* Foreign.**dutch**

> [Source: ../../../../language.py @ line 73](../../../../language.py#L73)

> Type: `str`

The language name in dutch

### *attr* Foreign.**esperanto**

> [Source: ../../../../language.py @ line 75](../../../../language.py#L75)

> Type: `str`

The language name in esperanto

### *attr* Foreign.**estonian**

> [Source: ../../../../language.py @ line 77](../../../../language.py#L77)

> Type: `str`

The language name in estonian

### *attr* Foreign.**finnish**

> [Source: ../../../../language.py @ line 79](../../../../language.py#L79)

> Type: `str`

The language name in finnish

### *attr* Foreign.**french**

> [Source: ../../../../language.py @ line 81](../../../../language.py#L81)

> Type: `str`

The language name in french

### *attr* Foreign.**galician**

> [Source: ../../../../language.py @ line 83](../../../../language.py#L83)

> Type: `str`

The language name in galician

### *attr* Foreign.**georgian**

> [Source: ../../../../language.py @ line 85](../../../../language.py#L85)

> Type: `str`

The language name in georgian

### *attr* Foreign.**german**

> [Source: ../../../../language.py @ line 87](../../../../language.py#L87)

> Type: `str`

The language name in german

### *attr* Foreign.**gujarati**

> [Source: ../../../../language.py @ line 89](../../../../language.py#L89)

> Type: `str`

The language name in gujarati

### *attr* Foreign.**haitian**

> [Source: ../../../../language.py @ line 91](../../../../language.py#L91)

> Type: `str`

The language name in haitian

### *attr* Foreign.**hebrew**

> [Source: ../../../../language.py @ line 93](../../../../language.py#L93)

> Type: `str`

The language name in hebrew

### *attr* Foreign.**hindi**

> [Source: ../../../../language.py @ line 95](../../../../language.py#L95)

> Type: `str`

The language name in hindi

### *attr* Foreign.**hungarian**

> [Source: ../../../../language.py @ line 97](../../../../language.py#L97)

> Type: `str`

The language name in hungarian

### *attr* Foreign.**icelandic**

> [Source: ../../../../language.py @ line 99](../../../../language.py#L99)

> Type: `str`

The language name in icelandic

### *attr* Foreign.**indonesian**

> [Source: ../../../../language.py @ line 101](../../../../language.py#L101)

> Type: `str`

The language name in indonesian

### *attr* Foreign.**irish**

> [Source: ../../../../language.py @ line 103](../../../../language.py#L103)

> Type: `str`

The language name in irish

### *attr* Foreign.**italian**

> [Source: ../../../../language.py @ line 105](../../../../language.py#L105)

> Type: `str`

The language name in italian

### *attr* Foreign.**japanese**

> [Source: ../../../../language.py @ line 107](../../../../language.py#L107)

> Type: `str`

The language name in japanese

### *attr* Foreign.**javanese**

> [Source: ../../../../language.py @ line 109](../../../../language.py#L109)

> Type: `str`

The language name in javanese

### *attr* Foreign.**kannada**

> [Source: ../../../../language.py @ line 111](../../../../language.py#L111)

> Type: `str`

The language name in kannada

### *attr* Foreign.**kazakh**

> [Source: ../../../../language.py @ line 113](../../../../language.py#L113)

> Type: `str`

The language name in kazakh

### *attr* Foreign.**khmer**

> [Source: ../../../../language.py @ line 115](../../../../language.py#L115)

> Type: `str`

The language name in khmer

### *attr* Foreign.**kirghiz**

> [Source: ../../../../language.py @ line 117](../../../../language.py#L117)

> Type: `str`

The language name in kirghiz

### *attr* Foreign.**korean**

> [Source: ../../../../language.py @ line 119](../../../../language.py#L119)

> Type: `str`

The language name in korean

### *attr* Foreign.**lao**

> [Source: ../../../../language.py @ line 121](../../../../language.py#L121)

> Type: `str`

The language name in lao

### *attr* Foreign.**latin**

> [Source: ../../../../language.py @ line 123](../../../../language.py#L123)

> Type: `str`

The language name in latin

### *attr* Foreign.**latvian**

> [Source: ../../../../language.py @ line 125](../../../../language.py#L125)

> Type: `str`

The language name in latvian

### *attr* Foreign.**lithuanian**

> [Source: ../../../../language.py @ line 127](../../../../language.py#L127)

> Type: `str`

The language name in lithuanian

### *attr* Foreign.**luxembourgish**

> [Source: ../../../../language.py @ line 129](../../../../language.py#L129)

> Type: `str`

The language name in luxembourgish

### *attr* Foreign.**macedonian**

> [Source: ../../../../language.py @ line 131](../../../../language.py#L131)

> Type: `str`

The language name in macedonian

### *attr* Foreign.**malagasy**

> [Source: ../../../../language.py @ line 133](../../../../language.py#L133)

> Type: `str`

The language name in malagasy

### *attr* Foreign.**malay**

> [Source: ../../../../language.py @ line 135](../../../../language.py#L135)

> Type: `str`

The language name in malay

### *attr* Foreign.**maltese**

> [Source: ../../../../language.py @ line 137](../../../../language.py#L137)

> Type: `str`

The language name in maltese

### *attr* Foreign.**maori**

> [Source: ../../../../language.py @ line 139](../../../../language.py#L139)

> Type: `str`

The language name in maori

### *attr* Foreign.**marathi**

> [Source: ../../../../language.py @ line 141](../../../../language.py#L141)

> Type: `str`

The language name in marathi

### *attr* Foreign.**moderngreek**

> [Source: ../../../../language.py @ line 143](../../../../language.py#L143)

> Type: `str`

The language name in moderngreek

### *attr* Foreign.**mongolian**

> [Source: ../../../../language.py @ line 145](../../../../language.py#L145)

> Type: `str`

The language name in mongolian

### *attr* Foreign.**nepali**

> [Source: ../../../../language.py @ line 147](../../../../language.py#L147)

> Type: `str`

The language name in nepali

### *attr* Foreign.**norwegian**

> [Source: ../../../../language.py @ line 149](../../../../language.py#L149)

> Type: `str`

The language name in norwegian

### *attr* Foreign.**panjabi**

> [Source: ../../../../language.py @ line 151](../../../../language.py#L151)

> Type: `str`

The language name in panjabi

### *attr* Foreign.**persian**

> [Source: ../../../../language.py @ line 153](../../../../language.py#L153)

> Type: `str`

The language name in persian

### *attr* Foreign.**polish**

> [Source: ../../../../language.py @ line 155](../../../../language.py#L155)

> Type: `str`

The language name in polish

### *attr* Foreign.**portuguese**

> [Source: ../../../../language.py @ line 157](../../../../language.py#L157)

> Type: `str`

The language name in portuguese

### *attr* Foreign.**romanian**

> [Source: ../../../../language.py @ line 159](../../../../language.py#L159)

> Type: `str`

The language name in romanian

### *attr* Foreign.**russian**

> [Source: ../../../../language.py @ line 161](../../../../language.py#L161)

> Type: `str`

The language name in russian

### *attr* Foreign.**scottishgaelic**

> [Source: ../../../../language.py @ line 163](../../../../language.py#L163)

> Type: `str`

The language name in scottishgaelic

### *attr* Foreign.**serbian**

> [Source: ../../../../language.py @ line 165](../../../../language.py#L165)

> Type: `str`

The language name in serbian

### *attr* Foreign.**sinhala**

> [Source: ../../../../language.py @ line 167](../../../../language.py#L167)

> Type: `str`

The language name in sinhala

### *attr* Foreign.**slovak**

> [Source: ../../../../language.py @ line 169](../../../../language.py#L169)

> Type: `str`

The language name in slovak

### *attr* Foreign.**slovenian**

> [Source: ../../../../language.py @ line 171](../../../../language.py#L171)

> Type: `str`

The language name in slovenian

### *attr* Foreign.**spanish**

> [Source: ../../../../language.py @ line 173](../../../../language.py#L173)

> Type: `str`

The language name in spanish

### *attr* Foreign.**sundanese**

> [Source: ../../../../language.py @ line 175](../../../../language.py#L175)

> Type: `str`

The language name in sundanese

### *attr* Foreign.**swahili**

> [Source: ../../../../language.py @ line 177](../../../../language.py#L177)

> Type: `str`

The language name in swahili

### *attr* Foreign.**swedish**

> [Source: ../../../../language.py @ line 179](../../../../language.py#L179)

> Type: `str`

The language name in swedish

### *attr* Foreign.**tagalog**

> [Source: ../../../../language.py @ line 181](../../../../language.py#L181)

> Type: `str`

The language name in tagalog

### *attr* Foreign.**tajik**

> [Source: ../../../../language.py @ line 183](../../../../language.py#L183)

> Type: `str`

The language name in tajik

### *attr* Foreign.**tamil**

> [Source: ../../../../language.py @ line 185](../../../../language.py#L185)

> Type: `str`

The language name in tamil

### *attr* Foreign.**telugu**

> [Source: ../../../../language.py @ line 187](../../../../language.py#L187)

> Type: `str`

The language name in telugu

### *attr* Foreign.**thai**

> [Source: ../../../../language.py @ line 189](../../../../language.py#L189)

> Type: `str`

The language name in thai

### *attr* Foreign.**turkish**

> [Source: ../../../../language.py @ line 191](../../../../language.py#L191)

> Type: `str`

The language name in turkish

### *attr* Foreign.**ukrainian**

> [Source: ../../../../language.py @ line 193](../../../../language.py#L193)

> Type: `str`

The language name in ukrainian

### *attr* Foreign.**urdu**

> [Source: ../../../../language.py @ line 195](../../../../language.py#L195)

> Type: `str`

The language name in urdu

### *attr* Foreign.**uzbek**

> [Source: ../../../../language.py @ line 197](../../../../language.py#L197)

> Type: `str`

The language name in uzbek

### *attr* Foreign.**vietnamese**

> [Source: ../../../../language.py @ line 199](../../../../language.py#L199)

> Type: `str`

The language name in vietnamese

### *attr* Foreign.**welsh**

> [Source: ../../../../language.py @ line 201](../../../../language.py#L201)

> Type: `str`

The language name in welsh

### *attr* Foreign.**xhosa**

> [Source: ../../../../language.py @ line 203](../../../../language.py#L203)

> Type: `str`

The language name in xhosa

### *attr* Foreign.**yiddish**

> [Source: ../../../../language.py @ line 205](../../../../language.py#L205)

> Type: `str`

The language name in yiddish

### *attr* Foreign.**zulu**

> [Source: ../../../../language.py @ line 207](../../../../language.py#L207)

> Type: `str`

The language name in zulu

## *const* **LANGUAGE_CACHE**

> [Source: ../../../../language.py @ line 211](../../../../language.py#L211)

## *const* **NULLABLE_ATTRIBUTES**

> [Source: ../../../../language.py @ line 212](../../../../language.py#L212)

## *class* **Language**

> [Source: ../../../../language.py @ line 215-347](../../../../language.py#L215-L347)

A language

### *attr* Language.**id**

> [Source: ../../../../language.py @ line 218](../../../../language.py#L218)

> Type: `str`

The language identifier

### *attr* Language.**alpha3**

> [Source: ../../../../language.py @ line 220](../../../../language.py#L220)

> Type: `str`

The ISO 639-3 (Alpha-3) code

### *attr* Language.**name**

> [Source: ../../../../language.py @ line 222](../../../../language.py#L222)

> Type: `str`

The english name

### *attr* Language.**alpha2**

> [Source: ../../../../language.py @ line 224](../../../../language.py#L224)

> Type: `Optional`

The ISO 639-1 (Alpha-2) code, if available

### *attr* Language.**alpha3b**

> [Source: ../../../../language.py @ line 226](../../../../language.py#L226)

> Type: `Optional`

The ISO 639-2B (Alpha-3) code, if available

### *attr* Language.**alpha3t**

> [Source: ../../../../language.py @ line 228](../../../../language.py#L228)

> Type: `Optional`

The ISO 639-2T (Alpha-3) code, if available

### *attr* Language.**extra**

> [Source: ../../../../language.py @ line 230](../../../../language.py#L230)

> Type: `Optional`

Extra data for the language, if available

### *attr* Language.**foreign**

> [Source: ../../../../language.py @ line 232](../../../../language.py#L232)

> Type: `Optional`

Name in foreign languages, if available

### *func* Language.**search**

> [Source: ../../../../language.py @ line 269-292](../../../../language.py#L269-L292)

Searches the given language

#### Parameters

- **cls**


- **query**: `str`


#### Returns

- `list`

### *func* Language.**get_extra**

> [Source: ../../../../language.py @ line 310-317](../../../../language.py#L310-L317)

Retrieves the given attribute from `extra` if available

#### Parameters

- **attribute**: `str`


#### Returns

- `NoneType`

- `str`

### *func* Language.**get_foreign**

> [Source: ../../../../language.py @ line 319-328](../../../../language.py#L319-L328)

Retrieves the given attribute from `foreign` if available

#### Parameters

- **attribute**: `ForwardRef('Language')`, `str`


#### Returns

- `NoneType`

- `str`

### *property* Language.**similarity**

> [Source: ../../../../language.py @ line 331-333](../../../../language.py#L331-L333)

The similarity with the vector while searching the language

#### Returns

- `float`

### *property* Language.**native**

> [Source: ../../../../language.py @ line 336-338](../../../../language.py#L336-L338)

The native name for the language or its english name

#### Returns

- `str`

### *property* Language.**rich**

> [Source: ../../../../language.py @ line 341-347](../../../../language.py#L341-L347)

If the language discovery used the full translatepy dataset  
Note: This returns `False` if the `Language` was not fully initialized

#### Returns

- `bool`

## *class* **LanguageData**

> [Source: ../../../../language.py @ line 352-356](../../../../language.py#L352-L356)

Groups all of the data

### *attr* LanguageData.**codes**

> [Source: ../../../../language.py @ line 354](../../../../language.py#L354)

> Type: `Dict`

### *attr* LanguageData.**data**

> [Source: ../../../../language.py @ line 355](../../../../language.py#L355)

> Type: `Dict`

### *attr* LanguageData.**vectors**

> [Source: ../../../../language.py @ line 356](../../../../language.py#L356)

> Type: `List`

## *const* **LANGUAGE_DATA_DIR**

> [Source: ../../../../language.py @ line 360](../../../../language.py#L360)

The directory where all of the data is stored

## *const* **DATA**

> [Source: ../../../../language.py @ line 363](../../../../language.py#L363)

The languages in-memory data

## *const* **TRANSLATEPY_LANGUAGE_FULL**

> [Source: ../../../../language.py @ line 369](../../../../language.py#L369)

If the full language data database got loaded at runtime

## *func* **load_full**

> [Source: ../../../../language.py @ line 378-385](../../../../language.py#L378-L385)

Loads the full data languages DB

## *const* **COMMON_LANGUAGES**

> [Source: ../../../../language.py @ line 392](../../../../language.py#L392)

All of the available foreign languages for the `foreign` field on the `Language` class and English
