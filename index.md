---
layout: default
title: 📘 CT4110 Flashcards
---

<style>
  .lecture-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 15px;
    margin-top: 15px;
  }
  .lecture-card {
    display: block;
    background: #fff;
    border: 3px solid #ddd;
    border-radius: 12px;
    padding: 30px;
    text-align: center;
    font-size: 1rem;
    transition: all 0.2s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    text-decoration: none;
    color: #0b74ff;
    font-weight: 600;
  }
  .lecture-card:hover {
    border-color: #0b74ff;
    box-shadow: 0 12px 12px rgba(0,0,0,0.3);
    transform: translateY(-3px);
  }
</style>

## 📘 CT4110: Flashcards for the tutorial sessions

### About Flashcards

This is the landing page for the flashcards used as part of the teaching material in the course CT4110. The flashcards shown here consists of `front and back` pairs, or alternatively `questions and answer` pairs, and are used to facilitate and encourage interaction with the cohorts about lecture specific topics.

We will display the card front, and first seek response and thoughts from the cohorts, then we reveal the back side. Remember that the answers themselve aren't that important, as is the discussion and the process of interaction. So please do not try to `learn` the answer beforehand! 😃

<div class="lecture-grid">
  {% for lec in site.material %}
    <a href="{{ lec.url | relative_url }}" class="lecture-card">
      {{ lec.title }}
    </a>
  {% endfor %}
</div>
