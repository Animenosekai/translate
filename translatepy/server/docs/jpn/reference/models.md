# *module* **models**

> [Source: ../../../../models.py @ line 0](../../../../models.py#L0)

translatepy/models.py  
Describes the different result models returned by the translators

## Imports

- [../../../../language.py](../../../../language.py): As `Language`

- [../../../../utils/audio.py](../../../../utils/audio.py): As `get_type`

## *class* **Speed**

> [Source: ../../../../models.py @ line 23-28](../../../../models.py#L23-L28)

Represents a speed percentage

### *attr* Speed.**FULL**

> [Source: ../../../../models.py @ line 25](../../../../models.py#L25)

### *attr* Speed.**HALF**

> [Source: ../../../../models.py @ line 26](../../../../models.py#L26)

### *attr* Speed.**QUARTER**

> [Source: ../../../../models.py @ line 27](../../../../models.py#L27)

### *attr* Speed.**SLOW**

> [Source: ../../../../models.py @ line 28](../../../../models.py#L28)

## *class* **Gender**

> [Source: ../../../../models.py @ line 31-36](../../../../models.py#L31-L36)

Represents a gender

### *attr* Gender.**MALE**

> [Source: ../../../../models.py @ line 33](../../../../models.py#L33)

### *attr* Gender.**FEMALE**

> [Source: ../../../../models.py @ line 34](../../../../models.py#L34)

### *attr* Gender.**OTHER**

> [Source: ../../../../models.py @ line 35](../../../../models.py#L35)

### *attr* Gender.**GENDERLESS**

> [Source: ../../../../models.py @ line 36](../../../../models.py#L36)

## *class* **WordClass**

> [Source: ../../../../models.py @ line 39-110](../../../../models.py#L39-L110)

Part of speech

> **Note**
> Refer to https://en.wikipedia.org/wiki/Part_of_speech

### *attr* WordClass.**NOUN**

> [Source: ../../../../models.py @ line 45](../../../../models.py#L45)

A word or lexical item denoting any abstract (abstract noun: e.g. home) or concrete entity (concrete noun: e.g. house);  
a person (police officer, Michael), place (coastline, London), thing (necktie, television), idea (happiness), or quality (bravery).  
Nouns can also be classified as count nouns or non-count nouns; some can belong to either category. The most common part of speech; they are called naming words.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**PRONOUN**

> [Source: ../../../../models.py @ line 54](../../../../models.py#L54)

A substitute for a noun or noun phrase (them, he). Pronouns make sentences shorter and clearer since they replace nouns.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**ADJECTIVE**

> [Source: ../../../../models.py @ line 60](../../../../models.py#L60)

A modifier of a noun or pronoun (big, brave). Adjectives make the meaning of another word (noun) more precise.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**VERB**

> [Source: ../../../../models.py @ line 66](../../../../models.py#L66)

A word denoting an action (walk), occurrence (happen), or state of being (be). Without a verb, a group of words cannot be a clause or sentence.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**ADVERB**

> [Source: ../../../../models.py @ line 72](../../../../models.py#L72)

A modifier of an adjective, verb, or another adverb (very, quite). Adverbs make language more precise.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**PREPOSITION**

> [Source: ../../../../models.py @ line 78](../../../../models.py#L78)

A word that relates words to each other in a phrase or sentence and aids in syntactic context (in, of).  
Prepositions show the relationship between a noun or a pronoun with another word in the sentence.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**CONJUNCTION**

> [Source: ../../../../models.py @ line 86](../../../../models.py#L86)

A syntactic connector; links words, phrases, or clauses (and, but). Conjunctions connect words or group of words  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**INTERJECTION**

> [Source: ../../../../models.py @ line 92](../../../../models.py#L92)

An emotional greeting or exclamation (Huzzah, Alas). Interjections express strong feelings and emotions.  
Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**ARTICLE**

> [Source: ../../../../models.py @ line 98](../../../../models.py#L98)

A grammatical marker of definiteness (the) or indefiniteness (a, an).  
The article is not always listed among the parts of speech.  
It is considered by some grammarians to be a type of adjective or sometimes the term 'determiner' (a broader class) is used.

> **Note**
> https://en.wikipedia.org/wiki/Part_of_speech#Classification

### *attr* WordClass.**OTHER**

> [Source: ../../../../models.py @ line 107](../../../../models.py#L107)

For other part of speech

## *const* **Translator**

> [Source: ../../../../models.py @ line 113](../../../../models.py#L113)

## *const* **PRIVATE_ATTRIBUTES**

> [Source: ../../../../models.py @ line 115](../../../../models.py#L115)

## *func* **should_be_exported**

> [Source: ../../../../models.py @ line 118-121](../../../../models.py#L118-L121)

if the given attribute should be exposed or not

### Parameters

- **attr**: `str`


## *class* **ResultAttribute**

> [Source: ../../../../models.py @ line 125-129](../../../../models.py#L125-L129)

Details about a result attribute

### *attr* ResultAttribute.**name**

> [Source: ../../../../models.py @ line 127](../../../../models.py#L127)

> Type: `str`

### *attr* ResultAttribute.**annotation**

> [Source: ../../../../models.py @ line 128](../../../../models.py#L128)

> Type: `Optional`

### *attr* ResultAttribute.**description**

> [Source: ../../../../models.py @ line 129](../../../../models.py#L129)

> Type: `Optional`

## *class* **Result**

> [Source: ../../../../models.py @ line 136-287](../../../../models.py#L136-L287)

The base result model

### Raises

- `IndexError`

### *attr* Result.**service**

> [Source: ../../../../models.py @ line 143](../../../../models.py#L143)

> Type: `Translator`

The service which returned the result

### *attr* Result.**source**

> [Source: ../../../../models.py @ line 146](../../../../models.py#L146)

> Type: `str`

The source text

### *attr* Result.**source_lang**

> [Source: ../../../../models.py @ line 148](../../../../models.py#L148)

> Type: `Language`

The source text's language

### *attr* Result.**raw**

> [Source: ../../../../models.py @ line 158](../../../../models.py#L158)

> Type: `Optional`

The raw response returned by the service.  
Note: This is very dependent on the service used.  
Refer to the service documentation to learn how to use this object.

### *property* Result.**attributes**

> [Source: ../../../../models.py @ line 217-267](../../../../models.py#L217-L267)

The different attributes on the dataclass

#### Parameters

- **cls**


#### Returns

- `list`

### *property* Result.**exported**

> [Source: ../../../../models.py @ line 270-281](../../../../models.py#L270-L281)

A dictionary version of the dataclass which can be exposed to the public

#### Returns

- `dict`

## *class* **TranslationResult**

> [Source: ../../../../models.py @ line 291-329](../../../../models.py#L291-L329)

Holds the result of a regular translation

### *attr* TranslationResult.**dest_lang**

> [Source: ../../../../models.py @ line 296](../../../../models.py#L296)

> Type: `Language`

The result's language

### *attr* TranslationResult.**translation**

> [Source: ../../../../models.py @ line 299](../../../../models.py#L299)

> Type: `str`

The translation result

### *property* TranslationResult.**alternatives**

> [Source: ../../../../models.py @ line 306-310](../../../../models.py#L306-L310)

Returns the alternative translations associated

## *const* **TRANSLATION_TEST**

> [Source: ../../../../models.py @ line 332](../../../../models.py#L332)

## *class* **TransliterationResult**

> [Source: ../../../../models.py @ line 344-371](../../../../models.py#L344-L371)

Holds the result of a transliteration

### *attr* TransliterationResult.**transliteration**

> [Source: ../../../../models.py @ line 348](../../../../models.py#L348)

> Type: `str`

The transliteration result

### *attr* TransliterationResult.**dest_lang**

> [Source: ../../../../models.py @ line 351](../../../../models.py#L351)

> Type: `Language`

The result's language

## *const* **TRANSLITERATION_TEST**

> [Source: ../../../../models.py @ line 374](../../../../models.py#L374)

## *class* **SpellcheckResult**

> [Source: ../../../../models.py @ line 384-410](../../../../models.py#L384-L410)

Holds a spellchecking result

### *attr* SpellcheckResult.**rich**

> [Source: ../../../../models.py @ line 389](../../../../models.py#L389)

### *attr* SpellcheckResult.**source_lang**

> [Source: ../../../../models.py @ line 391](../../../../models.py#L391)

> Type: `Language`

The source text's language

### *attr* SpellcheckResult.**corrected**

> [Source: ../../../../models.py @ line 393](../../../../models.py#L393)

> Type: `str`

The corrected text

## *const* **SPELLCHECK_TEST**

> [Source: ../../../../models.py @ line 413](../../../../models.py#L413)

## *class* **SpellcheckMistake**

> [Source: ../../../../models.py @ line 422-435](../../../../models.py#L422-L435)

This holds a mistake made detected by the spellchecker

### *attr* SpellcheckMistake.**start**

> [Source: ../../../../models.py @ line 424](../../../../models.py#L424)

> Type: `int`

The beginning index of the part to correct in the original text

### *attr* SpellcheckMistake.**end**

> [Source: ../../../../models.py @ line 426](../../../../models.py#L426)

> Type: `int`

The ending index of the part to correct in the original text

### *attr* SpellcheckMistake.**corrected**

> [Source: ../../../../models.py @ line 428](../../../../models.py#L428)

> Type: `str`

The corrected part

### *attr* SpellcheckMistake.**message**

> [Source: ../../../../models.py @ line 431](../../../../models.py#L431)

> Type: `Optional`

A message explaining what happened

### *attr* SpellcheckMistake.**rule**

> [Source: ../../../../models.py @ line 434](../../../../models.py#L434)

> Type: `Optional`

A string which identifies the rule associated with the mistake made

## *class* **RichSpellcheckResult**

> [Source: ../../../../models.py @ line 441-601](../../../../models.py#L441-L601)

Holds a rich spellchecking result

### *attr* RichSpellcheckResult.**rich**

> [Source: ../../../../models.py @ line 447](../../../../models.py#L447)

### *attr* RichSpellcheckResult.**source_lang**

> [Source: ../../../../models.py @ line 449](../../../../models.py#L449)

> Type: `Language`

The source text's language

### *attr* RichSpellcheckResult.**mistakes**

> [Source: ../../../../models.py @ line 451](../../../../models.py#L451)

> Type: `List`

The different mistakes made

### *property* RichSpellcheckResult.**corrected**

> [Source: ../../../../models.py @ line 455-463](../../../../models.py#L455-L463)

The corrected text

#### Returns

- `str`

## *const* **RICH_SPELLCHECK_TEST**

> [Source: ../../../../models.py @ line 604](../../../../models.py#L604)

## *class* **LanguageResult**

> [Source: ../../../../models.py @ line 618-628](../../../../models.py#L618-L628)

Holds the language of the given text

## *const* **LANGUAGE_TEST**

> [Source: ../../../../models.py @ line 631](../../../../models.py#L631)

## *class* **ExampleResult**

> [Source: ../../../../models.py @ line 635-725](../../../../models.py#L635-L725)

Holds an example sentence where the given word is used.

### *attr* ExampleResult.**example**

> [Source: ../../../../models.py @ line 641](../../../../models.py#L641)

> Type: `str`

The example

### *attr* ExampleResult.**reference**

> [Source: ../../../../models.py @ line 644](../../../../models.py#L644)

> Type: `Optional`

Where the example comes from (i.e a book or a the person who said it if it's a quote)

### *property* ExampleResult.**position**

> [Source: ../../../../models.py @ line 648-655](../../../../models.py#L648-L655)

The first position of the word in the example

#### Returns

- `NoneType`

- `int`

### *property* ExampleResult.**positions**

> [Source: ../../../../models.py @ line 658-690](../../../../models.py#L658-L690)

The positions of the word in the example

#### Returns

- `list[int]`
    - A list of positions of the word in the example

## *const* **EXAMPLE_TEST**

> [Source: ../../../../models.py @ line 728](../../../../models.py#L728)

## *class* **DictionaryResult**

> [Source: ../../../../models.py @ line 737-752](../../../../models.py#L737-L752)

Holds the meaning of the given text

### *attr* DictionaryResult.**rich**

> [Source: ../../../../models.py @ line 743](../../../../models.py#L743)

### *attr* DictionaryResult.**meaning**

> [Source: ../../../../models.py @ line 745](../../../../models.py#L745)

> Type: `str`

The meaning of the text

## *const* **DICTIONARY_TEST**

> [Source: ../../../../models.py @ line 755](../../../../models.py#L755)

## *class* **EtymologicalNode**

> [Source: ../../../../models.py @ line 764-791](../../../../models.py#L764-L791)

The node of an etymological tree

### *attr* EtymologicalNode.**origin**

> [Source: ../../../../models.py @ line 766](../../../../models.py#L766)

> Type: `str`

The origin name (i.e 'Latin')

### *attr* EtymologicalNode.**source**

> [Source: ../../../../models.py @ line 769](../../../../models.py#L769)

> Type: `Optional`

The original way of writing it

### *attr* EtymologicalNode.**year**

> [Source: ../../../../models.py @ line 771](../../../../models.py#L771)

> Type: `Optional`

The year of origin

## *class* **RichDictionaryResult**

> [Source: ../../../../models.py @ line 795-904](../../../../models.py#L795-L904)

Holds more (optional) information than the regular `DictionaryResult`

### *attr* RichDictionaryResult.**rich**

> [Source: ../../../../models.py @ line 801](../../../../models.py#L801)

### *attr* RichDictionaryResult.**etymology**

> [Source: ../../../../models.py @ line 803](../../../../models.py#L803)

> Type: `List`

The etymological/origins tree of the given text  
Each element corresponds to a node in the tree of origins for the given text

#### Examples

##### Example 1

`Node1 (Greek) -> Node2 (Latin) -> Node3 (French) -> Node4 (Ancient English) -> Current Word`

### *attr* RichDictionaryResult.**gender**

> [Source: ../../../../models.py @ line 814](../../../../models.py#L814)

> Type: `Gender`

For languages which assign genders on words

#### Examples

##### Example 1

`chaîse (french; a chair) -> Gender.FEMALE`

### *attr* RichDictionaryResult.**pronunciation**

> [Source: ../../../../models.py @ line 823](../../../../models.py#L823)

> Type: `Optional`

A way of pronouncing the text

### *attr* RichDictionaryResult.**type**

> [Source: ../../../../models.py @ line 826](../../../../models.py#L826)

> Type: `WordClass`

The part of speech of the text

### *attr* RichDictionaryResult.**synonyms**

> [Source: ../../../../models.py @ line 829](../../../../models.py#L829)

> Type: `List`

### *attr* RichDictionaryResult.**antonyms**

> [Source: ../../../../models.py @ line 830](../../../../models.py#L830)

> Type: `List`

## *const* **RICH_DICTIONARY_TEST**

> [Source: ../../../../models.py @ line 907](../../../../models.py#L907)

## *class* **TextToSpeechResult**

> [Source: ../../../../models.py @ line 922-988](../../../../models.py#L922-L988)

Holds the text to speech results

### *attr* TextToSpeechResult.**result**

> [Source: ../../../../models.py @ line 928](../../../../models.py#L928)

> Type: `bytes`

Text to speech result

### *attr* TextToSpeechResult.**speed**

> [Source: ../../../../models.py @ line 930](../../../../models.py#L930)

> Type: `int`

Speed of the text to speech result

### *attr* TextToSpeechResult.**gender**

> [Source: ../../../../models.py @ line 932](../../../../models.py#L932)

> Type: `Gender`

Gender of the 'person' saying the text

### *property* TextToSpeechResult.**type**

> [Source: ../../../../models.py @ line 936-938](../../../../models.py#L936-L938)

Returns the type of audio file

### *property* TextToSpeechResult.**mime_type**

> [Source: ../../../../models.py @ line 941-953](../../../../models.py#L941-L953)

Returns the MIME type of the audio file

#### Returns

- `Optional[str]`
    - The MIME type of the audio file

### *property* TextToSpeechResult.**extension**

> [Source: ../../../../models.py @ line 956-968](../../../../models.py#L956-L968)

Returns the audio file extension

#### Returns

- `Optional[str]`
    - The MIME type of the audio file

### *func* TextToSpeechResult.**write_to_file**

> [Source: ../../../../models.py @ line 970-988](../../../../models.py#L970-L988)

Writes the spoken text to a file.

#### Parameters

- **file**: `BinaryIO`, `IO`, `Path`, `str`
  - The output path or object


- **replace_ext**: `bool`
  - Default Value: `True`
  - If we need to change the extension of the file to match the right file type


## *class* **HTMLTranslationNode**

> [Source: ../../../../models.py @ line 992-1029](../../../../models.py#L992-L1029)

A translation node, containing the DOM element and its translation result

### *attr* HTMLTranslationNode.**node**

> [Source: ../../../../models.py @ line 996](../../../../models.py#L996)

> Type: `bs4.NavigableString`

### *attr* HTMLTranslationNode.**result**

> [Source: ../../../../models.py @ line 997](../../../../models.py#L997)

> Type: `Optional`

### *property* HTMLTranslationNode.**position**

> [Source: ../../../../models.py @ line 1000-1020](../../../../models.py#L1000-L1020)

The position of the node in the HTML

#### Returns

- `int`

### *property* HTMLTranslationNode.**exported**

> [Source: ../../../../models.py @ line 1023-1029](../../../../models.py#L1023-L1029)

The exported dictionary

#### Returns

- `dict`

## *class* **HTMLTranslationResult**

> [Source: ../../../../models.py @ line 1033-1052](../../../../models.py#L1033-L1052)

Holds an HTML translation result

### *attr* HTMLTranslationResult.**result**

> [Source: ../../../../models.py @ line 1037](../../../../models.py#L1037)

> Type: `str`

### *attr* HTMLTranslationResult.**soup**

> [Source: ../../../../models.py @ line 1038](../../../../models.py#L1038)

> Type: `bs4.BeautifulSoup`

### *attr* HTMLTranslationResult.**nodes**

> [Source: ../../../../models.py @ line 1039](../../../../models.py#L1039)

> Type: `List`

### *property* HTMLTranslationResult.**exported**

> [Source: ../../../../models.py @ line 1048-1052](../../../../models.py#L1048-L1052)

#### Returns

- `dict`
