/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../blog/templates/**/*.html',     // all templates in your app
    '../blog_center/templates/**/*.html',
    '../static/js/**/*.js',            // optional if you have JS using Tailwind classes
    '../templates/*.html',
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./static/**/*.js",
    "./**/*.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
