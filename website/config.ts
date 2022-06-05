const Configuration = {
    request: {
        host: process.env.NODE_ENV ? "http://127.0.0.1:5000" : "https://translate.herokuapp.com"
    }
}

export default Configuration