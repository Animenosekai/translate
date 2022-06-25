/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    async redirects() {
        return [{
            source: '/documentation',
            destination: '/documentation/translatepy',
            permanent: false,
        }, ]
    },
}

module.exports = nextConfig