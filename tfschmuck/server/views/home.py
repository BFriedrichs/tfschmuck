from . import view


class Home(view.BaseView):
    template = "home"

    async def get(self, request):
        """
        This is the view handler for the "/" url.

        :param request: the request object
        :return: context for the template.
        """

        return {
            'title': request.app['name'],
        }
