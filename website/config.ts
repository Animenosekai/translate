const Configuration = {
    request: {
        host: `/api`
    },
    origin: typeof window !== "undefined" ? window.location.origin : ""
}

export default Configuration