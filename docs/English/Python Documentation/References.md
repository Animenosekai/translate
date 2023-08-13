# translatepy's Python Reference

## The `Translate` class

The `Translate` class lets you group and use multiple translators at the same time, to increase your chance on getting an answer.

### Arguments

It takes three *optional* arguments :

- the `services_list` argument, which lets you define the different `Translator` objects to use
- the `request` argument, which lets you provide your own translatepy `Request` class to use, which will be used to make HTP requests
- the `fast` argument, to enable [*fast* mode]()

### Methods

Here are the supported methods :

- translate: To translate things
- translate_html : To translate HTML snippets
- transliterate: To transliterate things
- spellcheck: To check the spelling of a text
- language: To get the language of a text
- example: To get a list of examples of a word
- dictionary: To get a list of alternative translations
- text_to_speech: To get an audio file containing the speech version of the given text

```python
>>> from translatepy import Translator
>>> translator = Translator()
>>> translator.translate("Hello", "French")
TranslationResult(service=Yandex, source=Hello, source_language=auto, destination_language=French, result=Bonjour)
>>> translator.language("こんにちは")
LanguageResult(service=Yandex, source=こんにちは, result=Language(jpn))
```

## Translators

There is a list of built-in translators to use with translatepy, but you can also use any object inheriting from `translatepy.translators.base.BaseTranslator`

You can use each translator separately, as well as including them into the previously defined `Translate` class.

```python
>>> from translatepy.translators.google import GoogleTranslate
>>> gtranslate = GoogleTranslate()
>>> gtranslate.translate("Hello World", "Japanese")
TranslationResult(service=Google, source=Hello World, source_language=eng, destination_language=jpn, result=こんにちは世界)
```

And some translators have their own parameters:

```python
>>> gtranslate_china = GoogleTranslate(service_url="translate.google.cn")
>>> gtranslate_china.translate("Hello World", "Japanese")
TranslationResult(service=Google, source=Hello World, source_language=eng, destination_language=jpn, result=こんにちは世界)

# it can even be used by translatepy.Translator
>>> from translatepy import Translator
>>> t = Translator([gtranslate_china])
>>> t.translate("Hello World", "Japanese")
TranslationResult(service=Google, source=Hello World, source_language=eng, destination_language=jpn, result=こんにちは世界)
```

## The `Language` class

The language class contains lots of information about a language.

You need to pass the language name or code to the class initialization:

```python
>>> from translatepy import Language
>>> Language("French")
# Returns a Language class with the "fra" language
>>> Language("en")
# Returns a Language class with the "eng" language
>>> Language("eng")
# Returns a Language class with the "eng" language
>>> Language("日本語")
# Returns a Language class with the "jpn" language
```

> Let translatepy understand which language you want to use !

### ISO Specifications

The `Language` class contains both the ISO 639-1 Alpha-2 language code and the ISO 639-2 Alpha-3 language code of a given language.

```python
>>> Language("English").alpha2 # ISO 639-1 (alpha 2), nullable
'en'
>>> Language("English").alpha3 # ISO 639-3 (alpha 3)
'eng'
>>> Language("English").alpha3b # ISO 639-2B, nullable
'eng'
>>> Language("English").alpha3t # ISO 639-2T, nullable
'eng'
```

Each available language has its own ID, coming most of the time from the Alpha-3 Language Code, but which can be a unique translatepy ID (`'auto'` or `'emj'` for example)

```python
>>> Language("French").id
'fra'
>>> Language("Emoji").id
'emj'
>>> Language("自動").id
'auto'
```

### Language name translation

It also contains the language name for a lot of languages:

```python
>>> Language("Français").in_foreign_languages.get("ja", None) # an alpha-2 code needs to be passed in, also make sure to have a fallback such as None here because not all of the languages had been translated.
'フランス語'
```

All languages which have a `alpha2` code are assured to have at least their translation in the following languages:

```python
to = ['af', 'am', 'ar', 'az', 'be', 'bg', 'bn', 'bs', 'ca', 'ceb', 'co', 'cs', 'cy', 'da', 'de', 'el', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy', 'ga', 'gd', 'gl', 'gu', 'ha', 'haw', 'hi', 'hmn', 'hr', 'ht', 'hu', 'hy', 'id', 'ig', 'is', 'it', 'he', 'ja', 'jv', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'ky', 'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'no', 'ny', 'or', 'pa', 'pl', 'ps', 'pt', 'ro', 'ru', 'sd', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sq', 'sr', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tl', 'tr', 'ug', 'uk', 'ur', 'uz', 'vi', 'xh', 'yi', 'yo', 'zh', 'zu']
```

The other ones may or may not have a translation in more or less languages.

### Input string similarity

The `Language` class also contains the "similarity" attribute which gives back a number between 0 and 100 showing the similarity of the input string with the database data:

```python
>>> round(Language("French").similarity, 2)
100.0
>>> Language("Englesh").similarity
94.86832980505137
```

<details>
    <summary>Note</summary>
    <p>Only the languages which have an <i>alpha2</i> language code and are of type <i>Living</i> or <i>Ancient</i> are vectorized and will be used in the similarity search.</p>
</details>
<br>

### Extra

Each language also contains an 'extra' attribute with their type *(nullable)* and their scope *(nullable)*.

```python
>>> Language("French").extra
LanguageExtra(type=LanguageType(Living), scope=LanguageScope(Individual))
>>> Language("Latin").extra.type
LanguageType(Ancient)
```

### Exception

A `translatepy.exceptions.UnknownLanguage` exception is raised if the given language is unknown.

This exception contains the most similar language along with its similarity:

```python
>>> from translatepy import Language
>>> from translatepy.exceptions import UnknownLanguage
>>> try:
...     language = Language("中国")
... except UnknownLanguage as error:
...     print("The similarity seemed to be too low for translatepy to accept it as a correct language name")
...     print("The language found is:", error.guessed_language)
...     print("Its similarity from the passed input is:", str(error.similarity))
```

> If you find that the default threshold given to the language search is too low, you can always change it by passing the `threshold` parameter when initializing a `Language`:

```python
>>> from translatepy import Language
>>> Language("国語")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/animenosekai/Documents/Coding/Projects/translate/translatepy/language.py", line 106, in __init__
    raise UnknownLanguage(_search_result, self.similarity, raising_message)
translatepy.exceptions.UnknownLanguage: Couldn't recognize the given language (中国)
Did you mean: 中国語 (Similarity: 81.65%)?
>>> Language("中国", threshold=80)
Language(zho)
```

## Results

All of the methods should have its own result class (defined in [translatepy/models.py](translatepy/models.py)) which all have at least the service, source, result attributes and a `as_json` method to convert everything into a JSON String.

## Errors

All of the `translatepy` errors are inherited from `translatepy.exceptions.TranslatepyException` so that you can easily catch a `translatepy` error.

```python
>>> from translatepy import Translator
>>> from translatepy.exceptions import TranslatepyException, UnknownLanguage
>>> t = Translator()
>>> def translate(text, dest):
...     try:
...         result = t.translate(text, destination_language=dest)
        except UnknownLanguage as err:
            print("An error occured while searching for the language you passed in")
            print("Similarity:", round(err.similarity), "%")
            return
        except TranslatepyException:
            print("An error occured while translating with translatepy")
            return
        except Exception:
            print("An unknown error occured")
            return
...     # do something with the result...
...     
```
