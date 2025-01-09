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
  "\\U": "\\mathbb{U}",
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

  "\\Point": "\\Big( { #1 } \\v { #2 } \\Big)",

  "\\defoo": "\\big] {#1} \\v {#2} \\big[",
  "\\defff": "\\big[ {#1} \\v {#2} \\big]",
  "\\defof": "\\big] {#1} \\v {#2} \\big]",
  "\\deffo": "\\big[ {#1} \\v {#2} \\big[",

  "\\deftan": "\\R \\setminus \\{ \\dfrac{\\pi}{2} + k\\pi \\mid k \\in \\Z \\}",
  "\\deftanprincipal": "\\big] -\\dfrac{\\pi}{2} \\v \\dfrac{\\pi}{2}\\big[",
  "\\defprincipale": "\\big] - \\pi \\v \\pi \\big]",
  "\\defrad": "\\big[ 0 \\v 2\\pi \\big[",

  "\\defunitoo": "\\big] 0 \\v 1\\big[",
  "\\defunitfo": "\\big[ 0 \\v 1\\big[",
  "\\defunitof": "\\big] 0 \\v 1\\big]",
  "\\defunitff": "\\big[ 0 \\v 1\\big]",

  "\\defentiersn": "\\llbracket 1 \\v n\\rrbracket",
  "\\defentiers": "\\llbracket {#1} \\v {#2} \\rrbracket",

  "\\ssi": "\\Leftrightarrow",

  "\\pv": "; \\;",
  "\\v": ", \\;",

  "\\somme": "\\sum \\limits_{#1}^{#2}",
  "\\produit": "\\prod \\limits_{#1}^{#2}",
  "\\integ": "\\int \\limits_{#1}^{#2}",

  "\\limm": "\\lim \\limits_{ {#1} }",

  "\\Re": "\\operatorname{Re}",
  "\\Im": "\\operatorname{Im}",
  "\\Arg": "\\operatorname{Arg}",
  "\\Ker": "\\operatorname{Ker}",
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
