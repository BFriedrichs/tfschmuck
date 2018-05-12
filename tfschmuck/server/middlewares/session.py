from aiohttp import web
import aiohttp_session


def middleware(storage):
    @web.middleware
    async def factory(request, handler):
        request[aiohttp_session.STORAGE_KEY] = storage
        raise_response = False
        try:
            response = await handler(request)
        except web.HTTPException as exc:
            response = exc
            raise_response = True
        session = request.get(aiohttp_session.SESSION_KEY)
        if session is not None:
            if session._changed:
                await storage.save_session(request, response, session)
        if raise_response:
            raise response
        return response

    return factory
