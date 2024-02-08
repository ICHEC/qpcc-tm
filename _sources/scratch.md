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
```

```{code-cell} ipython3
:tags: ['remove-input']
from jupytercards import display_flashcards
display_flashcards('./material/cards_1.json', front_colors=["beige"], back_colors=["cyan"], text_colors=["black"])
```


#### 1
````{dropdown} How does quantum computing (QC) fit alongside classical high-performance computing (HPC) systems & applications?
```{card} Answer
QC will serve as an accelerator in HPC for specific parts of an application, leading to hybrid HPC-QC systems & applications.
```
````

#### 2
````{dropdown} What types of problems can quantum computing (QC) solve better than classical high-performance computing (HPC)?
```{card} Answer
Problems with approximations to address intractability, reducing precision when scaling complexity, simulate models which are related to quantum mechanics, etc..
```
````

#### 3
````{dropdown} How would you define your role & value in quantum computing (QC)?
```{card} Answer
This is best defined in discussion with experts in quantum computing systems & applications. Opportunities lie in end-user applications, co-development of technologies, ecosystem leadership, skills & training, etc..
```
````

#### 4
````{dropdown} What are key tipping points or milestones for quantum computing (QC) to become more reliable & scalable?
Improved noise & reliability in qubits & quantum gates, precision in control & engineering of quantum systems, integration of classical HPC & QC systems, higher-level software tools integrated with classical software tools.
```
````

#### 5
````{dropdown} Do quantum computers always need to be refridgerated and operated at extremely low temperatures?
```{card} Answer
No all quantum computer realisation methods require refridgeration and operation at extremely low temperatures. For instance, the superconducting approach requires refridgeration, while photonics or diamond-based approaches may be operated at room temperature.
```
````

#### 6
````{dropdown} If real NISQ devices are already available for free access, then do we need software-based simulators of quantum computers?
```{card} Answer
Currently available NISQ devices are extremely small and error-prone. Thus, programming them requires expertise in optimisation and customisation that is device-/vendor-specific. Software-based simulators on the other hand, allow for easier experimentation and skills development before using real hardware. Thus, beginning the learning and development process from software simulators before moving to NISQ hardware devices has proven helpful in the current scenario.
```
````

#### 7
````{dropdown} How or where can you start your engagement with quantum computing?
```{card} Answer
Investigate potential use-cases of interest, mechanisms for skills development, partners for collaborations & discussion, national & international programmes in which to participate, etc..
```
````

---

```{code-cell} ipython3
:tags: ['remove-input']

import json
with open("./material/cards_1.json") as f:
    dic = json.load(f)
ss = ''
for i, d in enumerate(dic):
    que, ans = d['front'], d['back']
    ss += '(c' + str(i+1) + ')=\n'
    ss += "## " + str(i+1) + '\n``````{dropdown} ' + que
    ss += '\n```{card} Answer\n'
    ss += ans + '\n```\n``````\n\n'
from IPython.display import display, Markdown
display(Markdown(ss))
#print(ss)
```

