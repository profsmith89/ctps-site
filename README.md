# ctps-site
Website for my Computational Thinking and Problem Solving (CTPS) book.

`index.html`: Homepage for `ctps.io`.

`select_ide.html`: An html page that helps a reader to understand what
is an IDE and how to select one. It links to Google Docs that explain
how to get started with my recommended IDEs.

`faq.html`: A placeholder html page for FAQs. It might be better as
another publicly accessible Google Doc.

`ales`: A directory with the ALE html files, which I created using
JupyterBook and copied from my `Books` directory.

`style.css`: Style sheet for site.

`script.js`: Javascripts used on the site.

`_config.yml`, `CNAME`: ??? Used by github pages?


**Temporary files** -- Experiments where I tried to find a boxing and
syntax highlighting for code blocks that I liked. The `prism.js` package
worked best, but I still didn't like the result.

`testing/prism.js`, `testing/themes/prism.js`: Files I downloaded
from the `prism.js` site.

`testing/chap01.md`: A test markdown file based on the source material
for the ALEs in CTPS Chapter 1.

`testing/ale.hmtl`: A HTML file that loads a markdown file (specifically
`chap01.md`), uses `marked.js` to render it as HTML, and applies syntax
highlighting using `prism.js`. In the end, I didn't like the syntax
highlighting.

`test_prism.html`: Experimenting with `prism.js` for the formatting
of code snippets. This seemed like a better approach than `highlight.js`.

`test_highlight.html`: Experimenting with `highlight.js`. My biggest
issue with this package is that it doesn't support (and is religously
against) line numbers.
