/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Red theme inspired by transparently.ai
        primary: {
          light: '#FCA5A5',  // Light Red
          DEFAULT: '#EF4444', // Red
          dark: '#991B1B',    // Deep Red
        },
        accent: {
          red: '#DC2626',
          lightRed: '#FEE2E2',
        },
        background: {
          DEFAULT: '#FFFFFF',
          secondary: '#F9FAFB',
          dark: '#1F2937',
        },
        text: {
          primary: '#111827',
          secondary: '#6B7280',
          light: '#9CA3AF',
        }
      },
      borderRadius: {
        xl: '1rem',
        '2xl': '1.5rem',
      },
      boxShadow: {
        'soft': '0 2px 8px rgba(0, 0, 0, 0.08)',
        'medium': '0 4px 12px rgba(0, 0, 0, 0.12)',
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.4s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
