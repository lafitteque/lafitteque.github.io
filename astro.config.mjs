import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

const macros = {
  "\\N": "\\mathbb{N}",
  "\\Z": "\\mathbb{Z}",
  "\\D": "\\mathbb{D}",
  "\\Q": "\\mathbb{Q}",
  "\\R": "\\mathbb{R}",
  "\\C": "\\mathbb{C}",
  "\\K": "\\mathbb{K}",
  "\\L": "\\mathbb{L}",

  "\\cA": "\\mathscr{A}",
  "\\cB": "\\mathscr{B}",
  "\\cC": "\\mathscr{C}",
  "\\cD": "\\mathscr{D}",
  "\\cE": "\\mathscr{E}",
  "\\cF": "\\mathscr{F}",
  "\\cM": "\\mathscr{M}",
  "\\cN": "\\mathscr{N}",
  "\\cP": "\\mathscr{P}",
  "\\cT": "\\mathscr{T}",

  "\\ssi": "\\Leftrightarrow",
  "\\pv": "; \\;",
  "\\overvar": "",
  "\\vect": "\\mathbf{#1}",
};

export default defineConfig({
  markdown: {
    shikiConfig: {
      theme: "dracula",
      wrap: false,
    }
  },
  site: 'https://lafitteque.github.io',
  integrations: [
    mdx({
      remarkPlugins: [remarkMath],
      rehypePlugins: [
        [
          rehypeKatex,
          {
            output: 'html',  // Désactiver MathML
            macros: macros,  // Ajouter tes macros ici
          }
        ]
      ]
    }),
  ],
});
