master_doc = 'index'
project = "Anuket Specifications"
html_title = "Anuket Specifications"
copyright = '2023, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel'
             ]

exclude_patterns = [
    '**/.tox',
    'ref_arch',
    'ref_cert',
    'ref_impl',
    'ref_model',
    'tech',
    'gov/README.rst'
]
linkcheck_ignore = [
    'https://github.com/cncf/telecom-user-group/blob/master/whitepaper/cloud_native_thinking_for_telecommunications.md#1.4',
    'https://static1.squarespace.com/static/5ad774cce74940d7115044b0/t/5db36ffa820b8d29022b6d08/1572040705841/ORAN-WG4.IOT.0-v01.00.pdf/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf',
    'https://ntia.gov',
    'https://www.ngmn.org/wp-content/uploads/Publications/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf',
    'https://wiki.lfnetworking.org/'
]
intersphinx_mapping = {
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None),
    'ref_arch_openstack': ('https://cntt.readthedocs.io/projects/ra1/en/latest/', None),
    'ref_arch_kubernetes': ('https://cntt.readthedocs.io/projects/ra2/en/latest/', None),
    'ref_cert_RC2': ('https://cntt.readthedocs.io/projects/rc2/en/latest/', None),
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4

numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}

html_theme = "piccolo_theme"

html_static_path = ['_static']
templates_path = ['_templates']
html_css_files = [
    'custom.css',
]

html_show_sourcelink = False
html_theme_options = {
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# Inverse png
html_logo = '_static/anuket-logo.png'
html_favicon = '_static/favicon.ico'
