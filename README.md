<div align="center" markdown>

<img src="https://i.ibb.co/LkNcFxR/DS-MANAGER-SLY.png"/>

# Import Dataset in COCO/Yolo/Cityscapes/PascalVOC format

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

You can upload a directory or an archive. If you are uploading an archive, it must contain a single top-level directory.

Directory name defines project name. Subdirectories define dataset names.

Project directory example:

```
.
cats_vs_dogs_project
├── cats
│   ├── ann
│   │   ├── cats_1.jpg.json
│   │   ├── ...
│   │   └── cats_9.jpg.json
│   └── img
│       ├── cats_1.jpg
│       ├── ...
│       └── cats_9.jpg
├── dogs
│   ├── ann
│   │   ├── dogs_1.jpg.json
│   │   ├── ...
│   │   └── dogs_9.jpg.json
│   └── img
│       ├── dogs_1.jpg
│       ├── ...
│       └── dogs_9.jpg
└── meta.json
```

As a result we will get project `cats_vs_dogs_project` with 2 datasets named: `cats` and `dogs`.

# How to Run

**Step 1.** Set your supervisely envirement using [this](https://developer.supervisely.com/getting-started/environment-variables) instruction

**Step 2.** Clone this repository to your local folder

**Step 3.** Run app in debug mode using settings.json

**Step 4.** Go to localhost:8000 to use this app

**Step 5.** Drag'n'Drop your dataset and click 'Scan' button

**Step 6.** Create project in Supervisely and click 'Import' button

### About DS Manager for CV

We use [DS Manager for CV](https://github.com/erastov-alex/sly-convert) for this app. Read more about on GitHub page.
