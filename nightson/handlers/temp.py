from __future__ import absolute_import

import httplib

from nightson.handlers.auth import AuthHandler
from tornado import gen
import ujson


class TempHandler(AuthHandler):

    @gen.coroutine
    def get(self):
        ''' Returns an event given an ID '''
        self.set_status(httplib.OK)
        self.write(ujson.dumps({
            'temp': 'hi there!'
        }))
