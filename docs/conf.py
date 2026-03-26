# conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Breezeline Login Account Guide'
author = 'Independent Service Provider'
release = '1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

# Use custom template
html_theme_options = {}
html_context = {}

# Add custom layout for Google/Bing tracking
html_sidebars = {
    '**': ['globaltoc.html', 'searchbox.html']
}
