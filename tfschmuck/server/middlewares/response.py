from aiohttp import web
from ..views import view
import aiohttp_jinja2


def middleware():
    @web.middleware
    async def factory(request, handler):
        response = await handler(request)
        # the actual handler is bound
        method = handler.keywords['handler']
        kls = getattr(method, '__self__', None)

        # a view is rendered, the rest is a json response
        if kls and isinstance(kls, view.BaseView):
            template = '{}.jinja'.format(kls.template)
            rendered = aiohttp_jinja2.render_template(
                template, request, response)
            return rendered

        return web.Response()

    return factory
