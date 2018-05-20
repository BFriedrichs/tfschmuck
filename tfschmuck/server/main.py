import os
import base64

from aiohttp import web
import aiohttp_session
from aiohttp_session import cookie_storage
import yacm
import jinja2
import aiohttp_jinja2

import tfschmuck

from . import middlewares, views


MODULE_PATH = os.path.dirname(tfschmuck.__file__)
BASE_PATH = os.path.dirname(__file__)


def register_routes(app):
    home_handler = views.home.Home()
    app.router.add_route('GET', '/', home_handler.get)

    jewellery_handler = views.jewellery.Jewellery()
    app.router.add_route('GET', '/jewellery', jewellery_handler.get)
    app.router.add_static(
        '/static/', path=os.path.join(MODULE_PATH, 'client', 'static'))


def create_app():
    app = web.Application()
    settings = yacm.read_configs('tfschmuck.server')

    template_path = os.path.join(MODULE_PATH, 'client', 'templates')
    jinja2_loader = jinja2.FileSystemLoader(template_path)
    # since the jinja context is apparently bugged currently we dont use setup
    # but rather set the env ourselves
    env = jinja2.Environment(autoescape=True, loader=jinja2_loader)

    update = {
        'name': 'tfschmuck',
        'settings': settings,
        aiohttp_jinja2.APP_KEY: env
    }
    app.update(**update)

    secret_key = base64.urlsafe_b64decode(settings['secrets']['cookie'])
    encrypted_storage = cookie_storage.EncryptedCookieStorage(secret_key)

    session_middleware = middlewares.session.middleware(encrypted_storage)
    response_middleware = middlewares.response.middleware()
    app.middlewares.append(response_middleware)
    app.middlewares.append(session_middleware)

    register_routes(app)
    return app
