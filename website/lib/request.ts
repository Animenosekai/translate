import Configuration from "../config"

type HTTPMethods = "GET" | "POST" | "DELETE"

interface RequestOptions {
    method?: HTTPMethods
    params?: object
    headers?: object
    form?: FormData
    authenticated?: boolean
    token?: string
    // text?: boolean // only for requestMedia
    // arrayBuffer?: boolean // only for requestMedia
}

export function prepare(path: string, options: RequestOptions) {
    /* Prepares a request */
    // const { token } = useAccounts();
    const headers = (options.headers || {})
    // if (options.authenticated !== undefined ? options.authenticated : true) {
    //     try {
    //         headers["Authorization"] = options.token || await config.getItem("animeterebi-account-accounts-value")[parseInt(await config.getItem("animeterebi-account-index-value"))]
    //     } catch (e) {
    //         // no account
    //     }
    // }
    const paramsArray: string[] = [];
    const params = (options.params || {})
    for (const key in params) {
        paramsArray.push(`${encodeURIComponent(key)}=${encodeURIComponent(params[key])}`)
    }

    try {
        const url = new URL(path)
        path = url.pathname
    } catch (e) {
        // no url
    }
    const pathSplit = path.split("/")
    const paramsString =
        paramsArray.length > 0
            ? ((pathSplit[pathSplit.length - 1].includes("?")
                ? "&"
                : "?")
                + paramsArray.join("&"))
            : ""
    return ({
        finalPath: (!path.startsWith("/") ? "/" : "") + path + paramsString,
        headers: headers as HeadersInit,
    })
}

export async function request<Data = any>(path: string, { ...options }: RequestOptions = {}): Promise<Data> {
    /* Make a request to the API server */
    const { finalPath, headers } = prepare(path, options)
    return window.fetch(Configuration.request.host + finalPath, {
        method: options.method || "GET",
        headers: headers,
        body: options.form
    })
        .then(async (resp) => {
            const data = await resp.json();
            // if (!data.success) {
            //     throw new Error(data.error);
            // }
            return data as Data;
        })
}
