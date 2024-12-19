import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
export default defineConfig({
  build: {
    format: 'directory', // Crée une structure de fichiers et dossiers
  },
  site: 'https://lafitteque.github.io',
  base: '', 
  integrations: [mdx()],
});