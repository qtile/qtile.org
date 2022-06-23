module.exports = {
  content: ["content/**/*.md", "layouts/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        varelaRound: "'Varela Round Regular', 'sans', 'serif'",
        'sans': ["'ui-sans-serif', ..."],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
