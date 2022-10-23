# Commands for building packages
```
pip install --upgrade pip build twine

python -m build
python -m twine upload dist/*
```

# References
* [How to package projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Configuring setuptools using setup.cfg files](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html#configuring-setuptools-using-setup-cfg-files)
* [How to package data files](https://setuptools.pypa.io/en/latest/userguide/datafiles.html)
* [How to write MANIFEST.in](https://packaging.python.org/en/latest/guides/using-manifest-in/)
* [How to name package versions](https://peps.python.org/pep-0440/#version-scheme)
* [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
* [Differences between install_requires and requirements files](https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/)
* [Why should not reference requirements.txt for the install_requires kwarg in setuptools' setup.py file](https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py)