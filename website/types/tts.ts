import { Request } from "./base"

export interface TTSRequest extends Request {
    data: TTSResult
}

export interface TTSResult {
    base64: string
}
