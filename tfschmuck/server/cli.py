import click
import os
import sys
import traceback

import asyncio
from aiohttp import web


class colors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


@click.command()
@click.option('--static', default=False, help='Add a static endpoint.')
@click.option('--port', default=8000, help='Specify the port.')
def develop(static, port):
    """Serve a a develop version of the project"""

    cli_print("Serving on localhost:{}".format(port))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(reload_server(loop, port))


def cli_print(*args, **kwargs):
    print(colors.OKGREEN + "[CLI]", *args, **kwargs, end=colors.ENDC + '\n')


async def reload_server(loop, port):
    # lazy import watchgod
    from watchgod import awatch
    MODULE_PATH = os.path.dirname(__file__)
    app = try_server()

    if app:
        server = await loop.create_server(
            app.make_handler(), '0.0.0.0', port)

    async for changes in awatch(MODULE_PATH):
        cli_print("Reloading server...")

        if app:
            # cleanup
            await app.shutdown()
            await app.cleanup()
            server.close()
            await server.wait_closed()

        app = try_server()
        if app:
            server = await loop.create_server(
                app.make_handler(), '0.0.0.0', port)


def try_server():
    app = None
    try:
        # for some reason importlib.reload doesnt work
        for key in list(sys.modules.keys()):
            if key.startswith('tfschmuck'):
                del sys.modules[key]

        from tfschmuck import server
        app = server.main.create_app()
    except Exception as e:
        traceback.print_exc()
    return app


@click.command()
@click.option('--port', default=8000, help='Specify the port.')
def serve(port):
    from tfschmuck import server
    app = server.main.create_app()

    web.run_app(app, port=port)


@click.group()
def cli():
    pass


cli.add_command(develop)
cli.add_command(serve)


if __name__ == '__main__':
    cli()
