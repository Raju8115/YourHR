// tailwind.config.js
module.exports = {
  content: [
    './templates/**/*.html',  // Include all HTML files within the templates directory
    './**/templates/**/*.html', // Include all HTML files in app-level templates directories
    './static/src/**/*.js', // Include all JavaScript files within static/src directory
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

