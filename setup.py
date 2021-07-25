from setuptools import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    readme_description = f.read()

setup(
    name ="translatepy",
    packages = ["translatepy"],
    version = "2.0",
    license = "GNU General Public License v3 (GPLv3)",
    description = "Translate, transliterate, get the language of texts in no time with the help of multiple APIs!",
    author = "Anime no Sekai",
    author_email = "niichannomail@gmail.com",
    url = "https://github.com/Animenosekai/translate",
    download_url = "https://github.com/Animenosekai/translate/archive/v2.0.tar.gz",
    keywords = ['python', 'translate', 'translation', 'google-translate', 'yandex-translate', 'bing-translate', 'reverso', 'transliteration', 'detect-language', 'text-to-speech', 'deepl', 'language'],
    install_requires = ['requests', 'beautifulsoup4', 'typing; python_version<"3.5"', 'pyuseragents', 'inquirer'],
    classifiers = ['Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.2', 'Programming Language :: Python :: 3.3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9'],
    long_description = readme_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
    python_requires='>=3.2, <4',
    entry_points={
          'console_scripts': [
              'translatepy = translatepy.__main__:main'
          ]
    },
    package_data={
        'translatepy': ['LICENSE'],
    },
)
