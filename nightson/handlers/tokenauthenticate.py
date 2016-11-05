from __future__ import absolute_import

from nightson.handlers.auth import AuthHandler

from tornado import gen
import httplib

class TokenAuthenticateHandler(AuthHandler):

    @gen.coroutine
    def get(self):
        self.write({
            'message': 'Valid token received!'
        })
        self.set_status(httplib.ACCEPTED)
        self.finish()
