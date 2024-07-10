const { nextui } = require("@nextui-org/react");

module.exports = {
    content: [
        "./pages/**/*.{js,ts,jsx,tsx}",
        "./components/**/*.{js,ts,jsx,tsx}",
        "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}"
    ],
    theme: {
        extend: {
            animation: {
                'enter-modal': 'enter-modal 300ms ease 1',
                'loading-blink': 'loading-blink 1.5s infinite both'
            },
            keyframes: {
                'enter-modal': {
                    '0%': {
                        opacity: 0,
                        backgroundColor: 'rgba(255, 255, 255, 0)',
                    },
                    '100%': {
                        opacity: 1,
                        backgroundColor: 'rgba(255, 255, 255, 0.8)',
                    }
                },
                'loading-blink': {
                    "0%": {
                        opacity: "0.2",
                    },
                    "20%": {
                        opacity: 1,
                    },
                    "100%": {
                        opacity: "0.2",
                    },
                }
            },
        },
    },
    darkMode: "class",
    plugins: [nextui()]
}