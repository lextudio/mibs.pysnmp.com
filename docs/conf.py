# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os


project = 'SNMP MIB Repository'
copyright = '2024, LeXtudio Inc.'
author = 'LeXtudio Inc. <support@lextudio.com>'

version = "1.0"
release = '1.0.0'

language = "en_US"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_sitemap",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_baseurl = "https://mibs.sharpsnmp.com/"
sitemap_url_scheme = "{link}"

templates_path = ["_templates"]

html_search_language = 'en'

def setup(app):
    on_rtd = os.environ.get("READTHEDOCS", None) == "True"
    if not on_rtd:
        """Insert Google Analytics tracker
        Based on this Stackoverflow suggestion: https://stackoverflow.com/a/41885884
        """
        app.add_js_file("https://www.googletagmanager.com/gtag/js?id=G-DYQGY4MKR3")
        app.add_js_file("google_analytics_tracker.js")
