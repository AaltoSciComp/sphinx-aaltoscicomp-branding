from os import environ
from os.path import abspath, join, dirname

from ._version import __version__

def setup(app):

    def config_hook(app, config):
        """Hook to set the HTML favicon"""
        config.html_favicon = abspath(join(dirname(__file__), '_static', 'logo-hexagons-02-compact.svg.ico'))

    # Only add the hook if we think we are being built in an AaltoSciComp
    # location:
    if (environ.get('GITHUB_REPOSITORY', '').lower().startswith('aaltoscicomp')
          or 'AALTOSCICOMP' in environ):
        print("Enabling sphinx-aaltoscicomp-branding in this build.")
        app.connect('config-inited', config_hook)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
