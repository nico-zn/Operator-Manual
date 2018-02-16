# -*- coding: utf-8 -*-
import sys, os, sphinx_rtd_theme

# Configuration
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'rst2pdf.pdfbuilder']
source_suffix = '.rst'
master_doc = 'index'
project = 'OpenJet'
copyright = u'2015-2018, OpenJet Team'
man_pages = [
    ('index', 'openjet', u'Openjet Documentation',
     [u'OpenJet Team'], 1)
]

# Doc version
version = '2.9.6'
release = ''

# PDF Configuration
pdf_documents = [('index', u'OpenJet_360__Operator_Manual', u'OpenJet 360 Operator Manual', u'OpenJet S.A.'),]
pdf_style_path = ['.', '_styles']

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
