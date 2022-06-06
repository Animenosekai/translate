module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        'enter-modal': 'enter-modal 300ms ease 1',
        'enter-menu': 'enter-menu 300ms ease 1',
        'exit-menu': 'enter-menu 300ms ease 1 reverse',
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
        'enter-menu': {
          '0%': {
            opacity: 0,
            transform: "translateX(100%)"
          },
          '100%': {
            opacity: 1,
            transform: "translateX(0%)"
          }
        }
      },
    },
    plugins: [],
  }
}