---
layout: default
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
  .exercise-list {
    display: grid;
    gap: 12px;
    margin-top: 15px;
  }
  #exercises-for-ct-4100 {
    margin-top: 4rem;
    scroll-margin-top: 1.5rem;
  }
  .section-shortcuts {
    display: flex;
    gap: 10px;
    margin: 20px 0 28px;
  }
  .section-shortcut {
    background: #0b74ff;
    border-radius: 8px;
    color: #fff;
    display: inline-block;
    font-weight: 600;
    padding: 10px 16px;
    text-decoration: none;
  }
  .section-shortcut:hover {
    background: #095ac7;
    color: #fff;
  }
  .exercise-item {
    align-items: center;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    display: flex;
    gap: 16px;
    justify-content: space-between;
    padding: 18px 20px;
  }
  .exercise-title {
    font-weight: 600;
  }
  .exercise-actions {
    display: flex;
    flex-shrink: 0;
    gap: 8px;
  }
  .exercise-button {
    border: 1px solid #0b74ff;
    border-radius: 7px;
    color: #0b74ff;
    padding: 7px 12px;
    text-decoration: none;
  }
  .exercise-button.primary {
    background: #0b74ff;
    color: #fff;
  }
  .exercise-button:hover {
    background: #095ac7;
    color: #fff;
  }
  @media (max-width: 520px) {
    .exercise-item {
      align-items: stretch;
      flex-direction: column;
    }
  }
</style>

<div class="section-shortcuts">
  <a class="section-shortcut" href="#exercises-for-ct-4100">Go to Exercises ↓</a>
</div>

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




## Exercises for CT-4110

The exercises are available to view in your browser or download as Jupyter notebooks.

{% assign notebooks = site.static_files | where: "extname", ".ipynb" | sort: "path" %}
<div class="exercise-list">
  {% for notebook in notebooks %}
    {% if notebook.path contains '/exercises/' %}
      {% assign filename = notebook.name %}
      {% assign configured_title = site.data.exercise_titles[filename] %}
      {% if configured_title %}
        {% assign exercise_name = configured_title %}
      {% else %}
        {% assign exercise_name = filename | remove: '.ipynb' | replace: '-', ' ' | replace: '_', ' ' | capitalize %}
      {% endif %}
      {% assign rendered_path = '/rendered-exercises/' | append: filename | replace: '.ipynb', '.html' %}
      <div class="exercise-item">
        <span class="exercise-title">{{ exercise_name }}</span>
        <span class="exercise-actions">
          <a class="exercise-button primary" href="{{ rendered_path | relative_url }}">View</a>
          <a class="exercise-button" href="{{ notebook.path | relative_url }}" download>Download</a>
        </span>
      </div>
    {% endif %}
  {% else %}
    <p>Exercises will be added here soon.</p>
  {% endfor %}
</div>
