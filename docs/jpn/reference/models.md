# *module* **models**

> [Source: ../../../translatepy/models.py](../../../translatepy/models.py#L0)

translatepy/models.py  
Describes the different result models returned by the translators

## Imports

- [../../../translatepy/language.py](../../../translatepy/language.py): As `Language`

- [../../../translatepy/utils/audio.py](../../../translatepy/utils/audio.py): As `get_type`

## *class* [**Speed**](../../../translatepy/models.py#L23-L28)

Represents a speed percentage

### *attr* [Speed.**FULL**](../../../translatepy/models.py#L25)

### *attr* [Speed.**HALF**](../../../translatepy/models.py#L26)

### *attr* [Speed.**QUARTER**](../../../translatepy/models.py#L27)

### *attr* [Speed.**SLOW**](../../../translatepy/models.py#L28)

## *class* [**Gender**](../../../translatepy/models.py#L31-L36)

Represents a gender

### *attr* [Gender.**MALE**](../../../translatepy/models.py#L33)

### *attr* [Gender.**FEMALE**](../../../translatepy/models.py#L34)

### *attr* [Gender.**OTHER**](../../../translatepy/models.py#L35)

### *attr* [Gender.**GENDERLESS**](../../../translatepy/models.py#L36)

## *class* [**WordClass**](../../../translatepy/models.py#L39-L110)

Part of speech

> **Note**
> Refer to https://en.wikipedia.org/wiki/Part_of_speech

### *attr* [WordClass.**NOUN**](../../../translatepy/models.py#L45)

A word or lexical item denoting any abstract (abstract noun: e.g. home) or concrete entity (concrete noun: e.g. house);  
a person (police officer, Michael), place (coastline, London), thing (necktie, television), idea (happiness), or quality (bravery).  
Nouns can also be classified as count nouns or non-count nouns; some can belong to either category. The most common part of speech; they are called naming words.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**PRONOUN**](../../../translatepy/models.py#L54)

A substitute for a noun or noun phrase (them, he). Pronouns make sentences shorter and clearer since they replace nouns.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**ADJECTIVE**](../../../translatepy/models.py#L60)

A modifier of a noun or pronoun (big, brave). Adjectives make the meaning of another word (noun) more precise.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**VERB**](../../../translatepy/models.py#L66)

A word denoting an action (walk), occurrence (happen), or state of being (be). Without a verb, a group of words cannot be a clause or sentence.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**ADVERB**](../../../translatepy/models.py#L72)

A modifier of an adjective, verb, or another adverb (very, quite). Adverbs make language more precise.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**PREPOSITION**](../../../translatepy/models.py#L78)

A word that relates words to each other in a phrase or sentence and aids in syntactic context (in, of).  
Prepositions show the relationship between a noun or a pronoun with another word in the sentence.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**CONJUNCTION**](../../../translatepy/models.py#L86)

A syntactic connector; links words, phrases, or clauses (and, but). Conjunctions connect words or group of words  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**INTERJECTION**](../../../translatepy/models.py#L92)

An emotional greeting or exclamation (Huzzah, Alas). Interjections express strong feelings and emotions.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**ARTICLE**](../../../translatepy/models.py#L98)

A grammatical marker of definiteness (the) or indefiniteness (a, an).  
The article is not always listed among the parts of speech.  
It is considered by some grammarians to be a type of adjective or sometimes the term 'determiner' (a broader class) is used.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* [WordClass.**OTHER**](../../../translatepy/models.py#L107)

For other part of speech

## *const* [**Translator**](../../../translatepy/models.py#L113)

## *const* [**PRIVATE_ATTRIBUTES**](../../../translatepy/models.py#L115)

## *func* [**should_be_exported**](../../../translatepy/models.py#L118-L121)

if the given attribute should be exposed or not

### Parameters

- **attr**: `str`


## *class* [**ResultAttribute**](../../../translatepy/models.py#L125-L129)

Details about a result attribute

### *attr* [ResultAttribute.**name**](../../../translatepy/models.py#L127)

> Type: `str`

### *attr* [ResultAttribute.**annotation**](../../../translatepy/models.py#L128)

> Type: `Optional`

### *attr* [ResultAttribute.**description**](../../../translatepy/models.py#L129)

> Type: `Optional`

## *class* [**Result**](../../../translatepy/models.py#L136-L287)

The base result model

### Raises

- `IndexError`

### *attr* [Result.**service**](../../../translatepy/models.py#L143)

> Type: `Translator`

The service which returned the result

### *attr* [Result.**source**](../../../translatepy/models.py#L146)

> Type: `str`

The source text

### *attr* [Result.**source_lang**](../../../translatepy/models.py#L148)

> Type: `Language`

The source text's language

### *attr* [Result.**raw**](../../../translatepy/models.py#L158)

> Type: `Optional`

The raw response returned by the service.  
Note: This is very dependent on the service used.  
Refer to the service documentation to learn how to use this object.

### *property* [Result.**attributes**](../../../translatepy/models.py#L217-L267)

The different attributes on the dataclass

#### Parameters

- **cls**


#### Returns

- `list`

### *property* [Result.**exported**](../../../translatepy/models.py#L270-L281)

A dictionary version of the dataclass which can be exposed to the public

#### Returns

- `dict`

## *class* [**TranslationResult**](../../../translatepy/models.py#L291-L329)

Holds the result of a regular translation

### *attr* [TranslationResult.**dest_lang**](../../../translatepy/models.py#L296)

> Type: `Language`

The result's language

### *attr* [TranslationResult.**translation**](../../../translatepy/models.py#L299)

> Type: `str`

The translation result

### *property* [TranslationResult.**alternatives**](../../../translatepy/models.py#L306-L310)

Returns the alternative translations associated

## *const* [**TRANSLATION_TEST**](../../../translatepy/models.py#L332)

## *class* [**TransliterationResult**](../../../translatepy/models.py#L344-L371)

Holds the result of a transliteration

### *attr* [TransliterationResult.**transliteration**](../../../translatepy/models.py#L348)

> Type: `str`

The transliteration result

### *attr* [TransliterationResult.**dest_lang**](../../../translatepy/models.py#L351)

> Type: `Language`

The result's language

## *const* [**TRANSLITERATION_TEST**](../../../translatepy/models.py#L374)

## *class* [**SpellcheckResult**](../../../translatepy/models.py#L384-L410)

Holds a spellchecking result

### *attr* [SpellcheckResult.**rich**](../../../translatepy/models.py#L389)

### *attr* [SpellcheckResult.**source_lang**](../../../translatepy/models.py#L391)

> Type: `Language`

The source text's language

### *attr* [SpellcheckResult.**corrected**](../../../translatepy/models.py#L393)

> Type: `str`

The corrected text

## *const* [**SPELLCHECK_TEST**](../../../translatepy/models.py#L413)

## *class* [**SpellcheckMistake**](../../../translatepy/models.py#L422-L435)

This holds a mistake made detected by the spellchecker

### *attr* [SpellcheckMistake.**start**](../../../translatepy/models.py#L424)

> Type: `int`

The beginning index of the part to correct in the original text

### *attr* [SpellcheckMistake.**end**](../../../translatepy/models.py#L426)

> Type: `int`

The ending index of the part to correct in the original text

### *attr* [SpellcheckMistake.**corrected**](../../../translatepy/models.py#L428)

> Type: `str`

The corrected part

### *attr* [SpellcheckMistake.**message**](../../../translatepy/models.py#L431)

> Type: `Optional`

A message explaining what happened

### *attr* [SpellcheckMistake.**rule**](../../../translatepy/models.py#L434)

> Type: `Optional`

A string which identifies the rule associated with the mistake made

## *class* [**RichSpellcheckResult**](../../../translatepy/models.py#L441-L601)

Holds a rich spellchecking result

### *attr* [RichSpellcheckResult.**rich**](../../../translatepy/models.py#L447)

### *attr* [RichSpellcheckResult.**source_lang**](../../../translatepy/models.py#L449)

> Type: `Language`

The source text's language

### *attr* [RichSpellcheckResult.**mistakes**](../../../translatepy/models.py#L451)

> Type: `List`

The different mistakes made

### *property* [RichSpellcheckResult.**corrected**](../../../translatepy/models.py#L455-L463)

The corrected text

#### Returns

- `str`

## *const* [**RICH_SPELLCHECK_TEST**](../../../translatepy/models.py#L604)

## *class* [**LanguageResult**](../../../translatepy/models.py#L618-L628)

Holds the language of the given text

## *const* [**LANGUAGE_TEST**](../../../translatepy/models.py#L631)

## *class* [**ExampleResult**](../../../translatepy/models.py#L635-L725)

Holds an example sentence where the given word is used.

### *attr* [ExampleResult.**example**](../../../translatepy/models.py#L641)

> Type: `str`

The example

### *attr* [ExampleResult.**reference**](../../../translatepy/models.py#L644)

> Type: `Optional`

Where the example comes from (i.e a book or a the person who said it if it's a quote)

### *property* [ExampleResult.**position**](../../../translatepy/models.py#L648-L655)

The first position of the word in the example

#### Returns

- `NoneType`

- `int`

### *property* [ExampleResult.**positions**](../../../translatepy/models.py#L658-L690)

The positions of the word in the example

#### Returns

- `list[int]`
    - A list of positions of the word in the example

## *const* [**EXAMPLE_TEST**](../../../translatepy/models.py#L728)

## *class* [**DictionaryResult**](../../../translatepy/models.py#L737-L752)

Holds the meaning of the given text

### *attr* [DictionaryResult.**rich**](../../../translatepy/models.py#L743)

### *attr* [DictionaryResult.**meaning**](../../../translatepy/models.py#L745)

> Type: `str`

The meaning of the text

## *const* [**DICTIONARY_TEST**](../../../translatepy/models.py#L755)

## *class* [**EtymologicalNode**](../../../translatepy/models.py#L764-L791)

The node of an etymological tree

### *attr* [EtymologicalNode.**origin**](../../../translatepy/models.py#L766)

> Type: `str`

The origin name (i.e 'Latin')

### *attr* [EtymologicalNode.**source**](../../../translatepy/models.py#L769)

> Type: `Optional`

The original way of writing it

### *attr* [EtymologicalNode.**year**](../../../translatepy/models.py#L771)

> Type: `Optional`

The year of origin

## *class* [**RichDictionaryResult**](../../../translatepy/models.py#L795-L904)

Holds more (optional) information than the regular `DictionaryResult`

### *attr* [RichDictionaryResult.**rich**](../../../translatepy/models.py#L801)

### *attr* [RichDictionaryResult.**etymology**](../../../translatepy/models.py#L803)

> Type: `List`

The etymological/origins tree of the given text  
Each element corresponds to a node in the tree of origins for the given text

#### Examples

##### Example 1

`Node1 (Greek) -> Node2 (Latin) -> Node3 (French) -> Node4 (Ancient English) -> Current Word`

### *attr* [RichDictionaryResult.**gender**](../../../translatepy/models.py#L814)

> Type: `Gender`

For languages which assign genders on words

#### Examples

##### Example 1

`chaîse (french; a chair) -> Gender.FEMALE`

### *attr* [RichDictionaryResult.**pronunciation**](../../../translatepy/models.py#L823)

> Type: `Optional`

A way of pronouncing the text

### *attr* [RichDictionaryResult.**type**](../../../translatepy/models.py#L826)

> Type: `WordClass`

The part of speech of the text

### *attr* [RichDictionaryResult.**synonyms**](../../../translatepy/models.py#L829)

> Type: `List`

### *attr* [RichDictionaryResult.**antonyms**](../../../translatepy/models.py#L830)

> Type: `List`

## *const* [**RICH_DICTIONARY_TEST**](../../../translatepy/models.py#L907)

## *class* [**TextToSpeechResult**](../../../translatepy/models.py#L922-L988)

Holds the text to speech results

### *attr* [TextToSpeechResult.**result**](../../../translatepy/models.py#L928)

> Type: `bytes`

Text to speech result

### *attr* [TextToSpeechResult.**speed**](../../../translatepy/models.py#L930)

> Type: `int`

Speed of the text to speech result

### *attr* [TextToSpeechResult.**gender**](../../../translatepy/models.py#L932)

> Type: `Gender`

Gender of the 'person' saying the text

### *property* [TextToSpeechResult.**type**](../../../translatepy/models.py#L936-L938)

Returns the type of audio file

### *property* [TextToSpeechResult.**mime_type**](../../../translatepy/models.py#L941-L953)

Returns the MIME type of the audio file

#### Returns

- `Optional[str]`
    - The MIME type of the audio file

### *property* [TextToSpeechResult.**extension**](../../../translatepy/models.py#L956-L968)

Returns the audio file extension

#### Returns

- `Optional[str]`
    - The MIME type of the audio file

### *func* [TextToSpeechResult.**write_to_file**](../../../translatepy/models.py#L970-L988)

Writes the spoken text to a file.

#### Parameters

- **file**: `BinaryIO`, `IO`, `Path`, `str`
  - The output path or object


- **replace_ext**: `bool`
  - Default Value: `True`
  - If we need to change the extension of the file to match the right file type


## *class* [**HTMLTranslationNode**](../../../translatepy/models.py#L992-L1029)

A translation node, containing the DOM element and its translation result

### *attr* [HTMLTranslationNode.**node**](../../../translatepy/models.py#L996)

> Type: `bs4.NavigableString`

### *attr* [HTMLTranslationNode.**result**](../../../translatepy/models.py#L997)

> Type: `Optional`

### *property* [HTMLTranslationNode.**position**](../../../translatepy/models.py#L1000-L1020)

The position of the node in the HTML

#### Returns

- `int`

### *property* [HTMLTranslationNode.**exported**](../../../translatepy/models.py#L1023-L1029)

The exported dictionary

#### Returns

- `dict`

## *class* [**HTMLTranslationResult**](../../../translatepy/models.py#L1033-L1052)

Holds an HTML translation result

### *attr* [HTMLTranslationResult.**result**](../../../translatepy/models.py#L1037)

> Type: `str`

### *attr* [HTMLTranslationResult.**soup**](../../../translatepy/models.py#L1038)

> Type: `bs4.BeautifulSoup`

### *attr* [HTMLTranslationResult.**nodes**](../../../translatepy/models.py#L1039)

> Type: `List`

### *property* [HTMLTranslationResult.**exported**](../../../translatepy/models.py#L1048-L1052)

#### Returns

- `dict`
