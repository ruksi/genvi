# `genvi`

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

## Quickstart

```bash
# creates a new directory after asking for a name
curl -fSL https://raw.githubusercontent.com/ruksi/genvi/main/magic/conjure.sh | bash
```

## Requirements

* Linux, macOS or Windows Subsystem for Linux (WSL) with a `bash`-like shell
* `python>=3.7` with `pip`
* `git`
* `make`

## What?

> "I would sacrifice anything for some good quality code."
> by Anonymous Principal Engineer :woman_technologist:

`genvi` (<i><b>gen</b>eration of <b>vi</b></i>pers :snake:) is a hyperopinionated
tool for creating Python projects. It's strict, some could even say _too_ strict.
Borderline __evil__.

Each new project is configured with:

:hook: sadistic `pre-commit hooks` to enforce conventions
<br/>
:magic_wand: automagical `GitHub actions` to verify pull requests
<br/>
:mage: bewitching testing setup with `pytest` with 100% coverage requirement
<br/>
:black_cat: occult project management though `make` for development

If you want a more concrete example of a `genvi` project, you are looking at one.
`genvi` itself follows the same rules and uses the same tools. Behind the scenes,
creating a new project renames a few files and rewrites a bit of content.

## Why?

> "Who would want to manage a project like this?"
> by Anonymous Gnu :water_buffalo:

Scratching my own itch. Check out [`ABOUT.md`](ABOUT.md) to learn more.

## Usage

### Quickstart Usage

```bash
# creates a new directory after asking for a name
curl -fSL https://raw.githubusercontent.com/ruksi/genvi/main/magic/conjure.sh | bash
```

### Manual Usage

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
