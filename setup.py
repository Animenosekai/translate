from setuptools import setup
from os import path
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    readme_description = f.read()
setup(
    name = "translatepy",
    packages = ["translatepy"],
    version = "1.4",
    license = "GNU General Public License v3 (GPLv3)",
    description = "Translate, transliterate, get the language of texts in no time with the help of multiple APIs!",
    author = "Anime no Sekai",
    author_email = "niichannomail@gmail.com",
    url = "https://github.com/Animenosekai/translate",
    download_url = "https://github.com/Animenosekai/translate/archive/v1.4.tar.gz",
    keywords = ['python', 'translate', 'translation', 'google-translate', 'yandex-translate', 'bing-translate', 'reverso', 'transliteration', 'detect-language'],
    install_requires = ['safeIO>=1.2', 'requests', 'beautifulsoup4', 'typing; python_version<"3.5"'],
    classifiers = ['Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.2', 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9'],
    long_description = readme_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
    package_data={
        'translatepy':['LICENSE'],
        'data': [
            'data/_alpha2_to_alpha3.json',
            'data/_google_translate_domains.json',
            'data/_languages_code.json',
            'data/_languages_name_to_code_en.json',
            'data/_languages_name_to_code_international.json',
            'data/_languages_to_international.json',
        ],
        'models': ['models/userAgents.json'],
    },
)
