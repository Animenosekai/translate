# *module* **audio**

> [Source: ../../../../translatepy/utils/audio.py @ line 0](../../../../translatepy/utils/audio.py#L0)

Handles audio file formats for translatepy

## Copyright

- **h2non, MIT License**
Author of `filetype.py` a Python package to infer binary file types checking the magic numbers signature
Most of the source code comes from this package
## *class* **Type**

> [Source: ../../../../translatepy/utils/audio.py @ line 12-22](../../../../translatepy/utils/audio.py#L12-L22)

Represents an audio format

### *attr* Type.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 16](../../../../translatepy/utils/audio.py#L16)

> Type: `str`

### *attr* Type.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 17](../../../../translatepy/utils/audio.py#L17)

> Type: `str`

### *func* Type.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 20-22](../../../../translatepy/utils/audio.py#L20-L22)

Tests if the given file matches the audio format

#### Parameters

- **data**: `bytes`


## *class* **MP3**

> [Source: ../../../../translatepy/utils/audio.py @ line 25-42](../../../../translatepy/utils/audio.py#L25-L42)

Implements the MP3 audio type matcher.

### *attr* MP3.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 29](../../../../translatepy/utils/audio.py#L29)

### *attr* MP3.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 30](../../../../translatepy/utils/audio.py#L30)

### *func* MP3.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 33-42](../../../../translatepy/utils/audio.py#L33-L42)

#### Parameters

- **data**: `bytes`


## *class* **M4A**

> [Source: ../../../../translatepy/utils/audio.py @ line 45-64](../../../../translatepy/utils/audio.py#L45-L64)

Implements the M4A audio type matcher.

### *attr* M4A.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 49](../../../../translatepy/utils/audio.py#L49)

### *attr* M4A.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 50](../../../../translatepy/utils/audio.py#L50)

### *func* M4A.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 53-64](../../../../translatepy/utils/audio.py#L53-L64)

#### Parameters

- **data**: `bytes`


## *class* **Ogg**

> [Source: ../../../../translatepy/utils/audio.py @ line 67-79](../../../../translatepy/utils/audio.py#L67-L79)

Implements the OGG audio type matcher.

### *attr* Ogg.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 71](../../../../translatepy/utils/audio.py#L71)

### *attr* Ogg.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 72](../../../../translatepy/utils/audio.py#L72)

### *func* Ogg.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 75-79](../../../../translatepy/utils/audio.py#L75-L79)

#### Parameters

- **data**: `bytes`


## *class* **Flac**

> [Source: ../../../../translatepy/utils/audio.py @ line 82-94](../../../../translatepy/utils/audio.py#L82-L94)

Implements the FLAC audio type matcher.

### *attr* Flac.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 86](../../../../translatepy/utils/audio.py#L86)

### *attr* Flac.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 87](../../../../translatepy/utils/audio.py#L87)

### *func* Flac.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 90-94](../../../../translatepy/utils/audio.py#L90-L94)

#### Parameters

- **data**: `bytes`


## *class* **Wav**

> [Source: ../../../../translatepy/utils/audio.py @ line 97-113](../../../../translatepy/utils/audio.py#L97-L113)

Implements the WAV audio type matcher.

### *attr* Wav.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 101](../../../../translatepy/utils/audio.py#L101)

### *attr* Wav.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 102](../../../../translatepy/utils/audio.py#L102)

### *func* Wav.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 105-113](../../../../translatepy/utils/audio.py#L105-L113)

#### Parameters

- **data**: `bytes`


## *class* **Amr**

> [Source: ../../../../translatepy/utils/audio.py @ line 116-130](../../../../translatepy/utils/audio.py#L116-L130)

Implements the AMR audio type matcher.

### *attr* Amr.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 120](../../../../translatepy/utils/audio.py#L120)

### *attr* Amr.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 121](../../../../translatepy/utils/audio.py#L121)

### *func* Amr.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 124-130](../../../../translatepy/utils/audio.py#L124-L130)

#### Parameters

- **data**: `bytes`


## *class* **Aac**

> [Source: ../../../../translatepy/utils/audio.py @ line 133-142](../../../../translatepy/utils/audio.py#L133-L142)

Implements the Aac audio type matcher.

### *attr* Aac.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 136](../../../../translatepy/utils/audio.py#L136)

### *attr* Aac.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 137](../../../../translatepy/utils/audio.py#L137)

### *func* Aac.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 140-142](../../../../translatepy/utils/audio.py#L140-L142)

#### Parameters

- **data**: `bytes`


## *class* **Aiff**

> [Source: ../../../../translatepy/utils/audio.py @ line 145-161](../../../../translatepy/utils/audio.py#L145-L161)

Implements the AIFF audio type matcher.

### *attr* Aiff.**MIME**

> [Source: ../../../../translatepy/utils/audio.py @ line 149](../../../../translatepy/utils/audio.py#L149)

### *attr* Aiff.**EXTENSION**

> [Source: ../../../../translatepy/utils/audio.py @ line 150](../../../../translatepy/utils/audio.py#L150)

### *func* Aiff.**test**

> [Source: ../../../../translatepy/utils/audio.py @ line 153-161](../../../../translatepy/utils/audio.py#L153-L161)

#### Parameters

- **data**: `bytes`


## *func* **get_type**

> [Source: ../../../../translatepy/utils/audio.py @ line 164-181](../../../../translatepy/utils/audio.py#L164-L181)

Returns the audio format of the given buffer

### Parameters

- **buffer**: `bytes`
  - The audio file data


### Returns

- `Optional[Type]`
    - The type of audio file
