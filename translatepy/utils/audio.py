"""
Handles audio file formats for translatepy

Copyright
---------
h2non, MIT License
    Author of `filetype.py` a Python package to infer binary file types checking the magic numbers signature
    Most of the source code comes from this package
"""


class Type:
    """
    Represents an audio format
    """
    MIME: str
    EXTENSION: str

    @staticmethod
    def test(data: bytes):
        """Tests if the given file matches the audio format"""
        return False


class MP3(Type):
    """
    Implements the MP3 audio type matcher.
    """
    MIME = 'audio/mpeg'
    EXTENSION = 'mp3'

    @staticmethod
    def test(data: bytes):
        return ((data[0] == 0x49 and
                 data[1] == 0x44 and
                 data[2] == 0x33) or
                (data[0] == 0xFF and
                 data[1] == 0xF2) or
                (data[0] == 0xFF and
                 data[1] == 0xF3) or
                (data[0] == 0xFF and
                 data[1] == 0xFB))


class M4A(Type):
    """
    Implements the M4A audio type matcher.
    """
    MIME = 'audio/mp4'
    EXTENSION = 'm4a'

    @staticmethod
    def test(data: bytes):
        return ((data[4] == 0x66 and
                 data[5] == 0x74 and
                 data[6] == 0x79 and
                 data[7] == 0x70 and
                 data[8] == 0x4D and
                 data[9] == 0x34 and
                 data[10] == 0x41) or
                (data[0] == 0x4D and
                    data[1] == 0x34 and
                    data[2] == 0x41 and
                    data[3] == 0x20))


class Ogg(Type):
    """
    Implements the OGG audio type matcher.
    """
    MIME = 'audio/ogg'
    EXTENSION = 'ogg'

    @staticmethod
    def test(data: bytes):
        return (data[0] == 0x4F and
                data[1] == 0x67 and
                data[2] == 0x67 and
                data[3] == 0x53)


class Flac(Type):
    """
    Implements the FLAC audio type matcher.
    """
    MIME = 'audio/x-flac'
    EXTENSION = 'flac'

    @staticmethod
    def test(data: bytes):
        return (data[0] == 0x66 and
                data[1] == 0x4C and
                data[2] == 0x61 and
                data[3] == 0x43)


class Wav(Type):
    """
    Implements the WAV audio type matcher.
    """
    MIME = 'audio/x-wav'
    EXTENSION = 'wav'

    @staticmethod
    def test(data: bytes):
        return (data[0] == 0x52 and
                data[1] == 0x49 and
                data[2] == 0x46 and
                data[3] == 0x46 and
                data[8] == 0x57 and
                data[9] == 0x41 and
                data[10] == 0x56 and
                data[11] == 0x45)


class Amr(Type):
    """
    Implements the AMR audio type matcher.
    """
    MIME = 'audio/amr'
    EXTENSION = 'amr'

    @staticmethod
    def test(data: bytes):
        return (data[0] == 0x23 and
                data[1] == 0x21 and
                data[2] == 0x41 and
                data[3] == 0x4D and
                data[4] == 0x52 and
                data[5] == 0x0A)


class Aac(Type):
    """Implements the Aac audio type matcher."""

    MIME = 'audio/aac'
    EXTENSION = 'aac'

    @staticmethod
    def test(data: bytes):
        return (data[:2] == bytearray([0xff, 0xf1]) or
                data[:2] == bytearray([0xff, 0xf9]))


class Aiff(Type):
    """
    Implements the AIFF audio type matcher.
    """
    MIME = 'audio/x-aiff'
    EXTENSION = 'aiff'

    @staticmethod
    def test(data: bytes):
        return (data[0] == 0x46 and
                data[1] == 0x4F and
                data[2] == 0x52 and
                data[3] == 0x4D and
                data[8] == 0x41 and
                data[9] == 0x49 and
                data[10] == 0x46 and
                data[11] == 0x46)


def get_type(buffer: bytes):
    """
    Returns the audio format of the given buffer

    Parameters
    ----------
    buffer: bytes
        The audio file data

    Returns
    -------
    Optional[Type]
        The type of audio file
    """
    for audio_format in (MP3, M4A, Ogg, Flac, Wav, Amr, Aac, Aiff):
        if audio_format.test(buffer):
            return audio_format
    return None
