from safeIO import JSONFile

GOOGLE_TRANSLATE_DOMAINS = JSONFile("data/_google_translate_domains.json").read()
LANGUAGES_CODE = JSONFile("data/_languages_code.json").read()
LANGUAGES_NAME_TO_CODE_EN = JSONFile("data/_languages_name_to_code_en.json").read()
LANGUAGES_NAME_TO_CODE_INTERNATIONAL = JSONFile("data/_languages_name_to_code_international.json").read()
LANGUAGES_TO_INTERNATIONAL = JSONFile("data/_languages_to_international.json").read()
LANGUAGES_CODE_TO_NAME_EN = {LANGUAGES_NAME_TO_CODE_EN[language_name]:language_name for language_name in LANGUAGES_NAME_TO_CODE_EN}
ALPHA2_TO_ALPHA3 = JSONFile("data/_alpha2_to_alpha3.json").read()
ALPHA3_TO_ALPHA2 = {ALPHA2_TO_ALPHA3[code]:code for code in ALPHA2_TO_ALPHA3}