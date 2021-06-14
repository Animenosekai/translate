from translatepy.utils import iso639_table


def _build_index(idx):
    return dict((r[idx].lower(), r) for r in iso639_table.languages_list)


by_name = _build_index(0)
by_alpha2 = _build_index(1)
by_alpha3 = _build_index(2)

by_foreign_name = dict()
for _language in iso639_table.languages_list:
    for k, v in _language[3].items():
        by_foreign_name.update({v.lower(): _language})

by_yandex = _build_index(4)
by_google = _build_index(5)
by_bing = _build_index(6)
by_reverso = _build_index(7)
by_deepl = _build_index(8)
