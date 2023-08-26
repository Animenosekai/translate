import { Language } from "./language"
import { Result } from "./result"

type AudioMIMEType =
    | "audio/mpeg"
    | "audio/mp4"
    | "audio/ogg"
    | "audio/x-flac"
    | "audio/x-wav"
    | "audio/amr"
    | "audio/aac"
    | "audio/x-aiff"

type AudioExtension =
    | "mp3"
    | "m4a"
    | "ogg"
    | "flac"
    | "wav"
    | "amr"
    | "aac"
    | "aiff"

type Gender = "male" | "female" | "other" | "genderless"
type base64 = string


export interface TextToSpeechResult extends Result {
    speed: number
    gender: Gender
    mime_type: AudioMIMEType
    extension: AudioExtension
    result: base64 // base64
}
