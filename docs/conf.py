# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from sphinx_tags import __version__

sys.path.insert(0, os.path.abspath("../src"))


# -- Project information -----------------------------------------------------

project = "sphinx-tags"
copyright = "2022, melissawm"
author = "melissawm"

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_tags",
    "sphinx_design",
    "myst_parser",
]

tags_create_tags = True
# tags_output_dir = "_tags"  # default
tags_overview_title = "All tags"  # default: "Tags overview"
tags_extension = ["rst", "md"]  # default: ["rst"]
tags_intro_text = "Tags in this page:"  # default: "Tags:"
tags_page_title = "All my tags"  # default: "My tags:"
tags_page_header = "Pages with this tag"  # default: "With this tag"
tags_index_head = "Tags in this site"  # default: "Tags"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# html_sidebars = {
#     "**": ["search-field.html", "sidebar-nav-bs.html", "sidebar-tags.html"],
#     "_tags/*": ["search-field.html", "sidebar-nav-bs.html"],
# }
