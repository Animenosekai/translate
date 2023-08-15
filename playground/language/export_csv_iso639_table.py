import csv
from translatepy.translators import YandexTranslate
from json_storager import JSONCacher
# from icecream import ic  # Only for debug
import concurrent.futures

dl = YandexTranslate()
dl._translations_cache = JSONCacher()  # Cache file storager

# Language = namedtuple('Language', 'name alpha2 alpha3 in_foreign_languages yandex google bing reverso deepl')

destination_languages_list = [
    'sw', 'ne', 'sq', 'ht', 'nl', 'be', 'ga', 'ba', 'ta', 'mg', 'pa', 'gd',
    'fi', 'ky', 'ar', 'he', 'lt', 'uz', 'pl', 'mi', 'ms', 'sv', 'uk', 'pt',
    'vi', 'hu', 'cy', 'gu', 'eo', 'km', 'no', 'bg', 'es', 'cv', 'et', 'ja',
    'da', 'bn', 'it', 'en', 'ca', 'th', 'tl', 'la', 'te', 'tt', 'ko', 'xh',
    'ml', 'sl', 'af', 'fa', 'tg', 'hy', 'hi', 'my', 'el', 'id', 'ka', 'mk',
    'cs', 'is', 'lo', 'eu', 'mr', 'jv', 'sr', 'bs', 'kn', 'ru', 'zh', 'gl',
    'si', 'ro', 'su', 'fr', 'ur', 'sk', 'lb', 'hr', 'am', 'yi', 'mn', 'de',
    'kk', 'mt', 'lv', 'tr', 'zu', 'az'
]


def iso_639_csv_exporter(output_file_py):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        _records_list = "from collections import namedtuple\n\nLanguage = namedtuple('Language', 'name alpha2 alpha3 in_foreign_languages yandex google bing reverso deepl')\nlanguages_list=[\n"
        with open('iso639.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                name = row[3].replace("'", '"')

                _translations_results = []
                for dest_lang in destination_languages_list:
                    # Translation to other languages
                    # ic(f"Append task: {dest_lang}")
                    future = executor.submit(dl.translate, name, dest_lang,
                                             "en")
                    _translations_results.append([future, dest_lang])

                _name_in_foreign_languages = {}
                for trans_result in _translations_results:
                    try:
                        result = trans_result[0].result().result
                        # ic(f"Getting task result: {result}")
                    except Exception as ex:
                        # ic(f"Got exception: {ex}")
                        result = "None"
                    finally:
                        _name_in_foreign_languages.update(
                            {trans_result[1]: result.replace("'", '"')})

                string = f"Language('{name}', '{row[2]}', '{row[0]}', " + f"{_name_in_foreign_languages}" + \
                    f", '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}'" + "),\n"
                # ic(string)

                _records_list += string

        _records_list += "]"

        with open(output_file_py, 'w') as file:
            file.write(_records_list)


iso_639_csv_exporter("iso639_table.py")

dl._translations_cache.save()  # Save cached values to JSON file
