# Objects

This file defines the different objects which can be returned to the client.

## Language

The `Language` object represents a `translatepy.Language` object, which is a class holding information about any Language.

### Example

```json
{
    "id": "eng",
    "similarity": 100,
    "alpha2": "en",
    "alpha3b": "eng",
    "alpha3t": "eng",
    "alpha3": "eng",
    "name": "English",
    "inForeignLanguages": {
        "af": "Engels",
        "sq": "Anglisht",
        "am": "እንግሊዝኛ",
        "ar": "الإنجليزية",
        "hy": "Անգլերեն",
        "...": "...",
        "zh": "英语",
        "he": "אנגלית",
        "jv": "Inggris",
        "en": "English"
    },
    "extra": {
        "type": "Living",
        "scope": "Individual"
    }
}   
```

### Attributes

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `id`         | The ID of the language           | string | No        |
| `similarity` | The string similarity of the input string with the one in the database | float      | No      |
| `alpha2`     | The ISO 639-1 (alpha 2) code     | string | Yes       |
| `alpha3b`    | The ISO 639-2B code              | string | Yes       |
| `alpha3t`    | The ISO 639-2T code              | string | Yes       |
| `alpha3`     | The ISO 639-3 code               | string | No        |
| `name`       | The English name of the language | string | No        |
| `inForeignLanguages`  | If available, the translation of the language name in different languages | object[alpha2Code(string): string] | No        |
| `extra`      | Extra information on the language | [`LanguageExtra`](#languageextra) | No        |

## LanguageExtra

The `LanguageExtra` object is an object holding extra information about a `Language`.

### Example

```json
{
    "type": "Living",
    "scope": "Individual"
}
```

### Attributes

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `type`       | The type of the language         | [`LanguageExtraType`](#languageextratype) | Yes        |
| `scope`      | The scope of the language        | [`LanguageExtraScope`](#languageextrascope)  | Yes      |

### LanguageExtraType

This is a string enum which can be any of the following strings :

```typescript
"Ancient" | "Constructed" | "Extinct" | "Historical" | "Living" | "Special"
```

### LanguageExtraScope

This is a string enum which can be any of the following strings :

```typescript
"Individual" | "Macrolanguage" | "Special"
```

## StarredTranslation

This represents a starred translation.

### Attributes

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source`     | This is the source text          | string | No        |
| `result`     | This is the resulting text       | string | No        |
| `language`   | This is the translation language data       | [`StarredTranslationLanguage`](#starredtranslationlanguage) | No        |
| `users`      | This is the number of users who starred the translation       | int | No        |

### Example

```json
{
    "source": "Hello world",
    "result": "ハローワールド",
    "language": {
        "source": "eng",
        "dest": "jpn"
    },
    "users": 35
}
```

### StarredTranslationLanguage

This is the language data for the starred translation.

#### Attributes

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source`     | This is the source language      | string | No        |
| `dest`       | This is the destination language | string | No        |

#### Example

```json
{
    "source": "eng",
    "dest": "jpn"
}
```
