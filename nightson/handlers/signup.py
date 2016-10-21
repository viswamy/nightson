from __future__ import absolute_import

import httplib
from nightson.handlers.auth import BaseHandler
from tornado import gen
import ujson

from nightson.managers.users_entity_manager import UsersEntityManager


class SignUpHandler(BaseHandler):

    @gen.coroutine
    def put(self):
        ''' Inserts and Returns an event '''
        users_entity_manager = UsersEntityManager(self.request)

        result = yield users_entity_manager.insert()
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))