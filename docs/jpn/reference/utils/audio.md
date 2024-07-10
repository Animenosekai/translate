# *module* **audio**

> [Source: ../../../../translatepy/utils/audio.py](../../../../translatepy/utils/audio.py#L0)

Handles audio file formats for translatepy

## Copyright

- **h2non, MIT License**
Author of `filetype.py` a Python package to infer binary file types checking the magic numbers signature
Most of the source code comes from this package
## *class* [**Type**](../../../../translatepy/utils/audio.py#L12-L22)

Represents an audio format

### *attr* [Type.**MIME**](../../../../translatepy/utils/audio.py#L16)

> Type: `str`

### *attr* [Type.**EXTENSION**](../../../../translatepy/utils/audio.py#L17)

> Type: `str`

### *func* [Type.**test**](../../../../translatepy/utils/audio.py#L20-L22)

Tests if the given file matches the audio format

#### Parameters

- **data**: `bytes`


## *class* [**MP3**](../../../../translatepy/utils/audio.py#L25-L42)

Implements the MP3 audio type matcher.

### *attr* [MP3.**MIME**](../../../../translatepy/utils/audio.py#L29)

### *attr* [MP3.**EXTENSION**](../../../../translatepy/utils/audio.py#L30)

### *func* [MP3.**test**](../../../../translatepy/utils/audio.py#L33-L42)

#### Parameters

- **data**: `bytes`


## *class* [**M4A**](../../../../translatepy/utils/audio.py#L45-L64)

Implements the M4A audio type matcher.

### *attr* [M4A.**MIME**](../../../../translatepy/utils/audio.py#L49)

### *attr* [M4A.**EXTENSION**](../../../../translatepy/utils/audio.py#L50)

### *func* [M4A.**test**](../../../../translatepy/utils/audio.py#L53-L64)

#### Parameters

- **data**: `bytes`


## *class* [**Ogg**](../../../../translatepy/utils/audio.py#L67-L79)

Implements the OGG audio type matcher.

### *attr* [Ogg.**MIME**](../../../../translatepy/utils/audio.py#L71)

### *attr* [Ogg.**EXTENSION**](../../../../translatepy/utils/audio.py#L72)

### *func* [Ogg.**test**](../../../../translatepy/utils/audio.py#L75-L79)

#### Parameters

- **data**: `bytes`


## *class* [**Flac**](../../../../translatepy/utils/audio.py#L82-L94)

Implements the FLAC audio type matcher.

### *attr* [Flac.**MIME**](../../../../translatepy/utils/audio.py#L86)

### *attr* [Flac.**EXTENSION**](../../../../translatepy/utils/audio.py#L87)

### *func* [Flac.**test**](../../../../translatepy/utils/audio.py#L90-L94)

#### Parameters

- **data**: `bytes`


## *class* [**Wav**](../../../../translatepy/utils/audio.py#L97-L113)

Implements the WAV audio type matcher.

### *attr* [Wav.**MIME**](../../../../translatepy/utils/audio.py#L101)

### *attr* [Wav.**EXTENSION**](../../../../translatepy/utils/audio.py#L102)

### *func* [Wav.**test**](../../../../translatepy/utils/audio.py#L105-L113)

#### Parameters

- **data**: `bytes`


## *class* [**Amr**](../../../../translatepy/utils/audio.py#L116-L130)

Implements the AMR audio type matcher.

### *attr* [Amr.**MIME**](../../../../translatepy/utils/audio.py#L120)

### *attr* [Amr.**EXTENSION**](../../../../translatepy/utils/audio.py#L121)

### *func* [Amr.**test**](../../../../translatepy/utils/audio.py#L124-L130)

#### Parameters

- **data**: `bytes`


## *class* [**Aac**](../../../../translatepy/utils/audio.py#L133-L142)

Implements the Aac audio type matcher.

### *attr* [Aac.**MIME**](../../../../translatepy/utils/audio.py#L136)

### *attr* [Aac.**EXTENSION**](../../../../translatepy/utils/audio.py#L137)

### *func* [Aac.**test**](../../../../translatepy/utils/audio.py#L140-L142)

#### Parameters

- **data**: `bytes`


## *class* [**Aiff**](../../../../translatepy/utils/audio.py#L145-L161)

Implements the AIFF audio type matcher.

### *attr* [Aiff.**MIME**](../../../../translatepy/utils/audio.py#L149)

### *attr* [Aiff.**EXTENSION**](../../../../translatepy/utils/audio.py#L150)

### *func* [Aiff.**test**](../../../../translatepy/utils/audio.py#L153-L161)

#### Parameters

- **data**: `bytes`


## *func* [**get_type**](../../../../translatepy/utils/audio.py#L164-L181)

Returns the audio format of the given buffer

### Parameters

- **buffer**: `bytes`
  - The audio file data


### Returns

- `Optional[Type]`
    - The type of audio file
