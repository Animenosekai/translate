module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        'enter-modal': 'enter-modal 300ms ease 1',
      },
      keyframes: {
        'enter-modal': {
          '0%': {
            opacity: 0,
            backgroundColor: 'rgba(255, 255, 255, 0)',
          },
          '100%': {
            opacity: 1,
            backgroundColor: 'rgba(255, 255, 255, 0.7)',
          }
        }
      },
    },
    plugins: [],
  }
}