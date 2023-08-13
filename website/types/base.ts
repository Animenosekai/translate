export interface Request {
    success: boolean
    message?: string
    error?: string
    data: { [key: string]: any }
}