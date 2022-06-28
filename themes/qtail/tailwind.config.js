module.exports = {
  content: ["content/**/*.md", "layouts/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        varelaRound: "'Varela Round Regular', 'sans', 'serif'",
        'sans': [
          "'-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'Noto Sans', 'sans-serif', 'Apple Color Emoji','Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji',"
        ],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
