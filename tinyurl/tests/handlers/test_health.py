from __future__ import absolute_import

from tinyurl.tests.handlers.test_base import TestBaseHandler

import tornado


class TestHealthHandler(TestBaseHandler):

    def get_endpoint(self):
        return "health"

    @tornado.testing.gen_test
    def test_http_fetch(self):
        response = yield self.http_client.fetch(self.get_url('/health'))
        assert response.code == 200
        assert response.body == 'OK'
