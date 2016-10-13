import tornado.ioloop
import tornado.web
import momoko

from nightson.web import routes
from psycopg2.extras import DictConnection
from psycopg2.extras import RealDictConnection

def make_app():
    return tornado.web.Application(
        routes.get_routes()
    )


def serve():
    app = make_app()
    app.listen(8888)
    current_ioloop = tornado.ioloop.IOLoop.current()
    app.db = momoko.Pool(
        dsn = '''dbname=nightson user=vswamy password=vswamy host=localhost port=5432''',
        size = 5,
        ioloop = current_ioloop,
        connection_factory = RealDictConnection,
    )
    app.db.connect()
    current_ioloop.start()
