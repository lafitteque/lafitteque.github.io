module.exports = {
	content: [
	  "./src/**/*.{html,js,astro,ts,svelte,vue}",
	  "./components/**/*.{html,js,astro,ts,svelte,vue}"
	],
	theme: {
	  extend: {
		colors: {
		  // Utilisation de fonctions JavaScript pour manipuler les couleurs
		  definition: ({ theme }) => {
			return theme('colors.success.DEFAULT', 'var(--color-success)');
		  },
		  proposition: ({ theme }) => {
			return theme('colors.warning.DEFAULT', 'var(--color-warning)');
		  },
		  theoreme: ({ theme }) => {
			return theme('colors.error.DEFAULT', 'var(--color-error)');
		  },
		  methode: ({ theme }) => {
			return theme('colors.neutral.DEFAULT', 'var(--color-neutral-content)');
		  },
		},
		fontFamily: {
		  serif: ['serif'],
		},
		fontSize: {
		  '2xl': '12.5rem',
		},
	  },
	},
	plugins: [
	  require('daisyui'),
	  // Plugin pour ajouter des variables CSS personnalisées
	  function({ addBase, theme }) {
		addBase({
		  ':root': {
			'--definition': 'color-mix(in oklab, var(--color-success) 95%, black 5%)',
			'--proposition': 'color-mix(in oklab, var(--color-warning) 95%, black 5%)',
			'--theoreme': 'color-mix(in oklab, var(--color-error) 95%, black 5%)',
			'--methode': 'color-mix(in oklab, var(--color-neutral-content) 80%, black 20%)',
			'--definition-bis': 'color-mix(in oklab, var(--color-success) 70%, black 30%)',
			'--proposition-bis': 'color-mix(in oklab, var(--color-warning) 70%, black 30%)',
			'--theoreme-bis': 'color-mix(in oklab, var(--color-error) 70%, black 30%)',
			'--methode-bis': 'color-mix(in oklab, var(--color-neutral-content) 50%, black 50%)',
		  }
		});
	  }
	],
	daisyui: {
	  // Vos paramètres daisyUI ici
	}
  }
