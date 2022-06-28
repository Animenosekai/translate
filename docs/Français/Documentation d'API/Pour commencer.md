
# Référence d'API pour translatepy

Bienvenue sur la référence d'API pour translatepy.

## Globalité

### Format de réponse

Généralement, les réponses JSON seront formattez comme suit (même lorsque des erreurs critiques sont encontrées)

```json
{
    "success": true,
    "message": "Ça marche!",
    "error": null,
    "data": {}
}
```

| Champ        | Description                                      | Peut être `null` |
| ------------ | ------------------------------------------------ | ---------------- |
| `success`    | Si la requête est un succès ou pas               | False            |
| `message`    | Un message qui décrit ce qu'il s'est passé       | True             |
| `error`      | Le nom de l'erreur si il y en a une              | True             |
| `data`       | Des données supplémentaires, les informations demandées | False            |

### Erreurs

De multiples erreurs peuvent survenir, que ce soit du côté client (au niveau de la requête) ou du côté du serveur.

Les erreurs spécifiques sont documentés dans chaque *Endpoint* mais celles-ci sont celles qui peuvent survenir sur n'importe quel endpoint :

| Erreur                      | Description                                                                                                     | Code  |
| --------------------------- | --------------------------------------------------------------------------------------------------------------- | ----- |
| `SERVER_ERROR`              | Quand une erreur survient sur translatepy en traitant la requête.                                                    | 500   |
| `MISSING_CONTEXT`           | Quand dans le code vous essayez d'accéder à une ressource seulement disponible dans un contexte Nasse (pendant une requête) mais que vous n'êtes pas dans un contexte Nasse.       | 500   |
| `INTERNAL_SERVER_ERROR`     | Quand une erreur critique survient sur le système                                                               | 500   |
| `METHOD_NOT_ALLOWED`        | Quand vous faites une requête avec le mauvaise méthode HTTP                                                     | 405   |
| `CLIENT_ERROR`              | Quand quelque chose manque où n'est pas bon avec la requête                                                     | 400   |
| `MISSING_VALUE`             | Quand quelque chose manque à la requête                                                                         | 400   |
| `MISSING_PARAM`             | Quand un paramètre manque à la requête                                                                          | 400   |
| `MISSING_DYNAMIC`           | Quand une valeur dynamique de l'URL manque                                                                      | 400   |
| `MISSING_HEADER`            | Quand un en-tête manque à la requête                                                                            | 400   |
| `MISSING_COOKIE`            | Quand un cookie manque à la requête                                                                             | 400   |
| `AUTH_ERROR`                | Quand une erreur d'authentification survient                                                                    | 403   |

### Requêtes authentifiées

Quand un utilisateur doit être connecter, l'en-tête "Authorization" doit être définie avec le token de connexion communiqué lorsqu'il s'est connecté.

Vous pouvez aussi utiliser le paramètre "translatepy_token" ou le cookie "__translatepy_token" mais ceux-ci ne vont pas être priorisé.

Si la règle d'authentification de l'*endpoint* est défini comme "seulement vérifié", le compte ne doit pas être cherché dans la base de donnée mais la forme du token ou des informations comprises à l'intérieur peuvent être vérifiées.

### Mode de développement

Lorsque le mode de développement est activé (`-d` ou `--debug`), de multiples informations sont renvoyées dans la section `debug` des réponses et le niveau `DEBUG` de logging est sélectioné sur le serveurr.

La section 'debug' est disponible sur tous type d'erreur, sauf celles qui sont renvoyées par Flask de manière interne (comme `INTERNAL_SERVER_ERROR`, `METHOD_NOT_ALLOWED`, etc.). En effet, celles-ci doivent modifier le moins possible la requête pour ne pas se retrouver avec une autre erreur qui pourrait survenir)

Le champ "call_stack" est activé seulement quand il y a le paramètre `call_stack` qui est envoyé avec la requête.

```json
{
    "success": true,
    "message": "Nous n'avons pas pu satisfaire la requête",
    "error": null,
    "data": {
        "username": "Animenosekai"
    },
    "debug": {
        "time": {
            "global": 0.036757,
            "verification": 0.033558,
            "authentication": 0.003031,
            "processing": 4.9e-05,
            "formatting": 0.0001
        },
        "ip": "127.0.0.1",
        "headers": {
            "Host": "api.translatepy.com",
            "Connection": "close",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "fr-fr",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
        },
        "values": {},
        "domain": "api.translatepy.com",
        "logs": [
            "1636562693.036563｜[INFO] [nasse.receive.Receive.__call__] → Incoming GET request to /account/name from 127.0.0.1",
            "1636562693.070008｜[ERROR] [nasse.exceptions.base.MissingToken.__init__] An authentication token is missing from the request"
        ],
        "call_stack": [
            "pass the 'call_stack' parameter to get the call stack"
        ]
    }
}
```

## Index

- [Language](./Sections/Language.md#language)
  - [Language Details](./Sections/Language.md#language-details)
  - [Language Search](./Sections/Language.md#language-search)
  - [Language Details (dynamic)](./Sections/Language.md#language-details-dynamic)
- [Stars](./Sections/Stars.md#stars)
  - [Stars](./Sections/Stars.md#stars-1)
  - [Translation Star](./Sections/Stars.md#translation-star)
- [Stats](./Sections/Stats.md#stats)
  - [Timings Stats](./Sections/Stats.md#timings-stats)
  - [Erros Stats](./Sections/Stats.md#erros-stats)
- [Translation](./Sections/Translation.md#translation)
  - [Translate](./Sections/Translation.md#translate)
  - [Translation Stream](./Sections/Translation.md#translation-stream)
  - [Translate HTML](./Sections/Translation.md#translate-html)
  - [Transliterate](./Sections/Translation.md#transliterate)
  - [Spellcheck](./Sections/Translation.md#spellcheck)
  - [Language](./Sections/Translation.md#language-1)
  - [Text to Speech](./Sections/Translation.md#text-to-speech)
