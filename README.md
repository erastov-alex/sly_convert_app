<div align="center" markdown>

<img src="https://i.ibb.co/6HfvSff/dataset-app.png"/>

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-to-Use">How to Use</a> •
  <a href="#Test">Tests</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://https://supervisely.com/)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)

</div>

# Overview

Supervisely app for import datasets in supported formats. App based on Supervisely SDK and [DS Manager for CV](https://github.com/erastov-alex/sly-convert).

#### Input files structure

Only folder with dataset. Before using read [Strict data format rule](https://github.com/erastov-alex/sly-convert#strict-data-format-rule)

# How to Run

**Step 1.** Set your supervisely envirement using [this](https://developer.supervisely.com/getting-started/environment-variables) instruction

**Step 2.** Clone this repository to your local folder

**Step 3.** Run app in debug mode using settings.json

**Step 4.** Go to localhost:8000 to use this app

**Step 5.** Drag'n'Drop your dataset. If your dataset contain PNG masks use input box to insert image's folder name. Click 'Scan' button

**Step 6.** Create project in Supervisely and click 'Import' button

### About DS Manager for CV

We use [DS Manager for CV](https://github.com/erastov-alex/sly-convert) for this app. Read more about on GitHub page.

#Tests

[This](https://github.com/erastov-alex/dataset_samples) tests passed.
