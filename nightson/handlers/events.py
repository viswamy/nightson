from __future__ import absolute_import

import httplib
from nightson.handlers.base import BaseHandler
from tornado import gen
import ujson

class EventsHandler(BaseHandler):

    @gen.coroutine
    def get(self):
        ''' Returns all events in the database '''
        sql = ''' SELECT * FROM Events; '''
        result = yield self.execute_sql(sql)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))
