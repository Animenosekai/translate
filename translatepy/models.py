"""
translatepy/models.py

Describes the different result models returned by the translators
"""
import dataclasses
import enum
import pathlib
import typing

from translatepy.language import Language
from translatepy.utils.audio import get_type

# pylint: disable=consider-using-f-string


class Speed(enum.Enum):
    """Represents a speed percentage"""
    FULL = 100
    HALF = 50
    QUARTER = 25
    SLOW = HALF


class Gender(enum.Enum):
    """Represents a gender"""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    GENDERLESS = "genderless"


class WordClass(enum.Enum):
    """
    Part of speech

    Note: Refer to https://en.wikipedia.org/wiki/Part_of_speech
    """
    NOUN = "noun"
    """
    A word or lexical item denoting any abstract (abstract noun: e.g. home) or concrete entity (concrete noun: e.g. house);
    a person (police officer, Michael), place (coastline, London), thing (necktie, television), idea (happiness), or quality (bravery).
    Nouns can also be classified as count nouns or non-count nouns; some can belong to either category. The most common part of speech; they are called naming words.
    
    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    PRONOUN = "pronoun"
    """
    A substitute for a noun or noun phrase (them, he). Pronouns make sentences shorter and clearer since they replace nouns.
    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    ADJECTIVE = "adjective"
    """
    A modifier of a noun or pronoun (big, brave). Adjectives make the meaning of another word (noun) more precise.
    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    VERB = "verb"
    """
    A word denoting an action (walk), occurrence (happen), or state of being (be). Without a verb, a group of words cannot be a clause or sentence.
    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    ADVERB = "adverb"
    """
    A modifier of an adjective, verb, or another adverb (very, quite). Adverbs make language more precise.
    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    PREPOSITION = "Preposition"
    """
    a word that relates words to each other in a phrase or sentence and aids in syntactic context (in, of).
    Prepositions show the relationship between a noun or a pronoun with another word in the sentence.

    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    CONJUNCTION = "conjunction"
    """
    A syntactic connector; links words, phrases, or clauses (and, but). Conjunctions connect words or group of words
    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    INTERJECTION = "interjection"
    """
    An emotional greeting or exclamation (Huzzah, Alas). Interjections express strong feelings and emotions.
    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    ARTICLE = "article"
    """
    A grammatical marker of definiteness (the) or indefiniteness (a, an).
    The article is not always listed among the parts of speech.
    It is considered by some grammarians to be a type of adjective or sometimes the term 'determiner' (a broader class) is used.

    Note: https://en.wikipedia.org/wiki/Part_of_speech#Classification
    """

    OTHER = "other"
    """
    For other part of speech
    """


@dataclasses.dataclass(kw_only=True, slots=True)
class Result:
    """
    The base result model
    """
    service: "BaseTranslator"
    """The service which returned the result"""

    source: str
    """The source text"""
    # source_language: Language
    # """The source text's language"""

    # We can't define `result` here because they vary accross the different models
    # result: typing.Any
    # """The result"""

    # destination_language: Language
    # """The result's language"""

    raw: typing.Optional[typing.Any] = None
    """
    The raw response returned by the service.
    Note: This is very dependent on the service used.
    
    Refer to the service documentation to learn how to use this object.
    """

    # def __str__(self) -> str:
    #     return str(self.result)

    def __repr__(self) -> str:
        return "{name}({params})".format(
            name=self.__class__.__name__,
            params=", ".join("{key}={val}".format(key=attr,
                                                  val=repr(getattr(self, attr)))
                             for attr in dir(self)
                             if not str(attr).startswith("__") and not callable(getattr(self, attr)) and attr != "raw")
        )

    def __pretty__(self, cli: bool = False) -> str:
        """
        A nice way of presenting the result to the end user
        """
        if not cli:
            return self.__repr__()

        return "{magenta}{name}{normal}({params})".format(
            magenta="\033[95m",
            normal="\033[0m",
            name=self.__class__.__name__,
            params=", ".join(
                "{blue}{key}{normal}={cyan}{val}{normal}".format(
                    blue="\033[94m",
                    normal="\033[0m",
                    cyan="\033[96m",
                    key=attr,
                    val=repr(getattr(self, attr))
                )
                for attr in dir(self)
                if not str(attr).startswith("__") and not callable(getattr(self, attr)) and attr != "raw")
        )


@dataclasses.dataclass(kw_only=True, slots=True)
class TranslationResult(Result):
    """
    Holds the result of a regular translation
    """
    source_language: Language
    """The source text's language"""

    destination_language: Language
    """The result's language"""

    translation: str
    """The translation result"""

    _alternatives: typing.List["TranslationResult"] = dataclasses.field(default_factory=list)
    """A cache to alternative translations"""

    @property
    def alternatives(self):
        """Returns the alternative translations associated"""
        if not self._alternatives:
            self._alternatives = self.service.alternatives(self)
        return self._alternatives

    def __pretty__(self, cli: bool = False) -> str:
        return """\
Source {grey}({source_lang}){normal}
{blue}------------{normal}
{cyan}{source}{normal}

Result {grey}({dest_lang}){normal}
{blue}------------{normal}
{green}{result}{normal}\
""".format(grey="\033[90m" if cli else "",
           normal="\033[0m" if cli else "",
           blue="\033[94m" if cli else "",
           cyan="\033[96m" if cli else "",
           green="\033[92m" if cli else "",
           source_lang=self.source_language,
           source=self.source,
           dest_lang=self.destination_language,
           result=self.translation)


TRANSLATION_TEST = TranslationResult(
    service=None,
    source="Hello, how are you ?",
    source_language=Language("english"),
    destination_language=Language("japanese"),
    translation="こんにちは、お元気ですか？"
)

# Note: No, we can't inherit from `TranslationResult` because transliterations aren't translations


@dataclasses.dataclass(kw_only=True, slots=True)
class TransliterationResult(Result):
    """
    Holds the result of a transliteration
    """
    transliteration: str
    """The transliteration result"""

    source_language: Language
    """The source text's language"""

    destination_language: Language
    """The result's language"""

    def __pretty__(self, cli: bool = False) -> str:
        return """\
Source {grey}({source_lang}){normal}
{blue}------------{normal}
{cyan}{source}{normal}

Result {grey}({dest_lang}){normal}
{blue}------------{normal}
{green}{result}{normal}\
""".format(grey="\033[90m" if cli else "",
           normal="\033[0m" if cli else "",
           blue="\033[94m" if cli else "",
           cyan="\033[96m" if cli else "",
           green="\033[92m" if cli else "",
           source_lang=self.source_language,
           source=self.source,
           dest_lang=self.destination_language,
           result=self.transliteration)


TRANSLITERATION_TEST = TransliterationResult(
    service=None,
    source="こんにちは",
    source_language=Language("japanese"),
    transliteration="Konnichiwa",
    destination_language=Language("English")
)


@dataclasses.dataclass(kw_only=True, slots=True)
class SpellcheckResult(Result):
    """
    Holds a spellchecking result
    """
    source_language: Language
    """The source text's language"""
    corrected: str
    """The corrected text"""

    def __pretty__(self, cli: bool = False) -> str:
        return """\
{blue}Original Text {grey}({source_lang}){normal}
{blue}-------------{normal}
{source}

{blue}Corrrected Text{normal}
{blue}---------------{normal}
{result}\
""".format(grey="\033[90m" if cli else "",
           normal="\033[0m" if cli else "",
           blue="\033[94m" if cli else "",
           source_lang=self.source_language,
           source=self.source,
           result=self.corrected)


SPELLCHECK_TEST = SpellcheckResult(
    service=None,
    source="Hello hw are you ?",
    source_language=Language("english"),
    corrected="Hello how are you ?"
)


@dataclasses.dataclass
class SpellcheckMistake:
    """This holds a mistake made detected by the spellchecker"""
    start: int
    """The beginning index of the part to correct in the original text"""
    end: int
    """The ending index of the part to correct in the original text"""
    corrected: str
    """The corrected part"""

    message: typing.Optional[str] = None
    """A message explaining what happened"""

    rule: typing.Optional[str] = None
    """A string which identifies the rule associated with the mistake made"""

# Cannot inherit `SpellcheckResult` for now because of overlapping types for attribute `result`


@dataclasses.dataclass(kw_only=True, slots=True)
class RichSpellcheckResult(Result):
    """
    Holds a rich spellchecking result
    """
    source_language: Language
    """The source text's language"""
    mistakes: typing.List[SpellcheckMistake] = dataclasses.field(default_factory=list)
    """The different mistakes made"""

    @property
    def corrected(self):
        """The corrected text"""
        res = self.source
        initial_len = len(res)
        diff = 0
        for mistake in self.mistakes:
            res = res[:mistake.start + diff] + mistake.corrected + res[mistake.end + diff + 1:]
            diff = len(res) - initial_len
        return res

    def __pretty__(self, cli: bool = False) -> str:
        """
        Formats the spellchecking in a nice way.

        For `SPELLCHECK_TEST`, would format the spellchecking like so:

        Original Text
        -------------
        Hello world, how are aaaaaaaaa oyu doin ?
                   ~        ~~~~~~~~~~ ~~~ ~~~~
                   ╰─> (1) UnneededComma│   ╰─> (4) EndingError
                                ╰─> (2) Meaningless
                                        ╰─> (3) TypoError

        (1): Is a comma really needed here ?
        (2): Meaningless repeated `a`.
        (3): `oyu` might be a typo. Did you mean `you` ?
        (4): A `g` is missing at the end of the verb

        Corrected Text
        --------------
        Hello world how are you doing ?
        """
        # Underline indicators
        remaining: typing.List[typing.Tuple[int, str, SpellcheckMistake]] = []
        indicators = "" if not cli else "\033[93m"
        current = 0
        for index, mistake in enumerate(self.mistakes, start=1):
            mistake_length = mistake.end - mistake.start

            indicators += " " * (mistake.start - current)  # adding the offset until the next tildes
            indicators += "~" * (mistake_length + 1)  # adding the tildes under the mistaken word

            current = mistake.end + 1

            # this skips the ANSI codes
            real_length = 0

            # The actual rendered correction name
            mistake_id = "\033[91m" if cli else ""
            mistake_id += "╰─> "
            real_length += 4
            mistake_id += "\033[0m" if cli else ""

            mistake_id += "\033[95m" if cli else ""
            appending = "({index})".format(index=index)
            mistake_id += appending
            real_length += len(appending)
            mistake_id += "\033[0m" if cli else ""

            if mistake.rule:
                mistake_id += "\033[1;91m" if cli else ""
                appending = " {rule}".format(rule=mistake.rule)
                mistake_id += appending
                real_length += len(appending)
                mistake_id += "\033[0m" if cli else ""

            remaining.append((real_length, mistake_id, mistake))

        if cli:
            indicators += "\033[0m"

        # creating the arrow tail
        arrow_tail = "\033[91m" if cli else ""
        arrow_tail += "│"
        arrow_tail += "\033[0m" if cli else ""

        identifiers = []
        while len(remaining) > 0:
            current_line = ""

            real_length, mistake_id, mistake = remaining.pop(0)  # the first element should always work
            middle_pos = mistake.start + ((mistake.end - mistake.start) // 2)
            end_pos = middle_pos + real_length  # end of the whole identifier

            # checking for previous lines to add the tail of the arrow
            for index, line in enumerate(identifiers):
                # FIXME: There is a problem with ANSI codes
                try:
                    if line[middle_pos] == " ":
                        identifiers[index] = line[:middle_pos] + arrow_tail + line[middle_pos + 1:]
                except IndexError:
                    identifiers[index] += " " * (middle_pos - len(line))
                    identifiers[index] += arrow_tail

            current_line += " " * middle_pos
            current_line += mistake_id

            for index, (real_length, mistake_id, mistake) in enumerate(remaining):  # the first one is removed
                middle_pos = mistake.start + ((mistake.end - mistake.start) // 2)  # position of the identifier in the line
                distance = middle_pos - end_pos  # distance from the previous identifier
                if distance > 0:  # `>` should be better than `>=` for readability ?
                    current_line += " " * distance  # offsets the identifier
                    current_line += mistake_id  # add the identifier

                    end_pos = middle_pos + real_length  # update the end position
                    remaining.pop(index)

                    # checking for previous lines to add the tail of the arrow
                    for index, line in enumerate(identifiers):
                        try:
                            if line[middle_pos] == " ":
                                identifiers[index] = line[:middle_pos] + "│" + line[middle_pos + 1:]
                        except IndexError:
                            identifiers[index] += " " * (middle_pos - len(line))
                            identifiers[index] += "│"

            identifiers.append(current_line)

        explanations = []
        for index, mistake in enumerate(self.mistakes, start=1):
            if mistake.message:
                explanations.append("{magenta}({index}){normal}: {msg}".format(magenta="\033[95m" if cli else "",
                                                                               normal="\033[0m" if cli else "",
                                                                               index=index,
                                                                               msg=mistake.message))

        return """\
{bold_blue}Original Text{normal}
{blue}-------------{normal}
{original}
{indicators}
{identifiers}

{explanations}

{bold_blue}Corrected Text{normal}
{blue}--------------{normal}
{result}\
""".format(bold_blue="\033[1;94m" if cli else "",
           blue="\033[94m" if cli else "",
           normal="\033[0m" if cli else "",
           original=self.source,
           indicators=indicators,
           identifiers="\n".join(identifiers),
           explanations="\n".join(explanations),
           result=self.corrected)


RICH_SPELLCHECK_TEST = RichSpellcheckResult(
    service=None,
    source="Hello world, how are aaaaaaaaa oyu doin ?",
    source_language=Language("English"),
    mistakes=[
        SpellcheckMistake(start=11, end=11, corrected="", message="Is a comma really needed here ?", rule="UnneededComma"),
        SpellcheckMistake(start=20, end=29, corrected="", message="Meaningless repeated `a`.", rule="Meaningless"),
        SpellcheckMistake(start=31, end=33, corrected="you", message="`oyu` might be a typo. Did you mean `you` ?", rule="TypoError"),
        SpellcheckMistake(start=35, end=38, corrected="doing", message="A `g` is missing at the end of the verb", rule="EndingError")
    ]
)


@dataclasses.dataclass(kw_only=True, slots=True)
class LanguageResult(Result):
    """
    Holds the language of the given text
    """
    language: Language
    """The detected language"""

    def __pretty__(self, cli: bool = False) -> str:
        return "The detected language is {colored}{lang}{normal}".format(
            lang=self.language,
            colored="\033[1;96m" if cli else "",
            normal="\033[0m" if cli else ""
        )


@dataclasses.dataclass(kw_only=True, slots=True)
class ExampleResult(Result):
    """
    Holds an example sentence where the given word is used.
    """
    example: str
    """The example"""

    reference: typing.Optional[str] = None
    """Where the example comes from (i.e a book or a the person who said it if it's a quote)"""

    @property
    def position(self) -> typing.Optional[int]:
        """
        The first position of the word in the example
        """
        try:
            return self.positions[0]
        except IndexError:
            return None

    @property
    def positions(self) -> typing.List[int]:
        """
        The positions of the word in the example
        """
        searching = False
        current_letter = 0
        searching_length = len(self.source)

        positions = []
        for index, letter in enumerate(self.example, start=1):
            same_letter = letter == self.source[current_letter]

            if same_letter and current_letter == 0 and not searching:
                searching = True
                current_letter += 1  # search for the next letter in `self.source`
            elif same_letter and searching:
                current_letter += 1  # search for the next letter in `self.source`
            else:
                # resetting everything
                current_letter = 0
                searching = False

            if current_letter >= searching_length:
                positions.append(index - searching_length)
                searching = False
                current_letter = 0
        return positions

    def __pretty__(self, cli: bool = False) -> str:
        source_length = len(self.source)
        if cli:
            result = self.example
            for pos in self.positions:
                result = "{before}{bold}{source}{normal}{after}".format(
                    before=result[:pos],
                    bold="\033[1m",
                    source=self.source,
                    normal="\033[0m",
                    after=result[pos + source_length:]
                )
        else:
            result = self.example

        indicators = "" if not cli else "\033[90m"
        current = 0
        for pos in self.positions:
            indicators += " " * (pos - current)  # adding the offset until the next tildes
            indicators += "~" * source_length  # adding the tildes under the source word
            current = (pos + source_length)  # end of the current word

        if cli:
            indicators += "\033[0m"

        return """\
{result}
{indicators}\
""".format(result=result,
           indicators=indicators)


EXAMPLE_TEST = ExampleResult(
    service=None,
    source="how",
    example="Hello everyone, how are you ?"
)


@dataclasses.dataclass(kw_only=True, slots=True)
class DictionaryResult(Result):
    """
    Holds the meaning of the given text
    """
    source_language: Language
    """The source text's language"""

    meaning: str
    """The meaning of the text"""

    def __pretty__(self, cli: bool = False) -> str:
        return "{colored}{text}{normal}: {meaning}".format(colored="\033[1;96m" if cli else "",
                                                           normal="\033[0m",
                                                           text=self.source,
                                                           meaning=self.meaning)


@dataclasses.dataclass
class EtymologicalNode:
    """The node of an etymological tree"""
    origin: str
    """The origin name (i.e 'Latin')"""

    source: typing.Optional[str] = None
    """The original way of writing it"""
    year: typing.Optional[int] = None
    """The year of origin"""

    def __pretty__(self, cli: bool = False) -> str:
        if self.source:
            if self.year:
                return "{origin} {grey}({source}; {year}){normal}".format(origin=self.origin,
                                                                          grey="\033[90m" if cli else "",
                                                                          normal="\033[0m" if cli else "",
                                                                          source=self.source,
                                                                          year=self.year)
            return "{origin} {grey}({source}){normal}".format(origin=self.origin,
                                                              grey="\033[90m" if cli else "",
                                                              normal="\033[0m" if cli else "",
                                                              source=self.source)
        if self.year:
            return "{origin} {grey}({year}){normal}".format(origin=self.origin,
                                                            grey="\033[90m" if cli else "",
                                                            normal="\033[0m" if cli else "",
                                                            year=self.year)
        return str(self.origin)


@dataclasses.dataclass(kw_only=True, slots=True)
class RichDictionaryResult(DictionaryResult):
    """
    Holds more (optional) information than the regular `DictionaryResult`
    """

    etymology: typing.List[EtymologicalNode] = dataclasses.field(default_factory=list)
    """
    The etymological/origins tree of the given text

    Each element corresponds to a node in the tree of origins for the given text

    Example
    -------
    Node1 (Greek) -> Node2 (Latin) -> Node3 (French) -> Node4 (Ancient English) -> Current Word
    """

    gender: Gender = Gender.OTHER
    """
    For languages which assign genders on words

    Example
    -------
    chaîse (french; a chair) -> Gender.FEMALE
    """

    pronunciation: typing.Optional[str] = None
    """A way of pronouncing the text"""

    type: WordClass = WordClass.OTHER
    """The part of speech of the text"""

    synonyms: typing.List[str] = dataclasses.field(default_factory=list)
    antonyms: typing.List[str] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        # self.__tried = False
        self.etymology.sort(key=lambda node: node.year or 0)

    # def __getattribute__(self, __name: str):
    #     if (__name == "pronunciation"  # if we are getting the pronunciation
    #             and not self.__tried):  # don't need to retry if we already failed once
    #         try:
    #             result = super().__getattribute__(__name)
    #             if result is None:  # there is no result: time to try get one!
    #                 # transliteration is kind of like pronunciation isn't it ?
    #                 result = self.service.transliterate(text=result, destination_language=self.source_language)
    #                 self.pronunciation = result  # saving it for later uses
    #         except Exception:
    #             pass
    #         self.__tried = True  # already tried so we don't need to try again
    #     else:
    #         result = super().__getattribute__(__name)
    #     return result

    def __pretty__(self, cli: bool = False) -> str:
        result = "{bold}{text}{normal} ".format(bold="\033[1m" if cli else "",
                                                text=self.source,
                                                normal="\033[0m" if cli else "")
        if self.pronunciation:
            result += "[{italic}{pronunc}{normal}] ".format(italic="\033[3m" if cli else "",
                                                            pronunc=self.pronunciation,
                                                            normal="\033[0m" if cli else "")

        result += "{}, {}".format(self.gender.name, self.type.name)
        result += "\n"
        result += " " * (len(self.source) + 1)
        result += self.meaning

        if self.synonyms:
            synonyms = """
{blue}Synonyms{normal}
{blue}--------{normal}
{syn}\
""".format(blue="\033[94m" if cli else "",
                normal="\033[0m" if cli else "",
                syn=", ".join(repr(syn) for syn in self.synonyms))
        else:
            synonyms = ""

        if self.antonyms:
            antonyms = """
{blue}Antonyms{normal}
{blue}--------{normal}
{ant}\
""".format(blue="\033[94m" if cli else "",
                normal="\033[0m" if cli else "",
                ant=", ".join(repr(ant) for ant in self.antonyms))
        else:
            antonyms = ""

        if self.etymology:
            etymology_tree = """
{blue}Etymology{normal}
{blue}---------{normal}
{tree} -> Current\
""".format(blue="\033[94m" if cli else "",
                normal="\033[0m" if cli else "",
                tree=" -> ".join([node.__pretty__(cli=cli) for node in self.etymology]))
        else:
            etymology_tree = ""

        return """\
{result}
{etymology}
{synonyms}
{antonyms}\
""".format(result=result, etymology=etymology_tree, synonyms=synonyms, antonyms=antonyms)


RICH_DICTIONARY_TEST = RichDictionaryResult(
    service=None,
    source="hello",
    source_language=Language("english"),
    pronunciation="/həˈləʊ,hɛˈləʊ/",
    type=WordClass.INTERJECTION,
    gender=Gender.GENDERLESS,
    meaning="Used as a greeting or to begin a phone conversation.",
    etymology=[EtymologicalNode(origin="English", source="hollo", year=1800), EtymologicalNode(origin="English", source="holla", year=1800)],
    synonyms=["Hi", "Good morning!"],
    antonyms=["Goodbye"]
)


@dataclasses.dataclass(kw_only=True, slots=True)
class TextToSpechResult(Result):
    """
    Holds the text to speech results
    """
    source_language: Language
    """The source text's language"""

    result: bytes
    """Text to speech result"""
    speed: int = 100
    """Speed of the text to speech result"""
    gender: Gender = Gender.OTHER
    """Gender of the 'person' saying the text"""

    @property
    def type(self):
        """Returns the type of audio file"""
        return get_type(self.result)

    @property
    def mime_type(self):
        """Returns the MIME type of the audio file"""
        try:
            return self.type.MIME
        except Exception:
            return None

    @property
    def extension(self):
        """Returns the audio file extension"""
        try:
            return self.type.EXTENSION
        except Exception:
            return None

    def write_to_file(self, file: typing.Union[str, pathlib.Path, typing.BinaryIO], replace_ext: bool = False):
        """
        Writes the spoken text to a file.

        Parameters
        ----------
        file: str | Path | IO
            The output path or object
        replace_ext: bool, default = False
            If we need to change the extension of the file to match the right file type
        """
        try:
            # BinaryIO
            file.write(self.result)
        except Exception:
            file = pathlib.Path(file)
            if replace_ext:
                file = file.with_suffix(".{ext}".format(ext=self.extension))
            file.write_bytes(self.result)
