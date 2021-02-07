from translatepy.data.data import ALPHA3_TO_ALPHA2, LANGUAGES_CODE
from translatepy.data.data import LANGUAGES_NAME_TO_CODE_EN
from translatepy.data.data import LANGUAGES_NAME_TO_CODE_INTERNATIONAL
from translatepy.data.data import LANGUAGES_CODE_TO_NAME_EN
from translatepy.data.data import LANGUAGES_TO_INTERNATIONAL
from translatepy.data.data import ALPHA2_TO_ALPHA3
from translatepy.utils.similarity import language_search
from translatepy.models.exceptions import UnknownLanguage
import translatepy

LANGUAGES_CACHES = {}


class Language():
    def __init__(self, language) -> None:
        global LANGUAGES_CACHES

        self.language = str(language).lower()
        self._language = self.language
        if self._language in LANGUAGES_CACHES:
            self.language = LANGUAGES_CACHES[self._language]["l"]
            self.similarity = LANGUAGES_CACHES[self._language]["s"]
        else:
            if self.language not in LANGUAGES_CODE:
                result = ALPHA3_TO_ALPHA2.get(self.language, None)
                if result is None:
                    result = LANGUAGES_NAME_TO_CODE_EN.get(self.language, None)
                    if result is None:
                        result = LANGUAGES_NAME_TO_CODE_INTERNATIONAL.get(self.language, None)
                        if result is None:
                            name, lang, similarity = language_search(self.language)
                            if similarity > 0.95:
                                self.language = lang
                                self.similarity = similarity
                            else:
                                exception_message = "Couldn't recognize the given language (" + str(language) + ")\nDid you mean '" + name + "' (Similarity: " + str(round(similarity*100, 2)) + "%)?"
                                raise UnknownLanguage(exception_message)
                        else:
                            self.language = result
                            self.similarity = 1
                    else:
                        self.language = result
                        self.similarity = 1
                else:
                    self.language = result
                    self.similarity = 1
            else:
                self.similarity = 1

            LANGUAGES_CACHES[self._language] = {
                "l": self.language,
                "s": self.similarity
            }

    
        self.name = LANGUAGES_CODE_TO_NAME_EN.get(self.language, "Unknown").title()
                
        #### ISO
        self.alpha2 = self.language.split("-")[0]
        self.alpha3 = ALPHA2_TO_ALPHA3.get(self.alpha2, None)

        #### Defining for specific translators
        self.google_translate = self.language
        self.yandex_translate = self.language
        self.reverso_translate = self.alpha3
        
        if self.language == "auto":
            self.bing_translate = "auto-detect"
        elif self.language == "no":
            self.bing_translate = "nb"
        elif self.language == "pt":
            self.bing_translate = "pt-pt"
        elif self.language.lower() == "zh-cn":
            self.bing_translate = "zh-Hans"
        elif self.language.lower() == "zh-tw":
            self.bing_translate = "zh-Hant"
        else:
            self.bing_translate = self.language
        

        #### Localization
        self.afrikaans = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('af', None)
        self.albanian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sq', None)
        self.amharic = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('am', None)
        self.arabic = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ar', None)
        self.armenian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('hy', None)
        self.azerbaijani = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('az', None)
        self.basque = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('eu', None)
        self.belarusian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('be', None)
        self.bengali = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('bn', None)
        self.bosnian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('bs', None)
        self.bulgarian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('bg', None)
        self.catalan = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ca', None)
        self.cebuano = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ceb', None)
        self.chichewa = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ny', None)
        self.chinese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('zh-CN', None)
        self.chinese_simplified = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('zh-CN', None)
        self.chinese_traditional = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('zh-TW', None)
        self.corsican = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('co', None)
        self.croatian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('hr', None)
        self.czech = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('cs', None)
        self.danish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('da', None)
        self.dutch = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('nl', None)
        self.english = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('en', None)
        self.esperanto = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('eo', None)
        self.estonian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('et', None)
        self.filipino = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('tl', None)
        self.finnish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('fi', None)
        self.french = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('fr', None)
        self.frisian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('fy', None)
        self.galician = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('gl', None)
        self.georgian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ka', None)
        self.german = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('de', None)
        self.greek = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('el', None)
        self.gujarati = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('gu', None)
        self.haitian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ht', None)
        self.creole = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ht', None)
        self.haitian_creole = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ht', None)
        self.hausa = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ha', None)
        self.hawaiian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('haw', None)
        self.hebrew = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('iw', None)
        self.hindi = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('hi', None)
        self.hmong = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('hmn', None)
        self.hungarian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('hu', None)
        self.icelandic = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('is', None)
        self.igbo = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ig', None)
        self.indonesian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('id', None)
        self.irish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ga', None)
        self.italian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('it', None)
        self.japanese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ja', None)
        self.javanese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('jw', None)
        self.kannada = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('kn', None)
        self.kazakh = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('kk', None)
        self.khmer = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('km', None)
        self.korean = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ko', None)
        self.kurdish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ku', None)
        self.kurdish_kurmanji = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ku', None)
        self.kyrgyz = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ky', None)
        self.lao = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('lo', None)
        self.latin = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('la', None)
        self.latvian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('lv', None)
        self.lithuanian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('lt', None)
        self.luxembourgish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('lb', None)
        self.macedonian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('mk', None)
        self.malagasy = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('mg', None)
        self.malay = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ms', None)
        self.malayalam = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ml', None)
        self.maltese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('mt', None)
        self.maori = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('mi', None)
        self.marathi = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('mr', None)
        self.mongolian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('mn', None)
        self.myanmar = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('my', None)
        self.burmese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('my', None)
        self.myanmar_burmese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('my', None)
        self.nepali = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ne', None)
        self.norwegian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('no', None)
        self.odia = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('or', None)
        self.pashto = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ps', None)
        self.persian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('fa', None)
        self.polish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('pl', None)
        self.portuguese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('pt', None)
        self.punjabi = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('pa', None)
        self.romanian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ro', None)
        self.russian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ru', None)
        self.samoan = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sm', None)
        self.scots = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('gd', None)
        self.gaelic = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('gd', None)
        self.scots_gaelic = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('gd', None)
        self.serbian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sr', None)
        self.sesotho = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('st', None)
        self.shona = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sn', None)
        self.sindhi = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sd', None)
        self.sinhala = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('si', None)
        self.slovak = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sk', None)
        self.slovenian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sl', None)
        self.somali = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('so', None)
        self.spanish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('es', None)
        self.sundanese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('su', None)
        self.swahili = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sw', None)
        self.swedish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('sv', None)
        self.tajik = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('tg', None)
        self.tamil = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ta', None)
        self.telugu = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('te', None)
        self.thai = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('th', None)
        self.turkish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('tr', None)
        self.ukrainian = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('uk', None)
        self.urdu = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ur', None)
        self.uyghur = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('ug', None)
        self.uzbek = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('uz', None)
        self.vietnamese = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('vi', None)
        self.welsh = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('cy', None)
        self.xhosa = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('xh', None)
        self.yiddish = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('yi', None)
        self.yoruba = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('yo', None)
        self.zulu = LANGUAGES_TO_INTERNATIONAL.get(self.language, {}).get('zu', None)

    
    def __repr__(self) -> str:
        if self.similarity != 1:
            return self.name + " (Similarity: " + str(round(self.similarity*100, 2)) + "%)"
        else:
            return self.name

    def __str__(self) -> str:
        return self.language

    def __call__(self, *args, **kwds):
        return self.language

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Language):
            return o.language == self.language
        return str(o) == self.result

    def __ne__(self, o: object) -> bool:
        if isinstance(o, Language):
            return o.language != self.language
        return str(o) != self.result
