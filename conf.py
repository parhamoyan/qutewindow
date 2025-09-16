# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'QuteWindow'
copyright = '2024, Parham Oyan'
author = 'Parham Oyan'
release = '0.2.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Autosummary settings
autosummary_generate = True

# Napoleon settings (for Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# HTML theme settings
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'navigation_depth': 4,
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pyside6': ('https://doc.qt.io/qtforpython/', None),
}

# Templates and static files
templates_path = ['_templates']
html_static_path = ['_static']

# Master document
master_doc = 'index'

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'examples']