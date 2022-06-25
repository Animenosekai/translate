const Configuration = {
    request: {
        host: process.env.NODE_ENV === "development" ? "http://127.0.0.1:5001" : "https://anise-translate.herokuapp.com"
    },
    repo: {
        // branch: "website"
        branch: "59d190ee0972ab8a0cb56c69c793063869f1ae5d"
    }
}

export default Configuration