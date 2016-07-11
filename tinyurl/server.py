import tornado.ioloop
import tornado.web

from tinyurl.web import routes


def make_app():
    return tornado.web.Application(
        routes.get_routes()
    )


def serve():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
