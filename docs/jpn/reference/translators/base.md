# *module* **base**

> [Source: ../../../../translatepy/translators/base.py @ line 0](../../../../translatepy/translators/base.py#L0)

translators/base.py  
Implements the Base Translator class

## *const* **C**

> [Source: ../../../../translatepy/translators/base.py @ line 25](../../../../translatepy/translators/base.py#L25)

## *const* **R**

> [Source: ../../../../translatepy/translators/base.py @ line 26](../../../../translatepy/translators/base.py#L26)

## *const* **HTMLType**

> [Source: ../../../../translatepy/translators/base.py @ line 27](../../../../translatepy/translators/base.py#L27)

## *class* **LazyIterable**

> [Source: ../../../../translatepy/translators/base.py @ line 30-69](../../../../translatepy/translators/base.py#L30-L69)

An object which can be iterated through, even multiple times, but lazy loads the results.

### Raises

- `IndexError`

## *const* **T**

> [Source: ../../../../translatepy/translators/base.py @ line 73](../../../../translatepy/translators/base.py#L73)

## *class* **BaseTranslateException**

> [Source: ../../../../translatepy/translators/base.py @ line 79-105](../../../../translatepy/translators/base.py#L79-L105)

A translator exception, indicating a problem which occured during translation

### *attr* BaseTranslateException.**error_codes**

> [Source: ../../../../translatepy/translators/base.py @ line 83](../../../../translatepy/translators/base.py#L83)

## *class* **Flag**

> [Source: ../../../../translatepy/translators/base.py @ line 108-112](../../../../translatepy/translators/base.py#L108-L112)

Defines a set of internal flags the handlers can send to the validator

### *attr* Flag.**MULTIPLE_RESULTS**

> [Source: ../../../../translatepy/translators/base.py @ line 112](../../../../translatepy/translators/base.py#L112)

## *class* **BaseTranslator**

> [Source: ../../../../translatepy/translators/base.py @ line 115-1293](../../../../translatepy/translators/base.py#L115-L1293)

The core of translatepy  
This defines a "Translator" instance, which is the gateway between the translator logic and translatepy

### Raises

- `ValueError`

- `exc`

- `exceptions.UnsupportedLanguage`

- `exceptions.UnsupportedMethod`

### *func* BaseTranslator.**translate**

> [Source: ../../../../translatepy/translators/base.py @ line 307-324](../../../../translatepy/translators/base.py#L307-L324)

Translates the given `text` into the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `Language`, `str`
  - The language to translate to


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `str`
  - The text to translate


#### Returns

- `TranslationResult`
    - The result of the translation

- `models.TranslationResult`

### *func* BaseTranslator.**translate**

> [Source: ../../../../translatepy/translators/base.py @ line 327-346](../../../../translatepy/translators/base.py#L327-L346)

Translates all of the elements in `text` into the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `Language`, `str`
  - The language to translate to


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `Iterable[str]`, `Iterable`
  - A list of texts you want to translate


#### Returns

- `LazyIterable`

- `LazyIterable[TranslationResult]`
    - An iterable which holds the different translations

> **Note**
> aka "Bulk Translation"

### *func* BaseTranslator.**translate**

> [Source: ../../../../translatepy/translators/base.py @ line 351-393](../../../../translatepy/translators/base.py#L351-L393)

Translates `text` into the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `str`


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `str`
  - Default Value: `auto`


- **text**: `Iterable`, `str`


#### Returns

- `ForwardRef('LazyIterable')`

- `ForwardRef('models.TranslationResult')`

> **Note**
> Refer to the overloaded methods docstrings for more information.

### *func* BaseTranslator.**translate_html**

> [Source: ../../../../translatepy/translators/base.py @ line 420-451](../../../../translatepy/translators/base.py#L420-L451)

Translates the given `html` into the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `Language`, `str`
  - The language to translate to


- **html**: `BeautifulSoup`, `HTMLType`, `PageElement`, `Tag`, `str`
  - The HTML you want to translate


- **kwargs**


- **parser**: `str`
  - Default Value: `html.parser`
  - The BeautifulSoup parser to use to parse the HTML


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from each node in `html`


- **strict**: `bool`
  - Default Value: `True`
  - If the function should raise something is one of the nodes couldn't be translated.
If `False`, the node will be left as is and the `result` part will be `None`


- **threads_limit**: `int`
  - Default Value: `100`
  - The maximum number of threads to spawn at a time to translate


#### Returns

- `HTMLTranslationResult`
    - Holds the HTML translation result

- `models.HTMLTranslationResult`

### *func* BaseTranslator.**translate_html**

> [Source: ../../../../translatepy/translators/base.py @ line 454-486](../../../../translatepy/translators/base.py#L454-L486)

Translates all of the elements in `html` into the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `Language`, `str`
  - The language to translate to


- **html**: `Iterable`
  - A list of HTML you want to translate


- **kwargs**


- **parser**: `str`
  - Default Value: `html.parser`
  - The BeautifulSoup parser to use to parse the HTML


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from each node in `html`


- **strict**: `bool`
  - Default Value: `True`
  - If the function should raise something is one of the nodes couldn't be translated.
If `False`, the node will be left as is and the `result` part will be `None`


- **threads_limit**: `int`
  - Default Value: `100`
  - The maximum number of threads to spawn at a time to translate


#### Returns

- `LazyIterable`

- `LazyIterable[HTMLTranslationResult]`
    - Holds the HTML translation result

> **Note**
> aka "Bulk Translation"

### *func* BaseTranslator.**translate_html**

> [Source: ../../../../translatepy/translators/base.py @ line 489-565](../../../../translatepy/translators/base.py#L489-L565)

Translates `html` into the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `str`


- **html**: `ForwardRef('HTMLType')`, `Iterable`


- **kwargs**


- **parser**: `str`
  - Default Value: `html.parser`


- **source_lang**: `ForwardRef('Language')`, `str`
  - Default Value: `auto`


- **strict**: `bool`
  - Default Value: `True`


- **threads_limit**: `int`
  - Default Value: `100`


#### Returns

- `ForwardRef('LazyIterable')`

- `ForwardRef('models.HTMLTranslationResult')`

#### Raises

- `exc`

> **Note**
> Refer to the overloaded methods docstrings for more information.

### *func* BaseTranslator.**alternatives**

> [Source: ../../../../translatepy/translators/base.py @ line 573-586](../../../../translatepy/translators/base.py#L573-L586)

Returns the different alternative translations available for a given previous translation.

#### Parameters

- **args**


- **kwargs**


- **translation**: `TranslationResult`, `models.TranslationResult`
  - The previous translation


#### Returns

- `list`

- `list[TranslationResult]`
    - The list of other translations a word might have

### *func* BaseTranslator.**alternatives**

> [Source: ../../../../translatepy/translators/base.py @ line 589-602](../../../../translatepy/translators/base.py#L589-L602)

Returns the different alternative translations available for all of the given translations.

#### Parameters

- **args**


- **kwargs**


- **translation**: `Iterable[TranslationResult]`, `Iterable`
  - All of the previous translation


#### Returns

- `LazyIterable`

- `LazyIterable[list[TranslationResult]]`
    - All of the other translations

### *func* BaseTranslator.**alternatives**

> [Source: ../../../../translatepy/translators/base.py @ line 606-632](../../../../translatepy/translators/base.py#L606-L632)

Returns the different alternative translations available for the given `translation`.

#### Parameters

- **args**


- **kwargs**


- **translation**: `models.TranslationResult`


#### Returns

- `ForwardRef('LazyIterable')`

- `list`

> **Note**
> Refer to the overloaded methods docstrings for more information.

### *func* BaseTranslator.**transliterate**

> [Source: ../../../../translatepy/translators/base.py @ line 664-681](../../../../translatepy/translators/base.py#L664-L681)

Transliterates the given `text` into the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `Language`, `str`
  - The language to translate to


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `str`
  - The text to transliterate


#### Returns

- `TransliterationResult`
    - The result of the transliteration

- `models.TransliterationResult`

### *func* BaseTranslator.**transliterate**

> [Source: ../../../../translatepy/translators/base.py @ line 684-701](../../../../translatepy/translators/base.py#L684-L701)

Transliterates all of the given `text` to the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `Language`, `str`
  - The language to translate to


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `Iterable[str]`, `Iterable`
  - The texts to transliterate


#### Returns

- `LazyIterable`

- `LazyIterable[TransliterationResult]`
    - An iterable which contains the transliterations

### *func* BaseTranslator.**transliterate**

> [Source: ../../../../translatepy/translators/base.py @ line 704-750](../../../../translatepy/translators/base.py#L704-L750)

Transliterates the given `text` to the given `dest_lang`

#### Parameters

- **args**


- **dest_lang**: `ForwardRef('Language')`, `str`


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `str`
  - Default Value: `auto`


- **text**: `Iterable`, `str`


#### Returns

- `ForwardRef('LazyIterable')`

- `ForwardRef('models.TransliterationResult')`

> **Note**
> Refer to the overloaded methods docstrings for more information.

### *attr* BaseTranslator.**transliteration**

> [Source: ../../../../translatepy/translators/base.py @ line 753](../../../../translatepy/translators/base.py#L753)

### *func* BaseTranslator.**spellcheck**

> [Source: ../../../../translatepy/translators/base.py @ line 781-798](../../../../translatepy/translators/base.py#L781-L798)

Checks for spelling mistakes in the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `str`
  - The text to check for spelling mistakes


#### Returns

- `ForwardRef('models.RichSpellcheckResult')`

- `ForwardRef('models.SpellcheckResult')`

- `RichSpellcheckResult`
    - If supported by the translator, rich spellchecking results, which include the different mistakes made

- `SpellcheckResult`
    - The result of the spell check

### *func* BaseTranslator.**spellcheck**

> [Source: ../../../../translatepy/translators/base.py @ line 801-818](../../../../translatepy/translators/base.py#L801-L818)

Checks for spelling mistakes in all of the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `Iterable[str]`, `Iterable`
  - All of the texts to check for spelling mistakes


#### Returns

- `LazyIterable`

- `LazyIterable[RichSpellcheckResult]`
    - If supported by the translator, rich spellchecking results, which include the different mistakes made

- `LazyIterable[SpellcheckResult]`
    - The results of the spell checks

### *func* BaseTranslator.**spellcheck**

> [Source: ../../../../translatepy/translators/base.py @ line 822-853](../../../../translatepy/translators/base.py#L822-L853)

Checks for spelling mistakes in the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `str`
  - Default Value: `auto`


- **text**: `Iterable`, `str`


#### Returns

- `ForwardRef('LazyIterable')`

- `ForwardRef('models.RichSpellcheckResult')`

- `ForwardRef('models.SpellcheckResult')`

> **Note**
> Refer to the other overloaded methods for more information.

### *func* BaseTranslator.**language**

> [Source: ../../../../translatepy/translators/base.py @ line 881-894](../../../../translatepy/translators/base.py#L881-L894)

Returns the detected language for the given `text`

#### Parameters

- **args**


- **kwargs**


- **text**: `str`
  - The text to get the language for


#### Returns

- `LanguageResult`
    - The result of the language detection

- `models.LanguageResult`

### *func* BaseTranslator.**language**

> [Source: ../../../../translatepy/translators/base.py @ line 897-910](../../../../translatepy/translators/base.py#L897-L910)

Returns the detected language for all of the given `text`

#### Parameters

- **args**


- **kwargs**


- **text**: `Iterable[str]`, `Iterable`
  - The texts to get the language of


#### Returns

- `LazyIterable`

- `LazyIterable[LanguageResult]`
    - The results of the language detections

### *func* BaseTranslator.**language**

> [Source: ../../../../translatepy/translators/base.py @ line 914-936](../../../../translatepy/translators/base.py#L914-L936)

Returns the detected language for the given `text`

#### Parameters

- **args**


- **kwargs**


- **text**: `Iterable`, `str`


#### Returns

- `ForwardRef('LazyIterable')`

- `ForwardRef('models.LanguageResult')`

#### Raises

- `exceptions.UnsupportedLanguage`

> **Note**
> Refer to the other overloaded methods for more information.

### *func* BaseTranslator.**example**

> [Source: ../../../../translatepy/translators/base.py @ line 960-975](../../../../translatepy/translators/base.py#L960-L975)

Returns use cases for the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `str`
  - The text to get the example for


#### Returns

- `list`

- `list[ExampleResult]`
    - The examples

### *func* BaseTranslator.**example**

> [Source: ../../../../translatepy/translators/base.py @ line 978-993](../../../../translatepy/translators/base.py#L978-L993)

Returns use cases for all of the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `Iterable[str]`, `Iterable`
  - The texts to get the examples for


#### Returns

- `LazyIterable`

- `LazyIterable[list[ExampleResult]]`
    - All of the examples

### *func* BaseTranslator.**example**

> [Source: ../../../../translatepy/translators/base.py @ line 997-1031](../../../../translatepy/translators/base.py#L997-L1031)

Returns use cases for the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `str`
  - Default Value: `auto`


- **text**: `Iterable`, `str`


#### Returns

- `ForwardRef('LazyIterable')`

- `list`

> **Note**
> Refer to the other overloaded methods for more information.

### *func* BaseTranslator.**dictionary**

> [Source: ../../../../translatepy/translators/base.py @ line 1060-1077](../../../../translatepy/translators/base.py#L1060-L1077)

Returns the meaning for the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `str`
  - The text to get the meaning for


#### Returns

- `DictionaryResult`
    - The meaning of the given `text`

- `RichDictionaryResult`
    - If supported, a value which contains much more information on `text`

- `list`

### *func* BaseTranslator.**dictionary**

> [Source: ../../../../translatepy/translators/base.py @ line 1080-1097](../../../../translatepy/translators/base.py#L1080-L1097)

Returns the meaning for all of the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `Language`, `str`
  - Default Value: `auto`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **text**: `Iterable[str]`, `Iterable`
  - The texts to get the meanings for


#### Returns

- `LazyIterable`

- `LazyIterable[DictionaryResult]`
    - The meanings for all of the given `text`

- `LazyIterable[RichDictionaryResult]`
    - If supported, a value which contains much more information on all of the `text`

### *func* BaseTranslator.**dictionary**

> [Source: ../../../../translatepy/translators/base.py @ line 1101-1135](../../../../translatepy/translators/base.py#L1101-L1135)

Returns the meaning for the given `text`

#### Parameters

- **args**


- **kwargs**


- **source_lang**: `ForwardRef('Language')`, `str`
  - Default Value: `auto`


- **text**: `Iterable`, `str`


#### Returns

- `ForwardRef('LazyIterable')`

- `list`

> **Note**
> Refer to the other overloaded methods for more information.

### *func* BaseTranslator.**text_to_speech**

> [Source: ../../../../translatepy/translators/base.py @ line 1161-1180](../../../../translatepy/translators/base.py#L1161-L1180)

Returns the speech version of the given `text`

#### Parameters

- **gender**: `Gender`
  - The gender of the voice, if supported


- **source_lang**: `Language`, `str`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **speed**: `Speed`, `int`
  - The speed percentage of the text to speech result, if supported


- **text**: `str`
  - The text to get the speech for


#### Returns

- `TextToSpeechResult`
    - The text to speech result

### *func* BaseTranslator.**text_to_speech**

> [Source: ../../../../translatepy/translators/base.py @ line 1183-1202](../../../../translatepy/translators/base.py#L1183-L1202)

Returns the speech version for all of the given `text`

#### Parameters

- **gender**: `Gender`
  - The gender of the voice, if supported


- **source_lang**: `Language`, `str`
  - The language `text` is in. If "auto", the translator will try to infer the language from `text`


- **speed**: `Speed`, `int`
  - The speed percentage of the text to speech result, if supported


- **text**: `str`
  - The texts to get the speech versions for


#### Returns

- `LazyIterable[TextToSpeechResult]`
    - The text to speech results

### *func* BaseTranslator.**text_to_speech**

> [Source: ../../../../translatepy/translators/base.py @ line 1205-1241](../../../../translatepy/translators/base.py#L1205-L1241)

Returns the speech version of the given `text`

> **Note**
> Refer to the other overloaded methods for more information.

### *func* BaseTranslator.**clean_cache**

> [Source: ../../../../translatepy/translators/base.py @ line 1265-1274](../../../../translatepy/translators/base.py#L1265-L1274)

Cleans caches

#### Returns

- `None`
