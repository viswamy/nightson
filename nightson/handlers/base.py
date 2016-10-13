from __future__ import absolute_import

import httplib
import tornado

from tornado import gen

class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    @gen.coroutine
    def execute_sql(self, sql):
        ''' Executes an sql statement and returns the value '''
        cursor = yield self.db.execute(sql)
        raise gen.Return(cursor)

