[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit: enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![license: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![class: wizard](https://img.shields.io/badge/class-wizard-blue.svg)](https://github.com/ruksi/genvi)
[![alignment: chaotic evil](https://img.shields.io/badge/alignment-chaotic%20evil-red.svg)](https://github.com/ruksi/genvi)

<br/>
<div align="center">
<img src="https://github.com/ruksi/genvi/blob/main/images/genvi.svg"  alt="genvi logo"/>
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

* Linux, macOS or Windows Subsystem for Linux (WSL) with a `bash`-like shell
* `python>=3.7` with `pip`
* `git`
* `make`

## 👉️ What?

> "I would sacrifice anything for some good quality code."
> by Anonymous Principal Engineer :woman_technologist:

`genvi` (<i><b>gen</b>eration of <b>vi</b></i>pers :snake:) is a hyperopinionated
tool for creating Python projects. It's strict, some could even say _too_ strict.
Borderline __evil__.

Each new project is configured with:

🐈‍⬛ eery `black` as the code style, single quoted
<br/>
🪝 sadistic `pre-commit hooks` to enforce conventions
<br/>
🪄 automagical `GitHub actions` to verify incoming pull requests
<br/>
🧙 bewitching testing setup with `pytest` with 100% coverage requirement
<br/>
✴️ occult project management though `make` for development
<br/>
♾️ plethora of 20+ design and type checkers like `flake8`, `pylint` and `mypy`

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

1. Name your project e.g. `myproject`

   ```bash
   export NAME=myproject
   ```

2. Clone this repository

   ```bash
   git clone git@github.com:ruksi/genvi.git $NAME
   cd $NAME
   ```

3. Delete the `.git/` directory to remove all relation to `genvi`

   ```bash
   rm -rf .git/
   ```

4. Finalize the transformation

   ```bash
   make package=$NAME
   # answer questions if any pop up
   ```

5. Follow the new [`README.md`](magic/utils/readme_template.md) to continue development

## 📜 License

This project is released under the [MIT License](LICENSE).

## 🧑‍💻 Contributions

Sure, the [`README.md`](magic/utils/readme_template.md) template should get you started
as `genvi` itself works like the projects it generates.
