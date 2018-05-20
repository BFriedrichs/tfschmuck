from . import view


class Jewellery(view.BaseView):
    template = "jewellery"

    async def get(self, request):
        """
        This is the view handler for the "/jewellery" url.

        :param request: the request object
        :return: context for the template.
        """

        return {
            'title': request.app['name'],
        }