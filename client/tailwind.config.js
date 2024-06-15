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
          sidebar: 'var(--sidebar-bg)',
        },
        txt: {
          editor: 'var(--editor-txt)',
          detail: 'var(--detail-txt)',
          note: 'var(--note-txt)',
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
