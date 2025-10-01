# 📘 CT4110: collection of Flashcards for the tutorial session

This is the landing page for the flashcards used as part of the teaching material in the course CT4110. The flashcards shown here consists of `front and back` pairs, or alternatively `questions and answer` pairs, and are used to facilitate and encourage interaction with the cohorts about lecture specific topics.

## Content organization

Following is the structure of content

```bash

.
├── _config.yml             # jekyll configurations
├── _layouts
│   └── cards-template.html # card layout
├── _material               # header files for each card
│   ├── cards-01.md
│   ├── cards-02.md
│   ├── cards-03.md
│   ├── cards-04.md
│   ├── cards-05.md
│   ├── cards-06.md
│   ├── cards-07.md
│   ├── cards-08.md
│   ├── cards-09.md
│   ├── cards-10.md
│   ├── cards-11.md
│   └── cards-12.md
├── assets
│   ├── css                # css style for pretty look
│   │   └── flashcards.css
│   ├── data               # actual flashcard data
│   │   ├── cards_01.json
│   │   ├── cards_02.json
│   │   ├── cards_03.json
│   │   ├── cards_04.json
│   │   ├── cards_05.json
│   │   ├── cards_06.json
│   │   ├── cards_07.json
│   │   ├── cards_08.json
│   │   ├── cards_09.json
│   │   ├── cards_10.json
│   │   ├── cards_11.json
│   │   └── cards_12.json
│   └── js                # javascript that displays the card
│       └── flashcards.js
├── course-flow.drawio
├── Gemfile               # jekyll dependencies
├── index.md              # main page.
├── logo.png              # logo
├── README.md             # this file
├── requirements.txt      # not really required.
```

The files for lectures are named as with suffixes `01, 02, 03 ...`. 

### Card header

The card header is kept under `_material` folder, with pattern `cards-01.md`. It should look like the following, with three keys. One normally just needs to update lecture title, and insure one has corresponding `.json` files in right place.

```yaml
---
layout: cards-template
title: lecture title
jsonfile: /assets/data/cards_01.json
---
```

### Card content

The card content is placed under `assets/data/` as json file with pattern `card_01.json`. It should look like following -

```json
[
    {
        "front": "What is Moore's law and how is it relevant to quantum computing? ",
        "back": "Moore's law states that the number of transistors on a microprocessor doubles approximately every two years. When we make transistors smaller and smaller (to squeeze more in to a microchip), their behaviour is only accurately described by quantum physics."
    },
    {
        "front": "Discuss the similarities in the features of classical and quantum computing",
        "back": "Both require the existence of independent states like the 0 and 1 state. Gates are used to manipulate the information in both cases. Both have universal gate sets."  
    }
]
```

The structure of json file is a list of dictionaries, each of which have two keys 1. `front` and 2. `back` with string values. These values are displayed as front and back of the card. 

- Latex in the values is supported, atleast inline latex `$ expression $` with following caveat. JSON parser will have trouble if it finds escape characters, so extra '\' is needed. For example 
  - following wouldn't work under the string 
    ```markdown
        The state $|s\rangle = c_1|1\rangle + c_2|2\rangle + ... c_n|n\rangle$ 
    ```
  - But following would work
    ```markdown
        The state $|s\\rangle = c_1|1\\rangle + c_2|2\\rangle + ... c_n|n\\rangle$ 
    ```

- One can insert markdown image such as `![](./path/to/some/image.png)` though not yet tested.


### Running locally

To test, view the rendered page locally, get familiar with Ruby Gems, install `bundle` package using

```bash
gem install bundler jekyll # install gem as well via `brew install gem` if not installed

cd this-repo # chdir to this repo folder

bundle exec jekyll serve # => Now browse to http://localhost:4000 
```

The last command will serve a web page locally where you can see the pages.