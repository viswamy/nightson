from __future__ import absolute_import

import httplib
from nightson.handlers.base import BaseHandler
from tornado import gen


class HealthHandler(BaseHandler):

    @gen.coroutine
    def get(self):
        ''' Return the helath of the service '''
        self.set_status(httplib.OK)
        self.write('OK')
