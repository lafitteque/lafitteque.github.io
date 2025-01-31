import { createEffect, createSignal, For, type JSX } from "solid-js";

import "./TableOfContent.css";

export interface TableOfContentProps {
  title: string;
}
const titlesChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function getInput(c: number, indent: number) {
  if (indent === 1) {
    return titlesChar[c - 1];
  }
  return `${c}`;
}

const depthFromNode = {
  H2: 0,
  H3: 1,
  H4: 2,
};
class Prefixer {
  counts: number[] = []; // [1,1.A,1.A.1,   1]

  getPrefix(depth = 0) {
    if (!this.counts[depth]) {
      this.counts.push(0);
    }

    this.counts[depth] += 1;
    this.counts = this.counts.slice(0, depth + 1);
    return this.counts.map(getInput).join(".") + " ";
  }
}
interface TitleContent {
  title: string;
  id: string;
  depth: number;
}
export default function TableOfContent(p: TableOfContentProps) {
  const [list, setList] = createSignal<TitleContent[]>([]);

  createEffect(() => {
    const titles = document.querySelectorAll<HTMLHeadingElement>("h2,h3,h4");

    const prefixer = new Prefixer();

    const resultTitles: TitleContent[] = [];
    for (const title of titles) {
      const depth: number =
        depthFromNode[title.nodeName as keyof typeof depthFromNode];
      const prefix = prefixer.getPrefix(depth);
      const titleStr = prefix + title.innerHTML;
      resultTitles.push({
        id: title.id,
        title: titleStr,
        depth,
      });
    }
    setList(resultTitles);
  });

  return (
    <div>
      <For each={list()}>
        {(item) => {
          return (
            <div class={`toc-${item.depth} hover:text-tertiary`}>
              <a
                onclick={(e) => {
                  e.preventDefault();
                  const el = document.querySelector("#" + item.id);
                  if (!el) return;
                  el.scrollIntoView({
                    behavior: "smooth",
                  });
                }}
                href={`#${item.id}`}
              >
                {item.title}
              </a>
            </div>
          );
        }}
      </For>
    </div>
  );
}
