# -*- coding: utf-8 -*-
execfile('../conf.py')
# -- General -------------------------------------------------------------------
project = u'Administrator Guide'

# -- Options for HTML output ---------------------------------------------------
html_title = "NetXMS %s %s" % (release, project)

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ('index', 'netxms-admin.tex', u'NetXMS %s' % project, project_author, 'manual'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project