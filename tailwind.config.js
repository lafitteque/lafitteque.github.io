module.exports = {
	daisyui: {
		themes: [
			{
				light: {
					primary: '#ffffff',
					secondary: "#fafafa",
					result: "#ede6af",
					methode: "#e0e0e0",
					definition:"#ccf5cc",
					thborder:"#b64b4b",
					propborder:"#db9224",
					corborder:"#56b0d3",
					defborder:"#b0d5b0",
					methborder:"#a0a0a0",
			},
		},
		],
	},
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	
	plugins: [
		require('daisyui'),
	],
}
