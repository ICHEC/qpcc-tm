#!/usr/bin/env python3
"""Render exercise notebooks to HTML with a notebook download link."""

from html import escape
from pathlib import Path
from urllib.parse import quote

import nbformat
from nbconvert import HTMLExporter


SOURCE_DIR = Path("exercises")
OUTPUT_DIR = Path("rendered-exercises")


def download_bar(filename: str) -> str:
    download_url = f"../exercises/{quote(filename)}"
    return f"""
<style>
  .exercise-download-bar {{
    background: #fff;
    border-bottom: 1px solid #ddd;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    padding: 12px 24px;
  }}
  .exercise-download-link {{
    color: #0b74ff;
    font-weight: 600;
    text-decoration: none;
  }}
  .exercise-download-link:hover {{
    color: #095ac7;
    text-decoration: underline;
  }}
</style>
<div class="exercise-download-bar">
  <span>Want to work on this exercise locally or in Colab?</span>
  <a class="exercise-download-link" href="{download_url}" download
     aria-label="Download {escape(filename)}">
    Download the Jupyter notebook ⬇
  </a>
</div>
"""


def render_notebook(notebook_path: Path, exporter: HTMLExporter) -> None:
    notebook = nbformat.read(notebook_path, as_version=4)
    html, _ = exporter.from_notebook_node(notebook)

    body_start = html.find("<body")
    body_end = html.find(">", body_start)
    if body_start == -1 or body_end == -1:
        raise ValueError(f"Could not find the HTML body in {notebook_path}")

    html = html[: body_end + 1] + download_bar(notebook_path.name) + html[body_end + 1 :]
    output_path = OUTPUT_DIR / f"{notebook_path.stem}.html"
    output_path.write_text(html, encoding="utf-8")
    print(f"Rendered {notebook_path} -> {output_path}")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    exporter = HTMLExporter(template_name="lab")
    for notebook_path in sorted(SOURCE_DIR.glob("*.ipynb")):
        render_notebook(notebook_path, exporter)


if __name__ == "__main__":
    main()
