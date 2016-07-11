from __future__ import absolute_import

import httplib
import tornado

from tornado import gen


class HealthHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        ''' Return the helath of the service '''
        self.set_status(httplib.OK)
        self.write('OK')
