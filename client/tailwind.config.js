/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"IBM Plex Sans"', 'sans-serif'],
        mono: ['"IBM Plex Mono"', 'monospace'],
      },
      colors: {
        brand: {
          main: '#448CC2',
          accent: '#62B2E9',
        },
        background: {
          main: 'var(--main-bg)',
          sidebar: 'hsl(var(--sidebar-bg) / <alpha-value>)',
        },
        txt: {
          editor: 'hsl(var(--editor-txt) / <alpha-value>)',
          detail: 'hsl(var(--detail-txt) / <alpha-value>)',
          note: 'hsl(var(--note-txt) / <alpha-value>)',
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
