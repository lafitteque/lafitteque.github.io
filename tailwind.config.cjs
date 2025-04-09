module.exports = {
	content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
	theme: {
		extend: {
		  colors: {
			primary: '#ffffff',
			antiprimary: '#000000',
			secondary: "#fafafa",
			tertiary: "#cccccc",
			result: "#ede6af",
			methode: "#e0e0e0",
			definition:"#ccf5cc",
			thborder:"#b64b4b",
			propborder:"#db9224",
			corborder:"#56b0d3",
			defborder:"#b0d5b0",
			methborder:"#a0a0a0",
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
	],
}
