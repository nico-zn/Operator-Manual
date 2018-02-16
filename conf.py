# -*- coding: utf-8 -*-
import sys, os, sphinx_rtd_theme

# Configuration
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.imgmath']
source_suffix = '.rst'
master_doc = 'index'
project = 'OpenJet'
copyright = u'2015-2018, OpenJet Team'
man_pages = [
    ('index', 'openjet', u'Openjet Documentation',
     [u'OpenJet Team'], 1)
]

# Doc version
version = ''
release = ''

# Sphinx Read the doc theme : https://github.com/rtfd/sphinx_rtd_theme
html_theme = "openjet_rtd_theme"
html_theme_path = ["_themes"]
html_logo = '_images/logo.png'
html_favicon = '_images/favicon.ico'

rst_epilog = """
"""

# Linkcheck
# Exclude gitlab for prevent SSL certificate error
linkcheck_ignore = [r'https://gitlab\.openjetlab\.fr']
