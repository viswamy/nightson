from __future__ import absolute_import

import httplib
from nightson.handlers.auth import AuthHandler
from tornado import gen
import ujson

from nightson.managers.users_entity_manager import UsersEntityManager


class UsersHandler(AuthHandler):

    @gen.coroutine
    def get(self):
        ''' Returns an event given an ID '''
        users_entity_manager = UsersEntityManager(self.request)

        result = yield users_entity_manager.fetch_one()
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))

    @gen.coroutine
    def post(self):
        ''' Updates and Returns an event '''
        users_entity_manager = UsersEntityManager(self.request)

        result = yield users_entity_manager.update()
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))
