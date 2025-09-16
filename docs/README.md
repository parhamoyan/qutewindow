# QuteWindow Documentation

This directory contains the Sphinx configuration and source files for generating QuteWindow documentation.

## Building Documentation

To build the documentation locally:

```bash
cd docs
sphinx-build -b html . _build
```

The generated HTML documentation will be available in the `_build` directory.

## Configuration

- `conf.py` - Sphinx configuration file
- `index.rst` - Main documentation file with auto-generated API reference
- `requirements.txt` - Documentation dependencies

## ReadTheDocs

The documentation is automatically built and hosted on ReadTheDocs when changes are pushed to the repository.

## Auto-Generated Content

The documentation is automatically generated from docstrings in the source code using Sphinx's autodoc extension. No manual RST files are needed - the API reference is generated directly from the Python source code.