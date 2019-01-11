project('gnome-news',
    version: '0.0.1',
    meson_version: '>= 0.46.0'
)

# Importing modules
gnome = import('gnome')
i18n  = import('i18n')
python = import('python')

# Module objects
py_installation = python.find_installation('python3')

# Make sure Python is installed and found
if not py_installation.found()
    error('No valid python3 binary found')
endif

# Constants
PROJECT_RDNN_NAME = 'gnome-news'
APPLICATION_ID = 'org.gnome.News'
PYTHON_DIR = py_installation.get_path('purelib')
PKGDATA_DIR = join_paths(get_option('prefix'), get_option('datadir'), APPLICATION_ID)
PKGLIB_DIR = join_paths(get_option('prefix'), get_option('libdir'), APPLICATION_ID)

# Dependencies
dependency('goa-1.0')
dependency('gobject-introspection-1.0', version: '>= 1.35.0')
dependency('gtk+-3.0', version: '>= 3.23.1')
dependency('tracker-sparql-2.0', version: '>= 1.99.1')
dependency('pygobject-3.0', version: '>= 3.29.1')
dependency('py3cairo', version: '>= 1.14.0')

subdir('data')
subdir('po')

install_subdir(
    'gnomenews',
    install_dir: py_installation.get_install_dir()
)

# Install the executable file
bin_config = configuration_data()
bin_config.set('application_id', APPLICATION_ID)
bin_config.set('rdnn_name', PROJECT_RDNN_NAME)
bin_config.set('pkgdatadir', PKGDATA_DIR)
bin_config.set('localedir', join_paths(get_option('prefix'), get_option('datadir'), 'locale'))
bin_config.set('pythondir', PYTHON_DIR)
bin_config.set('pyexecdir', py_installation.get_path('stdlib'))
bin_config.set('schemasdir', '')
bin_config.set('version', meson.project_version())

configure_file(
    input: 'gnome-news.in',
    output: 'gnome-news',
    configuration: bin_config,
    install_dir: get_option('bindir')
)

# Install the builddir executable
local_config = configuration_data()
local_config.set('pkgdatadir', join_paths(meson.build_root(), 'data'))
local_config.set('localedir', join_paths(get_option('prefix'), get_option('datadir'), 'locale'))
local_config.set('pythondir', meson.source_root())
local_config.set('pyexecdir', meson.source_root())
local_config.set('schemasdir', join_paths(meson.build_root(), 'data'))
local_config.set('version', meson.project_version())

configure_file(
    input: 'gnome-news.in',
    output: 'local-news',
    configuration: local_config
)

meson.add_postconf_script('meson_post_conf.py')
meson.add_install_script('meson_post_install.py')
