# *module* **language**

> [Source: ../../../translatepy/language.py @ line 0](../../../translatepy/language.py#L0)

Handles the languages management on `translatepy`

## Imports

- [../../../translatepy/exceptions.py](../../../translatepy/exceptions.py): As `exceptions`

- [../../../translatepy/utils/lru.py](../../../translatepy/utils/lru.py): As `lru`

- [../../../translatepy/utils/vectorize.py](../../../translatepy/utils/vectorize.py): As `vectorize`

## *const* **Number**

> [Source: ../../../translatepy/language.py @ line 17](../../../translatepy/language.py#L17)

Represents a number

## *class* **LanguageExtra**

> [Source: ../../../translatepy/language.py @ line 21-34](../../../translatepy/language.py#L21-L34)

Extra data given on supported languages

### *attr* LanguageExtra.**scope**

> [Source: ../../../translatepy/language.py @ line 23](../../../translatepy/language.py#L23)

> Type: `cain.types.Enum`

Language scope

> **Note**
> Can be one of "individual", "macrolanguage", "special"

### *attr* LanguageExtra.**type**

> [Source: ../../../translatepy/language.py @ line 28](../../../translatepy/language.py#L28)

> Type: `cain.types.Enum`

Language type

> **Note**
> Can be one of "ancient", "constructed", "extinct", "historical", "living", "special"

## *class* **Foreign**

> [Source: ../../../translatepy/language.py @ line 37-208](../../../translatepy/language.py#L37-L208)

The language name in foreign languages

### *attr* Foreign.**afrikaans**

> [Source: ../../../translatepy/language.py @ line 39](../../../translatepy/language.py#L39)

> Type: `str`

The language name in afrikaans

### *attr* Foreign.**albanian**

> [Source: ../../../translatepy/language.py @ line 41](../../../translatepy/language.py#L41)

> Type: `str`

The language name in albanian

### *attr* Foreign.**amharic**

> [Source: ../../../translatepy/language.py @ line 43](../../../translatepy/language.py#L43)

> Type: `str`

The language name in amharic

### *attr* Foreign.**arabic**

> [Source: ../../../translatepy/language.py @ line 45](../../../translatepy/language.py#L45)

> Type: `str`

The language name in arabic

### *attr* Foreign.**armenian**

> [Source: ../../../translatepy/language.py @ line 47](../../../translatepy/language.py#L47)

> Type: `str`

The language name in armenian

### *attr* Foreign.**azerbaijani**

> [Source: ../../../translatepy/language.py @ line 49](../../../translatepy/language.py#L49)

> Type: `str`

The language name in azerbaijani

### *attr* Foreign.**basque**

> [Source: ../../../translatepy/language.py @ line 51](../../../translatepy/language.py#L51)

> Type: `str`

The language name in basque

### *attr* Foreign.**belarusian**

> [Source: ../../../translatepy/language.py @ line 53](../../../translatepy/language.py#L53)

> Type: `str`

The language name in belarusian

### *attr* Foreign.**bengali**

> [Source: ../../../translatepy/language.py @ line 55](../../../translatepy/language.py#L55)

> Type: `str`

The language name in bengali

### *attr* Foreign.**bosnian**

> [Source: ../../../translatepy/language.py @ line 57](../../../translatepy/language.py#L57)

> Type: `str`

The language name in bosnian

### *attr* Foreign.**bulgarian**

> [Source: ../../../translatepy/language.py @ line 59](../../../translatepy/language.py#L59)

> Type: `str`

The language name in bulgarian

### *attr* Foreign.**burmese**

> [Source: ../../../translatepy/language.py @ line 61](../../../translatepy/language.py#L61)

> Type: `str`

The language name in burmese

### *attr* Foreign.**catalan**

> [Source: ../../../translatepy/language.py @ line 63](../../../translatepy/language.py#L63)

> Type: `str`

The language name in catalan

### *attr* Foreign.**chinese**

> [Source: ../../../translatepy/language.py @ line 65](../../../translatepy/language.py#L65)

> Type: `str`

The language name in chinese

### *attr* Foreign.**croatian**

> [Source: ../../../translatepy/language.py @ line 67](../../../translatepy/language.py#L67)

> Type: `str`

The language name in croatian

### *attr* Foreign.**czech**

> [Source: ../../../translatepy/language.py @ line 69](../../../translatepy/language.py#L69)

> Type: `str`

The language name in czech

### *attr* Foreign.**danish**

> [Source: ../../../translatepy/language.py @ line 71](../../../translatepy/language.py#L71)

> Type: `str`

The language name in danish

### *attr* Foreign.**dutch**

> [Source: ../../../translatepy/language.py @ line 73](../../../translatepy/language.py#L73)

> Type: `str`

The language name in dutch

### *attr* Foreign.**esperanto**

> [Source: ../../../translatepy/language.py @ line 75](../../../translatepy/language.py#L75)

> Type: `str`

The language name in esperanto

### *attr* Foreign.**estonian**

> [Source: ../../../translatepy/language.py @ line 77](../../../translatepy/language.py#L77)

> Type: `str`

The language name in estonian

### *attr* Foreign.**finnish**

> [Source: ../../../translatepy/language.py @ line 79](../../../translatepy/language.py#L79)

> Type: `str`

The language name in finnish

### *attr* Foreign.**french**

> [Source: ../../../translatepy/language.py @ line 81](../../../translatepy/language.py#L81)

> Type: `str`

The language name in french

### *attr* Foreign.**galician**

> [Source: ../../../translatepy/language.py @ line 83](../../../translatepy/language.py#L83)

> Type: `str`

The language name in galician

### *attr* Foreign.**georgian**

> [Source: ../../../translatepy/language.py @ line 85](../../../translatepy/language.py#L85)

> Type: `str`

The language name in georgian

### *attr* Foreign.**german**

> [Source: ../../../translatepy/language.py @ line 87](../../../translatepy/language.py#L87)

> Type: `str`

The language name in german

### *attr* Foreign.**gujarati**

> [Source: ../../../translatepy/language.py @ line 89](../../../translatepy/language.py#L89)

> Type: `str`

The language name in gujarati

### *attr* Foreign.**haitian**

> [Source: ../../../translatepy/language.py @ line 91](../../../translatepy/language.py#L91)

> Type: `str`

The language name in haitian

### *attr* Foreign.**hebrew**

> [Source: ../../../translatepy/language.py @ line 93](../../../translatepy/language.py#L93)

> Type: `str`

The language name in hebrew

### *attr* Foreign.**hindi**

> [Source: ../../../translatepy/language.py @ line 95](../../../translatepy/language.py#L95)

> Type: `str`

The language name in hindi

### *attr* Foreign.**hungarian**

> [Source: ../../../translatepy/language.py @ line 97](../../../translatepy/language.py#L97)

> Type: `str`

The language name in hungarian

### *attr* Foreign.**icelandic**

> [Source: ../../../translatepy/language.py @ line 99](../../../translatepy/language.py#L99)

> Type: `str`

The language name in icelandic

### *attr* Foreign.**indonesian**

> [Source: ../../../translatepy/language.py @ line 101](../../../translatepy/language.py#L101)

> Type: `str`

The language name in indonesian

### *attr* Foreign.**irish**

> [Source: ../../../translatepy/language.py @ line 103](../../../translatepy/language.py#L103)

> Type: `str`

The language name in irish

### *attr* Foreign.**italian**

> [Source: ../../../translatepy/language.py @ line 105](../../../translatepy/language.py#L105)

> Type: `str`

The language name in italian

### *attr* Foreign.**japanese**

> [Source: ../../../translatepy/language.py @ line 107](../../../translatepy/language.py#L107)

> Type: `str`

The language name in japanese

### *attr* Foreign.**javanese**

> [Source: ../../../translatepy/language.py @ line 109](../../../translatepy/language.py#L109)

> Type: `str`

The language name in javanese

### *attr* Foreign.**kannada**

> [Source: ../../../translatepy/language.py @ line 111](../../../translatepy/language.py#L111)

> Type: `str`

The language name in kannada

### *attr* Foreign.**kazakh**

> [Source: ../../../translatepy/language.py @ line 113](../../../translatepy/language.py#L113)

> Type: `str`

The language name in kazakh

### *attr* Foreign.**khmer**

> [Source: ../../../translatepy/language.py @ line 115](../../../translatepy/language.py#L115)

> Type: `str`

The language name in khmer

### *attr* Foreign.**kirghiz**

> [Source: ../../../translatepy/language.py @ line 117](../../../translatepy/language.py#L117)

> Type: `str`

The language name in kirghiz

### *attr* Foreign.**korean**

> [Source: ../../../translatepy/language.py @ line 119](../../../translatepy/language.py#L119)

> Type: `str`

The language name in korean

### *attr* Foreign.**lao**

> [Source: ../../../translatepy/language.py @ line 121](../../../translatepy/language.py#L121)

> Type: `str`

The language name in lao

### *attr* Foreign.**latin**

> [Source: ../../../translatepy/language.py @ line 123](../../../translatepy/language.py#L123)

> Type: `str`

The language name in latin

### *attr* Foreign.**latvian**

> [Source: ../../../translatepy/language.py @ line 125](../../../translatepy/language.py#L125)

> Type: `str`

The language name in latvian

### *attr* Foreign.**lithuanian**

> [Source: ../../../translatepy/language.py @ line 127](../../../translatepy/language.py#L127)

> Type: `str`

The language name in lithuanian

### *attr* Foreign.**luxembourgish**

> [Source: ../../../translatepy/language.py @ line 129](../../../translatepy/language.py#L129)

> Type: `str`

The language name in luxembourgish

### *attr* Foreign.**macedonian**

> [Source: ../../../translatepy/language.py @ line 131](../../../translatepy/language.py#L131)

> Type: `str`

The language name in macedonian

### *attr* Foreign.**malagasy**

> [Source: ../../../translatepy/language.py @ line 133](../../../translatepy/language.py#L133)

> Type: `str`

The language name in malagasy

### *attr* Foreign.**malay**

> [Source: ../../../translatepy/language.py @ line 135](../../../translatepy/language.py#L135)

> Type: `str`

The language name in malay

### *attr* Foreign.**maltese**

> [Source: ../../../translatepy/language.py @ line 137](../../../translatepy/language.py#L137)

> Type: `str`

The language name in maltese

### *attr* Foreign.**maori**

> [Source: ../../../translatepy/language.py @ line 139](../../../translatepy/language.py#L139)

> Type: `str`

The language name in maori

### *attr* Foreign.**marathi**

> [Source: ../../../translatepy/language.py @ line 141](../../../translatepy/language.py#L141)

> Type: `str`

The language name in marathi

### *attr* Foreign.**moderngreek**

> [Source: ../../../translatepy/language.py @ line 143](../../../translatepy/language.py#L143)

> Type: `str`

The language name in moderngreek

### *attr* Foreign.**mongolian**

> [Source: ../../../translatepy/language.py @ line 145](../../../translatepy/language.py#L145)

> Type: `str`

The language name in mongolian

### *attr* Foreign.**nepali**

> [Source: ../../../translatepy/language.py @ line 147](../../../translatepy/language.py#L147)

> Type: `str`

The language name in nepali

### *attr* Foreign.**norwegian**

> [Source: ../../../translatepy/language.py @ line 149](../../../translatepy/language.py#L149)

> Type: `str`

The language name in norwegian

### *attr* Foreign.**panjabi**

> [Source: ../../../translatepy/language.py @ line 151](../../../translatepy/language.py#L151)

> Type: `str`

The language name in panjabi

### *attr* Foreign.**persian**

> [Source: ../../../translatepy/language.py @ line 153](../../../translatepy/language.py#L153)

> Type: `str`

The language name in persian

### *attr* Foreign.**polish**

> [Source: ../../../translatepy/language.py @ line 155](../../../translatepy/language.py#L155)

> Type: `str`

The language name in polish

### *attr* Foreign.**portuguese**

> [Source: ../../../translatepy/language.py @ line 157](../../../translatepy/language.py#L157)

> Type: `str`

The language name in portuguese

### *attr* Foreign.**romanian**

> [Source: ../../../translatepy/language.py @ line 159](../../../translatepy/language.py#L159)

> Type: `str`

The language name in romanian

### *attr* Foreign.**russian**

> [Source: ../../../translatepy/language.py @ line 161](../../../translatepy/language.py#L161)

> Type: `str`

The language name in russian

### *attr* Foreign.**scottishgaelic**

> [Source: ../../../translatepy/language.py @ line 163](../../../translatepy/language.py#L163)

> Type: `str`

The language name in scottishgaelic

### *attr* Foreign.**serbian**

> [Source: ../../../translatepy/language.py @ line 165](../../../translatepy/language.py#L165)

> Type: `str`

The language name in serbian

### *attr* Foreign.**sinhala**

> [Source: ../../../translatepy/language.py @ line 167](../../../translatepy/language.py#L167)

> Type: `str`

The language name in sinhala

### *attr* Foreign.**slovak**

> [Source: ../../../translatepy/language.py @ line 169](../../../translatepy/language.py#L169)

> Type: `str`

The language name in slovak

### *attr* Foreign.**slovenian**

> [Source: ../../../translatepy/language.py @ line 171](../../../translatepy/language.py#L171)

> Type: `str`

The language name in slovenian

### *attr* Foreign.**spanish**

> [Source: ../../../translatepy/language.py @ line 173](../../../translatepy/language.py#L173)

> Type: `str`

The language name in spanish

### *attr* Foreign.**sundanese**

> [Source: ../../../translatepy/language.py @ line 175](../../../translatepy/language.py#L175)

> Type: `str`

The language name in sundanese

### *attr* Foreign.**swahili**

> [Source: ../../../translatepy/language.py @ line 177](../../../translatepy/language.py#L177)

> Type: `str`

The language name in swahili

### *attr* Foreign.**swedish**

> [Source: ../../../translatepy/language.py @ line 179](../../../translatepy/language.py#L179)

> Type: `str`

The language name in swedish

### *attr* Foreign.**tagalog**

> [Source: ../../../translatepy/language.py @ line 181](../../../translatepy/language.py#L181)

> Type: `str`

The language name in tagalog

### *attr* Foreign.**tajik**

> [Source: ../../../translatepy/language.py @ line 183](../../../translatepy/language.py#L183)

> Type: `str`

The language name in tajik

### *attr* Foreign.**tamil**

> [Source: ../../../translatepy/language.py @ line 185](../../../translatepy/language.py#L185)

> Type: `str`

The language name in tamil

### *attr* Foreign.**telugu**

> [Source: ../../../translatepy/language.py @ line 187](../../../translatepy/language.py#L187)

> Type: `str`

The language name in telugu

### *attr* Foreign.**thai**

> [Source: ../../../translatepy/language.py @ line 189](../../../translatepy/language.py#L189)

> Type: `str`

The language name in thai

### *attr* Foreign.**turkish**

> [Source: ../../../translatepy/language.py @ line 191](../../../translatepy/language.py#L191)

> Type: `str`

The language name in turkish

### *attr* Foreign.**ukrainian**

> [Source: ../../../translatepy/language.py @ line 193](../../../translatepy/language.py#L193)

> Type: `str`

The language name in ukrainian

### *attr* Foreign.**urdu**

> [Source: ../../../translatepy/language.py @ line 195](../../../translatepy/language.py#L195)

> Type: `str`

The language name in urdu

### *attr* Foreign.**uzbek**

> [Source: ../../../translatepy/language.py @ line 197](../../../translatepy/language.py#L197)

> Type: `str`

The language name in uzbek

### *attr* Foreign.**vietnamese**

> [Source: ../../../translatepy/language.py @ line 199](../../../translatepy/language.py#L199)

> Type: `str`

The language name in vietnamese

### *attr* Foreign.**welsh**

> [Source: ../../../translatepy/language.py @ line 201](../../../translatepy/language.py#L201)

> Type: `str`

The language name in welsh

### *attr* Foreign.**xhosa**

> [Source: ../../../translatepy/language.py @ line 203](../../../translatepy/language.py#L203)

> Type: `str`

The language name in xhosa

### *attr* Foreign.**yiddish**

> [Source: ../../../translatepy/language.py @ line 205](../../../translatepy/language.py#L205)

> Type: `str`

The language name in yiddish

### *attr* Foreign.**zulu**

> [Source: ../../../translatepy/language.py @ line 207](../../../translatepy/language.py#L207)

> Type: `str`

The language name in zulu

## *const* **LANGUAGE_CACHE**

> [Source: ../../../translatepy/language.py @ line 211](../../../translatepy/language.py#L211)

## *const* **NULLABLE_ATTRIBUTES**

> [Source: ../../../translatepy/language.py @ line 212](../../../translatepy/language.py#L212)

## *class* **Language**

> [Source: ../../../translatepy/language.py @ line 215-347](../../../translatepy/language.py#L215-L347)

A language

### *attr* Language.**id**

> [Source: ../../../translatepy/language.py @ line 218](../../../translatepy/language.py#L218)

> Type: `str`

The language identifier

### *attr* Language.**alpha3**

> [Source: ../../../translatepy/language.py @ line 220](../../../translatepy/language.py#L220)

> Type: `str`

The ISO 639-3 (Alpha-3) code

### *attr* Language.**name**

> [Source: ../../../translatepy/language.py @ line 222](../../../translatepy/language.py#L222)

> Type: `str`

The english name

### *attr* Language.**alpha2**

> [Source: ../../../translatepy/language.py @ line 224](../../../translatepy/language.py#L224)

> Type: `Optional`

The ISO 639-1 (Alpha-2) code, if available

### *attr* Language.**alpha3b**

> [Source: ../../../translatepy/language.py @ line 226](../../../translatepy/language.py#L226)

> Type: `Optional`

The ISO 639-2B (Alpha-3) code, if available

### *attr* Language.**alpha3t**

> [Source: ../../../translatepy/language.py @ line 228](../../../translatepy/language.py#L228)

> Type: `Optional`

The ISO 639-2T (Alpha-3) code, if available

### *attr* Language.**extra**

> [Source: ../../../translatepy/language.py @ line 230](../../../translatepy/language.py#L230)

> Type: `Optional`

Extra data for the language, if available

### *attr* Language.**foreign**

> [Source: ../../../translatepy/language.py @ line 232](../../../translatepy/language.py#L232)

> Type: `Optional`

Name in foreign languages, if available

### *func* Language.**search**

> [Source: ../../../translatepy/language.py @ line 269-292](../../../translatepy/language.py#L269-L292)

Searches the given language

#### Parameters

- **cls**


- **query**: `str`


#### Returns

- `list`

### *func* Language.**get_extra**

> [Source: ../../../translatepy/language.py @ line 310-317](../../../translatepy/language.py#L310-L317)

Retrieves the given attribute from `extra` if available

#### Parameters

- **attribute**: `str`


#### Returns

- `NoneType`

- `str`

### *func* Language.**get_foreign**

> [Source: ../../../translatepy/language.py @ line 319-328](../../../translatepy/language.py#L319-L328)

Retrieves the given attribute from `foreign` if available

#### Parameters

- **attribute**: `ForwardRef('Language')`, `str`


#### Returns

- `NoneType`

- `str`

### *property* Language.**similarity**

> [Source: ../../../translatepy/language.py @ line 331-333](../../../translatepy/language.py#L331-L333)

The similarity with the vector while searching the language

#### Returns

- `float`

### *property* Language.**native**

> [Source: ../../../translatepy/language.py @ line 336-338](../../../translatepy/language.py#L336-L338)

The native name for the language or its english name

#### Returns

- `str`

### *property* Language.**rich**

> [Source: ../../../translatepy/language.py @ line 341-347](../../../translatepy/language.py#L341-L347)

If the language discovery used the full translatepy dataset  
Note: This returns `False` if the `Language` was not fully initialized

#### Returns

- `bool`

## *class* **LanguageData**

> [Source: ../../../translatepy/language.py @ line 352-356](../../../translatepy/language.py#L352-L356)

Groups all of the data

### *attr* LanguageData.**codes**

> [Source: ../../../translatepy/language.py @ line 354](../../../translatepy/language.py#L354)

> Type: `Dict`

### *attr* LanguageData.**data**

> [Source: ../../../translatepy/language.py @ line 355](../../../translatepy/language.py#L355)

> Type: `Dict`

### *attr* LanguageData.**vectors**

> [Source: ../../../translatepy/language.py @ line 356](../../../translatepy/language.py#L356)

> Type: `List`

## *const* **LANGUAGE_DATA_DIR**

> [Source: ../../../translatepy/language.py @ line 360](../../../translatepy/language.py#L360)

The directory where all of the data is stored

## *const* **DATA**

> [Source: ../../../translatepy/language.py @ line 363](../../../translatepy/language.py#L363)

The languages in-memory data

## *const* **TRANSLATEPY_LANGUAGE_FULL**

> [Source: ../../../translatepy/language.py @ line 369](../../../translatepy/language.py#L369)

If the full language data database got loaded at runtime

## *func* **load_full**

> [Source: ../../../translatepy/language.py @ line 378-385](../../../translatepy/language.py#L378-L385)

Loads the full data languages DB

## *const* **COMMON_LANGUAGES**

> [Source: ../../../translatepy/language.py @ line 392](../../../translatepy/language.py#L392)

All of the available foreign languages for the `foreign` field on the `Language` class and English
