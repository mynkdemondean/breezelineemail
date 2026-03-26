import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'breezelineemail'
author = 'breezelineemail'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

# Google Analytics
html_js_files = [
    'google_analytics.html',
]

# Bing Webmaster verification
html_context = {
    'metatags': """
    <meta name="msvalidate.01" content="739245F5D54BCBF40AC056DC0CBF5710" />
    """
}
