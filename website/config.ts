const Configuration = {
    request: {
        host: process.env.NODE_ENV === "development" ? "http://127.0.0.1:5001" : "https://anise-translate.herokuapp.com"
    }
}

export default Configuration