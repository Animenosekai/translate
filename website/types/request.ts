export interface Request<T = { [key: string]: any }> {
    success: boolean
    message?: string
    error?: string
    data: T
}