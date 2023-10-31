# *module* **base**

> [Source: ../../../../translatepy/translators/base.py](../../../../translatepy/translators/base.py#L0)

translators/base.py  
Implements the Base Translator class

## *const* [**C**](../../../../translatepy/translators/base.py#L25)

## *const* [**R**](../../../../translatepy/translators/base.py#L26)

## *const* [**HTMLType**](../../../../translatepy/translators/base.py#L27)

## *class* [**LazyIterable**](../../../../translatepy/translators/base.py#L30-L69)

An object which can be iterated through, even multiple times, but lazy loads the results.

### Raises

- `IndexError`

## *const* [**T**](../../../../translatepy/translators/base.py#L73)

## *class* [**BaseTranslateException**](../../../../translatepy/translators/base.py#L79-L105)

A translator exception, indicating a problem which occured during translation

### *attr* [BaseTranslateException.**error_codes**](../../../../translatepy/translators/base.py#L83)

## *class* [**Flag**](../../../../translatepy/translators/base.py#L108-L112)

Defines a set of internal flags the handlers can send to the validator

### *attr* [Flag.**MULTIPLE_RESULTS**](../../../../translatepy/translators/base.py#L112)

## *class* [**BaseTranslator**](../../../../translatepy/translators/base.py#L115-L1293)

The core of translatepy  
This defines a "Translator" instance, which is the gateway between the translator logic and translatepy

### Raises

- `ValueError`

- `exc`

- `exceptions.UnsupportedLanguage`

- `exceptions.UnsupportedMethod`

### *func* [BaseTranslator.**translate**](../../../../translatepy/translators/base.py#L307-L324)

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

### *func* [BaseTranslator.**translate**](../../../../translatepy/translators/base.py#L327-L346)

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

### *func* [BaseTranslator.**translate**](../../../../translatepy/translators/base.py#L351-L393)

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

### *func* [BaseTranslator.**translate_html**](../../../../translatepy/translators/base.py#L420-L451)

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

### *func* [BaseTranslator.**translate_html**](../../../../translatepy/translators/base.py#L454-L486)

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

### *func* [BaseTranslator.**translate_html**](../../../../translatepy/translators/base.py#L489-L565)

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

### *func* [BaseTranslator.**alternatives**](../../../../translatepy/translators/base.py#L573-L586)

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

### *func* [BaseTranslator.**alternatives**](../../../../translatepy/translators/base.py#L589-L602)

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

### *func* [BaseTranslator.**alternatives**](../../../../translatepy/translators/base.py#L606-L632)

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

### *func* [BaseTranslator.**transliterate**](../../../../translatepy/translators/base.py#L664-L681)

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

### *func* [BaseTranslator.**transliterate**](../../../../translatepy/translators/base.py#L684-L701)

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

### *func* [BaseTranslator.**transliterate**](../../../../translatepy/translators/base.py#L704-L750)

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

### *attr* [BaseTranslator.**transliteration**](../../../../translatepy/translators/base.py#L753)

### *func* [BaseTranslator.**spellcheck**](../../../../translatepy/translators/base.py#L781-L798)

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

### *func* [BaseTranslator.**spellcheck**](../../../../translatepy/translators/base.py#L801-L818)

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

### *func* [BaseTranslator.**spellcheck**](../../../../translatepy/translators/base.py#L822-L853)

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

### *func* [BaseTranslator.**language**](../../../../translatepy/translators/base.py#L881-L894)

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

### *func* [BaseTranslator.**language**](../../../../translatepy/translators/base.py#L897-L910)

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

### *func* [BaseTranslator.**language**](../../../../translatepy/translators/base.py#L914-L936)

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

### *func* [BaseTranslator.**example**](../../../../translatepy/translators/base.py#L960-L975)

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

### *func* [BaseTranslator.**example**](../../../../translatepy/translators/base.py#L978-L993)

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

### *func* [BaseTranslator.**example**](../../../../translatepy/translators/base.py#L997-L1031)

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

### *func* [BaseTranslator.**dictionary**](../../../../translatepy/translators/base.py#L1060-L1077)

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

### *func* [BaseTranslator.**dictionary**](../../../../translatepy/translators/base.py#L1080-L1097)

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

### *func* [BaseTranslator.**dictionary**](../../../../translatepy/translators/base.py#L1101-L1135)

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

### *func* [BaseTranslator.**text_to_speech**](../../../../translatepy/translators/base.py#L1161-L1180)

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

### *func* [BaseTranslator.**text_to_speech**](../../../../translatepy/translators/base.py#L1183-L1202)

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

### *func* [BaseTranslator.**text_to_speech**](../../../../translatepy/translators/base.py#L1205-L1241)

Returns the speech version of the given `text`

> **Note**
> Refer to the other overloaded methods for more information.

### *func* [BaseTranslator.**clean_cache**](../../../../translatepy/translators/base.py#L1265-L1274)

Cleans caches

#### Returns

- `None`
