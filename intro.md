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

# CT4110: collection of Flashcards for the tutorial session

```{admonition} About flashcards
:class: note
This is the landing page for the flashcards used as part of the teaching material in the course CT4110. The flashcards shown here consists of `front and back` pairs, or alternatively `questions and answer` pairs, and are used to facilitate and encourage interaction with the cohorts about lecture specific topics.

We will display the card front, and first seek response and thoughts from the cohorts, then we reveal the back side. Remember that the answers themselve aren't that important, as is the discussion and the process of interaction. So please do not try to `learn` the answer beforehand! 😃

We have also added a dropdown list version of the same card below in the page.
```


```{code-cell} ipython3
:tags: ['remove-input']
ss = ''
for i in range(1,13):
    fl = './material/cards-' + f"{i:02d}" + '.md'
    with open(fl) as f:
        txt = f.read()
    title = [l for l in txt.splitlines() if l.startswith('# ')][0][2:]
    ss += f"- [{title}]({fl})" + '\n'
from IPython.display import display, Markdown
display(Markdown(ss))
```
