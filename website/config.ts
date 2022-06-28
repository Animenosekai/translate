const Configuration = {
    request: {
        host: process.env.NODE_ENV === "development" ? "http://127.0.0.1:5001" : "https://anise-translate.herokuapp.com"
    },
    repo: {
        // branch: "website"
        branch: "f1c9a3db0ea71c6f727e37919d0c6cd8f8d15429"
    }
}

export default Configuration