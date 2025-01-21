import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import solidJs from '@astrojs/solid-js';

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
  "\\indicatrice": "\\mathbb{1}",

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
  "\\cR": "\\mathscr{R}",

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

  "\\floor": "\\lfloor {#1} \\rfloor",
  "\\ceil": "\\lceil {#1} \\rceil",

  "\\somme": "\\sum \\limits_{#1}^{#2}",
  "\\produit": "\\prod \\limits_{#1}^{#2}",
  "\\integ": "\\int \\limits_{#1}^{#2}",

  "\\limm": "\\lim \\limits_{ {#1} }",
  "\\limto":"\\mathop{\\longrightarrow}\\limits_{ {#1} \\to {#2}}",
  "\\limton":"\\mathop{\\longrightarrow}\\limits_{n \\to \\infty}",
  "\\suitedef":"({#1})_{n \\in {#2}}",
  "\\suitedefN":"({#1})_{n \\in \\N}",

  "\\Re": "\\operatorname{Re}",
  "\\Im": "\\operatorname{Im}",
  "\\Arg": "\\operatorname{Arg}",
  "\\Ker": "\\operatorname{Ker}",
  "\\sup": "\\operatorname{sup}",
  "\\inf": "\\operatorname{inf}",
};

export default defineConfig({
  markdown: {
    shikiConfig: {
      theme: "dracula",
      wrap: false,
    }
  },
  server: { host: true },
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
    solidJs()
  ],
});
