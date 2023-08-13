const Configuration = {
    request: {
        host: process.env.NODE_ENV === "development" ? "http://127.0.0.1:5001" : "https://anise-translate.herokuapp.com"
    },
    repo: {
        // branch: "website"
        branch: "c0ab2599d6d67847a9dd71a1b809609fb6e6d9b5"
    }
}

export default Configuration