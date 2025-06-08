# Airoh Template: Reproducible Pipelines Made Simple

_why don't you have a cup of relaxing jasmine tea?_

This repository provides a minimal, modular, and **fully reproducible** template for scientific workflows. Built on the [`invoke`](https://www.pyinvoke.org/) task runner, [datalad](https://www.datalad.org/) for data management as well as containerization tools (Docker or Apptainer), it lets you go from clean clone to output figures with just a few commands.

The logic is powered by [`airoh`](https://pypi.org/project/airoh/), a lightweight, pip-installable Python package of reusable `invoke` tasks. This repository runs small analyses just to demonstrate how the `airoh-template` works. It should be easy to adapt to a variety of other projects.

⚠️ **Status**: This template is in its early days. Expect rapid iteration and changes.

---

## ✨ TL;DR:

This repository is a [GitHub template](https://github.com/airoh-pipeline/airoh-template/generate). Click **“Use this template”** to create your own analysis project.
```bash
pip install -r setup.txt
invoke setup
invoke fetch
invoke run
```
Voilà — from clone to full reproduction.

---

## 🚀 Quick Start

### **Step 1**: Install `invoke` and clone core airoh dependencies

```
bash
pip install -r setup.txt
```

---

### **Step 2**: Fetch the source data

```
bash
invoke fetch
```

This uses Datalad under the hood to retrieve the configured file(s) listed in `invoke.yaml`.

---

### **Step 3**: Run the analysis pipeline

```
bash
invoke run
```

This will execute a full analysis pipeline (simulation + figures).

---

### **Step 4**: Build and archive a Docker image (optional)

If you want to freeze the environment:

```
bash
invoke docker-build
invoke docker-archive
```

This will save your image to a `.tar.gz` archive that can later be loaded with `docker-setup`:

```
bash
invoke docker-setup 
```
Note that the name of the docker image is configured through `invoke.yml`.

---

### **Step 5**: Run inside container (optional)

Once built or loaded:

```
bash
invoke docker-run --task run
```

This re-runs your pipeline inside the container.

---

### **Step 6**: Clean output data

```
bash
invoke clean
```

Removes the output folder listed in `invoke.yaml` under `output_data_dir`.

---

## 🧠 Core Features

* Modular `tasks.py` that imports reusable code from `airoh`
* Minimal and readable `invoke.yaml` configuration file
* Optional containerization for full reproducibility
* Real output notebooks & figures — ready to publish

---

## 📦 Using Datalad for Large Files

This template supports `datalad` to manage large assets (e.g., Docker images, datasets). To avoid bloating your Git repository:

1. Make sure the repo is initialized with Datalad:

   ```bash
   datalad create --force
   ```

2. Make sure `.gitattributes` is configured to match your needs. For example, this template excludes large Docker archives using:

   ```text
   *.tar.gz annex.largefiles=(largerthan=10MB)
   ```

3. Add and save your large files with:

   ```bash
   datalad add output_data/your-archive.tar.gz
   datalad save -m "Added archive with git-annex"
   ```

4. To verify that the file is tracked by `git-annex`, run:

   ```bash
   git annex whereis output_data/your-archive.tar.gz
   ```

If you're working with Zenodo or other public sources, you can also configure `invoke.yaml` to fetch and extract archives via `invoke fetch`.

You can add entries under the `files:` section in `invoke.yaml` to automate downloads using `invoke fetch`.

By default, the template excludes `source_data/` and `output_data/` from Git. If you prefer to track them, you can manage them with Datalad instead.

---

## 🧰 Task Overview

| Task             | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| `setup`          | Installs Python dependencies from `requirements.txt`           |
| `fetch`          | Downloads dataset using Datalad and config in `invoke.yaml`    |
| `run`            | Executes Jupyter notebooks for each figure                     |
| `clean`          | Removes the `output_data_dir` contents                         |
| `docker-build`   | Builds a Docker image from the current repo                    |
| `docker-archive` | Archives the Docker image into a `.tar.gz` for sharing         |
| `docker-setup`   | Loads a prebuilt image from a `.tar.gz` archive (e.g., Zenodo) |
| `docker-run`     | Runs any task inside the Docker image                          |

Use `invoke --list` or `invoke --help <task>` for descriptions and usage.

---

## 🧭 Tips

* Use `invoke --complete` for tab-completion support
* Configure paths and data sources in `invoke.yaml`
* To use this template for a new project, start from [`airoh-template`](https://github.com/SIMEXP/airoh-template) and customize `tasks.py` + `invoke.yaml`

---

## 📁 Folder Structure

| Folder         | Description                              |
| -------------- | ---------------------------------------- |
| `notebooks/`   | Jupyter notebooks (e.g., one per figure) |
| `source_data/` | Raw source datasets                      |
| `output_data/` | Generated results and figures            |
| `tasks.py`     | Project-specific invoke entrypoint       |
| `invoke.yaml`  | Config file for all reusable tasks       |

---

## 🧪 Want to use containers?

- Build: invoke docker-build
- Archive: invoke docker-archive
- Run: invoke docker-run --task run
- Setup from archive: invoke docker-setup 

---

## 🔁 Want to contribute?

Submit an issue or PR on [`airoh`](https://github.com/SIMEXP/airoh).

---

## Philosophy

Inspired by Uncle Iroh from *Avatar: The Last Airbender*, `airoh` aims to bring simplicity, reusability, and clarity to research infrastructure — one well-structured task at a time. It is meant to support a concrete implementation of the [YODA principles](https://handbook.datalad.org/en/latest/basics/101-127-yoda.html).

