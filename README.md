[![workflow: ci](https://github.com/ruksi/genvi/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ruksi/genvi/actions?workflow=ci)
[![license: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![pre-commit: enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![class: wizard](https://img.shields.io/badge/class-wizard-blue.svg)](https://github.com/ruksi/genvi)
[![alignment: chaotic evil](https://img.shields.io/badge/alignment-chaotic%20evil-red.svg)](https://github.com/ruksi/genvi)

<br/>
<div align="center">
<img src="https://github.com/ruksi/genvi/blob/main/.github/genvi.svg"  alt="genvi logo"/>
</div>
<br/>
<p align="center">
<i>
O <b>generation of vipers</b>, how can ye, being evil, speak good things?
</i>
<br/>
- Matthew 12:34
</p>
<br/>
<p align="center">
<code>genvi</code> — A sadistic Python project wizard :snake::mage:
</p>
<br/>

## ⚡️ Quickstart

```bash
curl -fSL https://raw.githubusercontent.com/ruksi/genvi/main/magic/conjure.sh | bash
```

## 📝 Requirements

`python>=3.8`, `git` and `make`.

## 👉️ What?

> "I would sacrifice anything for some good quality code."
> by Anonymous Principal Engineer :woman_technologist:

`genvi` (<i><b>gen</b>eration of <b>vi</b></i>pers :snake:) is a hyperopinionated
tool for creating Python projects. It's strict, some could even say _too_ strict.
Borderline __evil__.

Each new project is configured with:

🐈‍⬛ eery `ruff format` as the code style, single quoted
<br/>
🪝 sadistic `pre-commit hooks` to enforce conventions
<br/>
🪄 automagical `GitHub actions` to verify incoming pull requests
<br/>
🧙 bewitching testing setup with `pytest` with 100% coverage requirement
<br/>
✴️ occult project management though `make` for development
<br/>
♾️ plethora of 20+ style and type checkers included in `ruff` and `mypy`

If you want a more concrete example of a `genvi` project, you are looking at one.
`genvi` itself follows the same rules and uses the same tools. Behind the scenes,
creating a new project renames a few files and rewrites a bit of content.

## 🤔 Why?

> "Who would want to manage a project like this?"
> by Anonymous Gnu :water_buffalo:

Scratching my own itch, see [`ABOUT.md`](ABOUT.md) to learn more

## 🦮 Usage

### ⚡️ Quick

```bash
curl -fSL https://raw.githubusercontent.com/ruksi/genvi/main/magic/conjure.sh | bash
```

### ✋ Manual

1. Decide the project name and clone this repository

   ```bash
   git clone git@github.com:ruksi/genvi.git my-project
   cd my-project
   ```

2. Decide a clean package name, run the wizard and follow instruction

   ```bash
   # package name should be something you can `import` in Python
   # preferably just lowercase ASCII letters
   make package=myproject
   ```

## 📜 License

This project is released under the [MIT License](LICENSE).

## 🧑‍💻 Contributions

Sure, [`the README template`](magic/utils/readme_template.md) should get you started
as `genvi` itself works like the projects it generates.
