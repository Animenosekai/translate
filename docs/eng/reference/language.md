# *module* **language**

> [Source: ../../../translatepy/language.py](../../../translatepy/language.py#L0)

Handles the languages management on `translatepy`

## Imports

- [../../../translatepy/exceptions.py](../../../translatepy/exceptions.py): As `exceptions`

- [../../../translatepy/utils/lru.py](../../../translatepy/utils/lru.py): As `lru`

- [../../../translatepy/utils/vectorize.py](../../../translatepy/utils/vectorize.py): As `vectorize`

## *const* [**Number**](../../../translatepy/language.py#L17)

Represents a number

## *class* [**LanguageExtra**](../../../translatepy/language.py#L21-L34)

Extra data given on supported languages

### *attr* [LanguageExtra.**scope**](../../../translatepy/language.py#L23)

> Type: `cain.types.Enum`

Language scope

> **Note**
> Can be one of "individual", "macrolanguage", "special"

### *attr* [LanguageExtra.**type**](../../../translatepy/language.py#L28)

> Type: `cain.types.Enum`

Language type

> **Note**
> Can be one of "ancient", "constructed", "extinct", "historical", "living", "special"

## *class* [**Foreign**](../../../translatepy/language.py#L37-L208)

The language name in foreign languages

### *attr* [Foreign.**afrikaans**](../../../translatepy/language.py#L39)

> Type: `str`

The language name in afrikaans

### *attr* [Foreign.**albanian**](../../../translatepy/language.py#L41)

> Type: `str`

The language name in albanian

### *attr* [Foreign.**amharic**](../../../translatepy/language.py#L43)

> Type: `str`

The language name in amharic

### *attr* [Foreign.**arabic**](../../../translatepy/language.py#L45)

> Type: `str`

The language name in arabic

### *attr* [Foreign.**armenian**](../../../translatepy/language.py#L47)

> Type: `str`

The language name in armenian

### *attr* [Foreign.**azerbaijani**](../../../translatepy/language.py#L49)

> Type: `str`

The language name in azerbaijani

### *attr* [Foreign.**basque**](../../../translatepy/language.py#L51)

> Type: `str`

The language name in basque

### *attr* [Foreign.**belarusian**](../../../translatepy/language.py#L53)

> Type: `str`

The language name in belarusian

### *attr* [Foreign.**bengali**](../../../translatepy/language.py#L55)

> Type: `str`

The language name in bengali

### *attr* [Foreign.**bosnian**](../../../translatepy/language.py#L57)

> Type: `str`

The language name in bosnian

### *attr* [Foreign.**bulgarian**](../../../translatepy/language.py#L59)

> Type: `str`

The language name in bulgarian

### *attr* [Foreign.**burmese**](../../../translatepy/language.py#L61)

> Type: `str`

The language name in burmese

### *attr* [Foreign.**catalan**](../../../translatepy/language.py#L63)

> Type: `str`

The language name in catalan

### *attr* [Foreign.**chinese**](../../../translatepy/language.py#L65)

> Type: `str`

The language name in chinese

### *attr* [Foreign.**croatian**](../../../translatepy/language.py#L67)

> Type: `str`

The language name in croatian

### *attr* [Foreign.**czech**](../../../translatepy/language.py#L69)

> Type: `str`

The language name in czech

### *attr* [Foreign.**danish**](../../../translatepy/language.py#L71)

> Type: `str`

The language name in danish

### *attr* [Foreign.**dutch**](../../../translatepy/language.py#L73)

> Type: `str`

The language name in dutch

### *attr* [Foreign.**esperanto**](../../../translatepy/language.py#L75)

> Type: `str`

The language name in esperanto

### *attr* [Foreign.**estonian**](../../../translatepy/language.py#L77)

> Type: `str`

The language name in estonian

### *attr* [Foreign.**finnish**](../../../translatepy/language.py#L79)

> Type: `str`

The language name in finnish

### *attr* [Foreign.**french**](../../../translatepy/language.py#L81)

> Type: `str`

The language name in french

### *attr* [Foreign.**galician**](../../../translatepy/language.py#L83)

> Type: `str`

The language name in galician

### *attr* [Foreign.**georgian**](../../../translatepy/language.py#L85)

> Type: `str`

The language name in georgian

### *attr* [Foreign.**german**](../../../translatepy/language.py#L87)

> Type: `str`

The language name in german

### *attr* [Foreign.**gujarati**](../../../translatepy/language.py#L89)

> Type: `str`

The language name in gujarati

### *attr* [Foreign.**haitian**](../../../translatepy/language.py#L91)

> Type: `str`

The language name in haitian

### *attr* [Foreign.**hebrew**](../../../translatepy/language.py#L93)

> Type: `str`

The language name in hebrew

### *attr* [Foreign.**hindi**](../../../translatepy/language.py#L95)

> Type: `str`

The language name in hindi

### *attr* [Foreign.**hungarian**](../../../translatepy/language.py#L97)

> Type: `str`

The language name in hungarian

### *attr* [Foreign.**icelandic**](../../../translatepy/language.py#L99)

> Type: `str`

The language name in icelandic

### *attr* [Foreign.**indonesian**](../../../translatepy/language.py#L101)

> Type: `str`

The language name in indonesian

### *attr* [Foreign.**irish**](../../../translatepy/language.py#L103)

> Type: `str`

The language name in irish

### *attr* [Foreign.**italian**](../../../translatepy/language.py#L105)

> Type: `str`

The language name in italian

### *attr* [Foreign.**japanese**](../../../translatepy/language.py#L107)

> Type: `str`

The language name in japanese

### *attr* [Foreign.**javanese**](../../../translatepy/language.py#L109)

> Type: `str`

The language name in javanese

### *attr* [Foreign.**kannada**](../../../translatepy/language.py#L111)

> Type: `str`

The language name in kannada

### *attr* [Foreign.**kazakh**](../../../translatepy/language.py#L113)

> Type: `str`

The language name in kazakh

### *attr* [Foreign.**khmer**](../../../translatepy/language.py#L115)

> Type: `str`

The language name in khmer

### *attr* [Foreign.**kirghiz**](../../../translatepy/language.py#L117)

> Type: `str`

The language name in kirghiz

### *attr* [Foreign.**korean**](../../../translatepy/language.py#L119)

> Type: `str`

The language name in korean

### *attr* [Foreign.**lao**](../../../translatepy/language.py#L121)

> Type: `str`

The language name in lao

### *attr* [Foreign.**latin**](../../../translatepy/language.py#L123)

> Type: `str`

The language name in latin

### *attr* [Foreign.**latvian**](../../../translatepy/language.py#L125)

> Type: `str`

The language name in latvian

### *attr* [Foreign.**lithuanian**](../../../translatepy/language.py#L127)

> Type: `str`

The language name in lithuanian

### *attr* [Foreign.**luxembourgish**](../../../translatepy/language.py#L129)

> Type: `str`

The language name in luxembourgish

### *attr* [Foreign.**macedonian**](../../../translatepy/language.py#L131)

> Type: `str`

The language name in macedonian

### *attr* [Foreign.**malagasy**](../../../translatepy/language.py#L133)

> Type: `str`

The language name in malagasy

### *attr* [Foreign.**malay**](../../../translatepy/language.py#L135)

> Type: `str`

The language name in malay

### *attr* [Foreign.**maltese**](../../../translatepy/language.py#L137)

> Type: `str`

The language name in maltese

### *attr* [Foreign.**maori**](../../../translatepy/language.py#L139)

> Type: `str`

The language name in maori

### *attr* [Foreign.**marathi**](../../../translatepy/language.py#L141)

> Type: `str`

The language name in marathi

### *attr* [Foreign.**moderngreek**](../../../translatepy/language.py#L143)

> Type: `str`

The language name in moderngreek

### *attr* [Foreign.**mongolian**](../../../translatepy/language.py#L145)

> Type: `str`

The language name in mongolian

### *attr* [Foreign.**nepali**](../../../translatepy/language.py#L147)

> Type: `str`

The language name in nepali

### *attr* [Foreign.**norwegian**](../../../translatepy/language.py#L149)

> Type: `str`

The language name in norwegian

### *attr* [Foreign.**panjabi**](../../../translatepy/language.py#L151)

> Type: `str`

The language name in panjabi

### *attr* [Foreign.**persian**](../../../translatepy/language.py#L153)

> Type: `str`

The language name in persian

### *attr* [Foreign.**polish**](../../../translatepy/language.py#L155)

> Type: `str`

The language name in polish

### *attr* [Foreign.**portuguese**](../../../translatepy/language.py#L157)

> Type: `str`

The language name in portuguese

### *attr* [Foreign.**romanian**](../../../translatepy/language.py#L159)

> Type: `str`

The language name in romanian

### *attr* [Foreign.**russian**](../../../translatepy/language.py#L161)

> Type: `str`

The language name in russian

### *attr* [Foreign.**scottishgaelic**](../../../translatepy/language.py#L163)

> Type: `str`

The language name in scottishgaelic

### *attr* [Foreign.**serbian**](../../../translatepy/language.py#L165)

> Type: `str`

The language name in serbian

### *attr* [Foreign.**sinhala**](../../../translatepy/language.py#L167)

> Type: `str`

The language name in sinhala

### *attr* [Foreign.**slovak**](../../../translatepy/language.py#L169)

> Type: `str`

The language name in slovak

### *attr* [Foreign.**slovenian**](../../../translatepy/language.py#L171)

> Type: `str`

The language name in slovenian

### *attr* [Foreign.**spanish**](../../../translatepy/language.py#L173)

> Type: `str`

The language name in spanish

### *attr* [Foreign.**sundanese**](../../../translatepy/language.py#L175)

> Type: `str`

The language name in sundanese

### *attr* [Foreign.**swahili**](../../../translatepy/language.py#L177)

> Type: `str`

The language name in swahili

### *attr* [Foreign.**swedish**](../../../translatepy/language.py#L179)

> Type: `str`

The language name in swedish

### *attr* [Foreign.**tagalog**](../../../translatepy/language.py#L181)

> Type: `str`

The language name in tagalog

### *attr* [Foreign.**tajik**](../../../translatepy/language.py#L183)

> Type: `str`

The language name in tajik

### *attr* [Foreign.**tamil**](../../../translatepy/language.py#L185)

> Type: `str`

The language name in tamil

### *attr* [Foreign.**telugu**](../../../translatepy/language.py#L187)

> Type: `str`

The language name in telugu

### *attr* [Foreign.**thai**](../../../translatepy/language.py#L189)

> Type: `str`

The language name in thai

### *attr* [Foreign.**turkish**](../../../translatepy/language.py#L191)

> Type: `str`

The language name in turkish

### *attr* [Foreign.**ukrainian**](../../../translatepy/language.py#L193)

> Type: `str`

The language name in ukrainian

### *attr* [Foreign.**urdu**](../../../translatepy/language.py#L195)

> Type: `str`

The language name in urdu

### *attr* [Foreign.**uzbek**](../../../translatepy/language.py#L197)

> Type: `str`

The language name in uzbek

### *attr* [Foreign.**vietnamese**](../../../translatepy/language.py#L199)

> Type: `str`

The language name in vietnamese

### *attr* [Foreign.**welsh**](../../../translatepy/language.py#L201)

> Type: `str`

The language name in welsh

### *attr* [Foreign.**xhosa**](../../../translatepy/language.py#L203)

> Type: `str`

The language name in xhosa

### *attr* [Foreign.**yiddish**](../../../translatepy/language.py#L205)

> Type: `str`

The language name in yiddish

### *attr* [Foreign.**zulu**](../../../translatepy/language.py#L207)

> Type: `str`

The language name in zulu

## *const* [**LANGUAGE_CACHE**](../../../translatepy/language.py#L211)

## *const* [**NULLABLE_ATTRIBUTES**](../../../translatepy/language.py#L212)

## *class* [**Language**](../../../translatepy/language.py#L215-L347)

A language

### *attr* [Language.**id**](../../../translatepy/language.py#L218)

> Type: `str`

The language identifier

### *attr* [Language.**alpha3**](../../../translatepy/language.py#L220)

> Type: `str`

The ISO 639-3 (Alpha-3) code

### *attr* [Language.**name**](../../../translatepy/language.py#L222)

> Type: `str`

The english name

### *attr* [Language.**alpha2**](../../../translatepy/language.py#L224)

> Type: `Optional`

The ISO 639-1 (Alpha-2) code, if available

### *attr* [Language.**alpha3b**](../../../translatepy/language.py#L226)

> Type: `Optional`

The ISO 639-2B (Alpha-3) code, if available

### *attr* [Language.**alpha3t**](../../../translatepy/language.py#L228)

> Type: `Optional`

The ISO 639-2T (Alpha-3) code, if available

### *attr* [Language.**extra**](../../../translatepy/language.py#L230)

> Type: `Optional`

Extra data for the language, if available

### *attr* [Language.**foreign**](../../../translatepy/language.py#L232)

> Type: `Optional`

Name in foreign languages, if available

### *func* [Language.**search**](../../../translatepy/language.py#L269-L292)

Searches the given language

#### Parameters

- **cls**


- **query**: `str`


#### Returns

- `list`

### *func* [Language.**get_extra**](../../../translatepy/language.py#L310-L317)

Retrieves the given attribute from `extra` if available

#### Parameters

- **attribute**: `str`


#### Returns

- `NoneType`

- `str`

### *func* [Language.**get_foreign**](../../../translatepy/language.py#L319-L328)

Retrieves the given attribute from `foreign` if available

#### Parameters

- **attribute**: `ForwardRef('Language')`, `str`


#### Returns

- `NoneType`

- `str`

### *property* [Language.**similarity**](../../../translatepy/language.py#L331-L333)

The similarity with the vector while searching the language

#### Returns

- `float`

### *property* [Language.**native**](../../../translatepy/language.py#L336-L338)

The native name for the language or its english name

#### Returns

- `str`

### *property* [Language.**rich**](../../../translatepy/language.py#L341-L347)

If the language discovery used the full translatepy dataset  
Note: This returns `False` if the `Language` was not fully initialized

#### Returns

- `bool`

## *class* [**LanguageData**](../../../translatepy/language.py#L352-L356)

Groups all of the data

### *attr* [LanguageData.**codes**](../../../translatepy/language.py#L354)

> Type: `Dict`

### *attr* [LanguageData.**data**](../../../translatepy/language.py#L355)

> Type: `Dict`

### *attr* [LanguageData.**vectors**](../../../translatepy/language.py#L356)

> Type: `List`

## *const* [**LANGUAGE_DATA_DIR**](../../../translatepy/language.py#L360)

The directory where all of the data is stored

## *const* [**DATA**](../../../translatepy/language.py#L363)

The languages in-memory data

## *const* [**TRANSLATEPY_LANGUAGE_FULL**](../../../translatepy/language.py#L369)

If the full language data database got loaded at runtime

## *func* [**load_full**](../../../translatepy/language.py#L378-L385)

Loads the full data languages DB

## *const* [**COMMON_LANGUAGES**](../../../translatepy/language.py#L392)

All of the available foreign languages for the `foreign` field on the `Language` class and English
