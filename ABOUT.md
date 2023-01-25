# About

`genvi` is a tool to start new Python projects.

It doesn't have versioning as it's expected to be used
in a fire-and-forget fashion; generate the Python project and code on.

There isn't much anything special about `genvi`, it's just another Python project
template among many others. Different strokes for different folks.

## Alternatives

Other project templates you might want to check out:

* <https://github.com/cjolowicz/cookiecutter-hypermodern-python>
* <https://github.com/wemake-services/wemake-python-package>
* <https://github.com/rochacbruno/python-project-template>
* <https://github.com/pyscaffold/pyscaffold>

## FAQ

<dl>
<dt>
    Why not using <a href="https://github.com/cookiecutter/cookiecutter"><code>cookiecutter</code></a>?
</dt>
<dd>
    We don't need thousands of lines of code to <code>mv</code> a couple of files.
</dd>
<dt>
    Why mangle the source repository itself to create a new project?
</dt>
<dd>
    Mainly for DRY.
    Conceptually, if you were to create a project that generated a "perfect" project, shouldn't
    the generator project follow exactly the same rules and conventions? The downside
    is some extra clutter in the <code>genvi</code> repository.
</dd>
<dt>
    Why does the template include building/distributing/server start/command line usage/etc.?
</dt>
<dd>
    It is more robust to automatically set up everything and commit them to
    a version control before removing them. This way, if you ever need
    the features in the future, you can get them from the version control history.
</dd>
<dt>
    Some <code>pre-commit</code> hooks disable the isolated environment
    with <code>language: system</code>, why?
</dt>
<dd>
    Some tools like <code>mypy</code> won't work on their full potential
    if the rest of the dependencies are missing from the environment;
    and it makes little sense to reinstall the full the development setup.
    <br/><br/>
    You might want to integrate some tools (e.g. <code>ruff</code>, <code>mypy</code>)
    with your IDE, in which case the extra duplication becomes unnecessary.
</dd>
<dt>
    Who uses <code>make</code> anymore?
    Why not using <code>invoke</code>, <code>nox</code> or <code>tox</code> for task management?
</dt>
<dd>
    <code>make</code> is already available on most systems, and if not,
    it's easy to install. It is more coherent to get all the initial project requirements
    from a single interface where you are probably already getting Python and Git.
    <br/><br/>
    When working on multitude of project in different languages,
    it reduces the mental burden if you have a single way of managing projects.
    You don't want to require Python on your Go project just for the development
    tooling, for example. The answer to "How was testing done in this context?"
    is always <code>make test</code>
</dd>
<dt>
    Having an 100% test coverage requirement gives false sense-of-security.
    Isn't that an overkill?
</dt>
<dd>
    Yes.
</dd>
</dl>
