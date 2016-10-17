import tornado.ioloop
import tornado.web

from nightson.web import routes


def make_app():
    return tornado.web.Application(
        routes.get_routes()
    )


def serve():
    app = make_app()
    app.listen(8888)
    current_ioloop = tornado.ioloop.IOLoop.current()
    current_ioloop.start()
