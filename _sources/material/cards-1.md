---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
mystnb:
  render_markdown_format: myst
---

# Lecture 1: Demystifying Quantum Computing

```{admonition} Lecture 1
The flash card below is part of the discussion in the tutorial session of lecture 1.

Here we display the card front, and first seek response and thoughts from the cohorts, then we reveal the back side. Remember that the answers themselve aren't that important, as is the discussion and the process of interaction. So please do not try to `learn` the answer beforehand! 😃

We have also added a dropdown list version of the same card below in the page.
```

## Flashcards
```{tip}
Click the Card below to reveal the answer.
```

```{code-cell}
:tags: ['remove-input']
from jupytercards import display_flashcards
display_flashcards('./cards_1.json', front_colors=["beige"], back_colors=["cyan"], text_colors=["black"])
```

## Alternative lists

```{code-cell} ipython3
:tags: ['remove-input']
import json
with open("./cards_1.json") as f:
    dic = json.load(f)
ss = ''
for i, d in enumerate(dic):
    que, ans = d['front'], d['back']
    ss += '(c' + str(i+1) + ')=\n'
    ss += "### " + str(i+1) + '\n``````{dropdown} ' + que
    ss += '\n```{card} Answer\n'
    ss += ans + '\n```\n``````\n\n'
from IPython.display import display, Markdown
display(Markdown(ss))
```
