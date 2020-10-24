# -*- coding: utf-8 -*-
import sphinx_rtd_theme

# -- General configuration -----------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'easy_esi'
copyright = u'2013, Digium, Inc.; 2014-2015, Yelp, Inc'

exclude_patterns = []

pygments_style = 'sphinx'

autoclass_content = 'both'

# -- Options for HTML output ---------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

htmlhelp_basename = 'easy_esi-pydoc'


intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'easy-esi-core': ('https://easy-esi-core.readthedocs.io/en/latest/', None),
}
