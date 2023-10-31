# *module* **models**

> [Source: ../../../../models.py](../../../../models.py#L0)

translatepy/models.py  
Describes the different result models returned by the translators

## Imports

- [../../../../language.py](../../../../language.py): As `Language`

- [../../../../utils/audio.py](../../../../utils/audio.py): As `get_type`

## *class* [**Speed**](../../../../models.py#L23-L28)

Represents a speed percentage

### *attr* [Speed.**FULL**](../../../../models.py#L25)

### *attr* [Speed.**HALF**](../../../../models.py#L26)

### *attr* [Speed.**QUARTER**](../../../../models.py#L27)

### *attr* [Speed.**SLOW**](../../../../models.py#L28)

## *class* [**Gender**](../../../../models.py#L31-L36)

Represents a gender

### *attr* [Gender.**MALE**](../../../../models.py#L33)

### *attr* [Gender.**FEMALE**](../../../../models.py#L34)

### *attr* [Gender.**OTHER**](../../../../models.py#L35)

### *attr* [Gender.**GENDERLESS**](../../../../models.py#L36)

## *class* [**WordClass**](../../../../models.py#L39-L110)

Part of speech

> **Note**
> Refer to https://en.wikipedia.org/wiki/Part_of_speech

### *attr* [WordClass.**NOUN**](../../../../models.py#L45)

A word or lexical item denoting any abstract (abstract noun: e.g. home) or concrete entity (concrete noun: e.g. house);  
a person (police officer, Michael), place (coastline, London), thing (necktie, television), idea (happiness), or quality (bravery).  
Nouns can also be classified as count nouns or non-count nouns; some can belong to either category. The most common part of speech; they are called naming words.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**PRONOUN**](../../../../models.py#L54)

A substitute for a noun or noun phrase (them, he). Pronouns make sentences shorter and clearer since they replace nouns.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**ADJECTIVE**](../../../../models.py#L60)

A modifier of a noun or pronoun (big, brave). Adjectives make the meaning of another word (noun) more precise.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**VERB**](../../../../models.py#L66)

A word denoting an action (walk), occurrence (happen), or state of being (be). Without a verb, a group of words cannot be a clause or sentence.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**ADVERB**](../../../../models.py#L72)

A modifier of an adjective, verb, or another adverb (very, quite). Adverbs make language more precise.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**PREPOSITION**](../../../../models.py#L78)

A word that relates words to each other in a phrase or sentence and aids in syntactic context (in, of).  
Prepositions show the relationship between a noun or a pronoun with another word in the sentence.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**CONJUNCTION**](../../../../models.py#L86)

A syntactic connector; links words, phrases, or clauses (and, but). Conjunctions connect words or group of words  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**INTERJECTION**](../../../../models.py#L92)

An emotional greeting or exclamation (Huzzah, Alas). Interjections express strong feelings and emotions.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**ARTICLE**](../../../../models.py#L98)

A grammatical marker of definiteness (the) or indefiniteness (a, an).  
The article is not always listed among the parts of speech.  
It is considered by some grammarians to be a type of adjective or sometimes the term 'determiner' (a broader class) is used.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**OTHER**](../../../../models.py#L107)

For other part of speech

## *const* [**Translator**](../../../../models.py#L113)

## *const* [**PRIVATE_ATTRIBUTES**](../../../../models.py#L115)

## *func* [**should_be_exported**](../../../../models.py#L118-L121)

if the given attribute should be exposed or not

### Parameters

- **attr**: `str`


## *class* [**ResultAttribute**](../../../../models.py#L125-L129)

Details about a result attribute

### *attr* [ResultAttribute.**name**](../../../../models.py#L127)

> Type: `str`

### *attr* [ResultAttribute.**annotation**](../../../../models.py#L128)

> Type: `Optional`

### *attr* [ResultAttribute.**description**](../../../../models.py#L129)

> Type: `Optional`

## *class* [**Result**](../../../../models.py#L136-L287)

The base result model

### Raises

- `IndexError`

### *attr* [Result.**service**](../../../../models.py#L143)

> Type: `Translator`

The service which returned the result

### *attr* [Result.**source**](../../../../models.py#L146)

> Type: `str`

The source text

### *attr* [Result.**source_lang**](../../../../models.py#L148)

> Type: `Language`

The source text's language

### *attr* [Result.**raw**](../../../../models.py#L158)

> Type: `Optional`

The raw response returned by the service.  
Note: This is very dependent on the service used.  
Refer to the service documentation to learn how to use this object.

### *property* [Result.**attributes**](../../../../models.py#L217-L267)

The different attributes on the dataclass

#### Parameters

- **cls**


#### Returns

- `list`

### *property* [Result.**exported**](../../../../models.py#L270-L281)

A dictionary version of the dataclass which can be exposed to the public

#### Returns

- `dict`

## *class* [**TranslationResult**](../../../../models.py#L291-L329)

Holds the result of a regular translation

### *attr* [TranslationResult.**dest_lang**](../../../../models.py#L296)

> Type: `Language`

The result's language

### *attr* [TranslationResult.**translation**](../../../../models.py#L299)

> Type: `str`

The translation result

### *property* [TranslationResult.**alternatives**](../../../../models.py#L306-L310)

Returns the alternative translations associated

## *const* [**TRANSLATION_TEST**](../../../../models.py#L332)

## *class* [**TransliterationResult**](../../../../models.py#L344-L371)

Holds the result of a transliteration

### *attr* [TransliterationResult.**transliteration**](../../../../models.py#L348)

> Type: `str`

The transliteration result

### *attr* [TransliterationResult.**dest_lang**](../../../../models.py#L351)

> Type: `Language`

The result's language

## *const* [**TRANSLITERATION_TEST**](../../../../models.py#L374)

## *class* [**SpellcheckResult**](../../../../models.py#L384-L410)

Holds a spellchecking result

### *attr* [SpellcheckResult.**rich**](../../../../models.py#L389)

### *attr* [SpellcheckResult.**source_lang**](../../../../models.py#L391)

> Type: `Language`

The source text's language

### *attr* [SpellcheckResult.**corrected**](../../../../models.py#L393)

> Type: `str`

The corrected text

## *const* [**SPELLCHECK_TEST**](../../../../models.py#L413)

## *class* [**SpellcheckMistake**](../../../../models.py#L422-L435)

This holds a mistake made detected by the spellchecker

### *attr* [SpellcheckMistake.**start**](../../../../models.py#L424)

> Type: `int`

The beginning index of the part to correct in the original text

### *attr* [SpellcheckMistake.**end**](../../../../models.py#L426)

> Type: `int`

The ending index of the part to correct in the original text

### *attr* [SpellcheckMistake.**corrected**](../../../../models.py#L428)

> Type: `str`

The corrected part

### *attr* [SpellcheckMistake.**message**](../../../../models.py#L431)

> Type: `Optional`

A message explaining what happened

### *attr* [SpellcheckMistake.**rule**](../../../../models.py#L434)

> Type: `Optional`

A string which identifies the rule associated with the mistake made

## *class* [**RichSpellcheckResult**](../../../../models.py#L441-L601)

Holds a rich spellchecking result

### *attr* [RichSpellcheckResult.**rich**](../../../../models.py#L447)

### *attr* [RichSpellcheckResult.**source_lang**](../../../../models.py#L449)

> Type: `Language`

The source text's language

### *attr* [RichSpellcheckResult.**mistakes**](../../../../models.py#L451)

> Type: `List`

The different mistakes made

### *property* [RichSpellcheckResult.**corrected**](../../../../models.py#L455-L463)

The corrected text

#### Returns

- `str`

## *const* [**RICH_SPELLCHECK_TEST**](../../../../models.py#L604)

## *class* [**LanguageResult**](../../../../models.py#L618-L628)

Holds the language of the given text

## *const* [**LANGUAGE_TEST**](../../../../models.py#L631)

## *class* [**ExampleResult**](../../../../models.py#L635-L725)

Holds an example sentence where the given word is used.

### *attr* [ExampleResult.**example**](../../../../models.py#L641)

> Type: `str`

The example

### *attr* [ExampleResult.**reference**](../../../../models.py#L644)

> Type: `Optional`

Where the example comes from (i.e a book or a the person who said it if it's a quote)

### *property* [ExampleResult.**position**](../../../../models.py#L648-L655)

The first position of the word in the example

#### Returns

- `NoneType`

- `int`

### *property* [ExampleResult.**positions**](../../../../models.py#L658-L690)

The positions of the word in the example

#### Returns

- `list[int]`
    - A list of positions of the word in the example

## *const* [**EXAMPLE_TEST**](../../../../models.py#L728)

## *class* [**DictionaryResult**](../../../../models.py#L737-L752)

Holds the meaning of the given text

### *attr* [DictionaryResult.**rich**](../../../../models.py#L743)

### *attr* [DictionaryResult.**meaning**](../../../../models.py#L745)

> Type: `str`

The meaning of the text

## *const* [**DICTIONARY_TEST**](../../../../models.py#L755)

## *class* [**EtymologicalNode**](../../../../models.py#L764-L791)

The node of an etymological tree

### *attr* [EtymologicalNode.**origin**](../../../../models.py#L766)

> Type: `str`

The origin name (i.e 'Latin')

### *attr* [EtymologicalNode.**source**](../../../../models.py#L769)

> Type: `Optional`

The original way of writing it

### *attr* [EtymologicalNode.**year**](../../../../models.py#L771)

> Type: `Optional`

The year of origin

## *class* [**RichDictionaryResult**](../../../../models.py#L795-L904)

Holds more (optional) information than the regular `DictionaryResult`

### *attr* [RichDictionaryResult.**rich**](../../../../models.py#L801)

### *attr* [RichDictionaryResult.**etymology**](../../../../models.py#L803)

> Type: `List`

The etymological/origins tree of the given text  
Each element corresponds to a node in the tree of origins for the given text

#### Examples

##### Example 1

`Node1 (Greek) -> Node2 (Latin) -> Node3 (French) -> Node4 (Ancient English) -> Current Word`

### *attr* [RichDictionaryResult.**gender**](../../../../models.py#L814)

> Type: `Gender`

For languages which assign genders on words

#### Examples

##### Example 1

`chaîse (french; a chair) -> Gender.FEMALE`

### *attr* [RichDictionaryResult.**pronunciation**](../../../../models.py#L823)

> Type: `Optional`

A way of pronouncing the text

### *attr* [RichDictionaryResult.**type**](../../../../models.py#L826)

> Type: `WordClass`

The part of speech of the text

### *attr* [RichDictionaryResult.**synonyms**](../../../../models.py#L829)

> Type: `List`

### *attr* [RichDictionaryResult.**antonyms**](../../../../models.py#L830)

> Type: `List`

## *const* [**RICH_DICTIONARY_TEST**](../../../../models.py#L907)

## *class* [**TextToSpeechResult**](../../../../models.py#L922-L988)

Holds the text to speech results

### *attr* [TextToSpeechResult.**result**](../../../../models.py#L928)

> Type: `bytes`

Text to speech result

### *attr* [TextToSpeechResult.**speed**](../../../../models.py#L930)

> Type: `int`

Speed of the text to speech result

### *attr* [TextToSpeechResult.**gender**](../../../../models.py#L932)

> Type: `Gender`

Gender of the 'person' saying the text

### *property* [TextToSpeechResult.**type**](../../../../models.py#L936-L938)

Returns the type of audio file

### *property* [TextToSpeechResult.**mime_type**](../../../../models.py#L941-L953)

Returns the MIME type of the audio file

#### Returns

- `Optional[str]`
    - The MIME type of the audio file

### *property* [TextToSpeechResult.**extension**](../../../../models.py#L956-L968)

Returns the audio file extension

#### Returns

- `Optional[str]`
    - The MIME type of the audio file

### *func* [TextToSpeechResult.**write_to_file**](../../../../models.py#L970-L988)

Writes the spoken text to a file.

#### Parameters

- **file**: `BinaryIO`, `IO`, `Path`, `str`
  - The output path or object


- **replace_ext**: `bool`
  - Default Value: `True`
  - If we need to change the extension of the file to match the right file type


## *class* [**HTMLTranslationNode**](../../../../models.py#L992-L1029)

A translation node, containing the DOM element and its translation result

### *attr* [HTMLTranslationNode.**node**](../../../../models.py#L996)

> Type: `bs4.NavigableString`

### *attr* [HTMLTranslationNode.**result**](../../../../models.py#L997)

> Type: `Optional`

### *property* [HTMLTranslationNode.**position**](../../../../models.py#L1000-L1020)

The position of the node in the HTML

#### Returns

- `int`

### *property* [HTMLTranslationNode.**exported**](../../../../models.py#L1023-L1029)

The exported dictionary

#### Returns

- `dict`

## *class* [**HTMLTranslationResult**](../../../../models.py#L1033-L1052)

Holds an HTML translation result

### *attr* [HTMLTranslationResult.**result**](../../../../models.py#L1037)

> Type: `str`

### *attr* [HTMLTranslationResult.**soup**](../../../../models.py#L1038)

> Type: `bs4.BeautifulSoup`

### *attr* [HTMLTranslationResult.**nodes**](../../../../models.py#L1039)

> Type: `List`

### *property* [HTMLTranslationResult.**exported**](../../../../models.py#L1048-L1052)

#### Returns

- `dict`
