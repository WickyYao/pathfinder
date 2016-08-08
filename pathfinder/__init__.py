import os
from pyramid.config import Configurator


here = os.path.dirname(os.path.abspath(__file__))


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['mako.directories'] = os.path.join(here, 'templates')

    config = Configurator(settings=settings)
    config.include('pyramid_mako') # set mako
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
