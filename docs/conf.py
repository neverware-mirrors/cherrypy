# -*- coding: utf-8 -*-
#
# CherryPy documentation build configuration file, created by
# sphinx-quickstart on Sat Feb 20 09:18:03 2010.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import datetime
import importlib
import subprocess

assert sys.version_info > (3,), 'Python 3 required to build docs'


def try_import(mod_name):
    try:
        return importlib.import_module(mod_name)
    except ImportError:
        pass

sphinx_rtd_theme = try_import('sphinx_rtd_theme')  # noqa: E305

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'rst.linker',
]

intersphinx_mapping = {
    'https://docs.python.org/3/': None,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'  # noqa

# The master toctree document.
master_doc = 'index'

# load metadata from the project (borrowed from jaraco/skeleton)
root = os.path.join(os.path.dirname(__file__), '..')
setup_script = os.path.join(root, 'setup.py')
fields = ['--name', '--version', '--url', '--author']
dist_info_cmd = [sys.executable, setup_script] + fields
output_bytes = subprocess.check_output(dist_info_cmd, cwd=root)
project, version, url, author = output_bytes.decode('utf-8').strip().split('\n')

# General information about the project.
copyright = '2001-%d %s' % (datetime.date.today().year, author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None  # noqa

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''  # noqa
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'  # noqa

# List of documents that shouldn't be included in the build.
#unused_docs = []  # noqa

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None  # noqa

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True  # noqa

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True  # noqa

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False  # noqa

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []  # noqa


# -- Options for HTML output ---------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = getattr(sphinx_rtd_theme, '__name__', 'default')

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
# "relbarbgcolor": "#880000",
#     "relbartextcolor": "white",
# "relbarlinkcolor": "#FFEEEE",
# "sidebarbgcolor": "#880000",
#     "sidebartextcolor": "white",
# "sidebarlinkcolor": "#FFEEEE",
# "headbgcolor": "#FFF8FB",
#     "headtextcolor": "black",
# "headlinkcolor": "#660000",
# "footerbgcolor": "#880000",
#     "footertextcolor": "white",
# "codebgcolor": "#FFEEEE",
# }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []  # noqa
if sphinx_rtd_theme:
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None  # noqa

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None  # noqa

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None  # noqa

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None  # noqa

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_style = 'cpdocmain.css'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'  # noqa

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True  # noqa

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}  # noqa

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}  # noqa

# If false, no module index is generated.
#html_use_modindex = True  # noqa

# If false, no index is generated.
#html_use_index = True  # noqa

# If true, the index is split into individual pages for each letter.
#html_split_index = False  # noqa

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True  # noqa

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''  # noqa

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''  # noqa

# Output file base name for HTML help builder.
htmlhelp_basename = 'CherryPydoc'


# -- Options for LaTeX output --------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'  # noqa

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'  # noqa

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
# documentclass [howto/manual]).
latex_documents = [
    (
        'index',
        'CherryPy.tex',
        'CherryPy Documentation',
        'CherryPy Team',
        'manual',
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None  # noqa

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False  # noqa

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''  # noqa

# Documents to append as an appendix to all manuals.
#latex_appendices = []  # noqa

# If false, no module index is generated.
#latex_use_modindex = True  # noqa


def mock_pywin32():
    """
    Mock pywin32 so that Linux hosts, including ReadTheDocs,
    and other environments that don't have pywin32 can generate the docs
    properly including the PDF version.
    See:
    http://read-the-docs.readthedocs.org/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
    """
    if try_import('win32api'):
        return

    from unittest import mock

    MOCK_MODULES = [
        'win32api', 'win32con', 'win32event', 'win32service',
        'win32serviceutil',
    ]
    for mod_name in MOCK_MODULES:
        sys.modules[mod_name] = mock.MagicMock()
mock_pywin32()  # noqa: E305

link_files = {
    '../CHANGES.rst': dict(
        using=dict(
            GH='https://github.com',
            project=project,
            url=url,
        ),
        replace=[
            dict(
                pattern=r'(Issue )?#(?P<issue>\d+)',
                url='{url}/issues/{issue}',
            ),
            dict(
                pattern=r'^(?m)((?P<scm_version>v?\d+(\.\d+){1,2}))\n[-=]+\n',
                with_scm='{text}\n{rev[timestamp]:%d %b %Y}\n',
            ),
        ],
    ),
}
