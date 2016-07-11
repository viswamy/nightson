from __future__ import absolute_import

from tornado.testing import AsyncHTTPTestCase
from tinyurl import server


class TestBaseHandler(AsyncHTTPTestCase):

    def get_app(self):
        return server.make_app()

    def get_base_path(self):
        return 'http://localhost:{}/'.format(8888)
