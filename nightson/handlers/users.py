from __future__ import absolute_import

import httplib
from nightson.handlers.base import BaseHandler
from tornado import gen
import ujson

from nightson.managers.users_entity_manager import UsersEntityManager


class UsersHandler(BaseHandler):

    @gen.coroutine
    def get(self):
        ''' Returns an event given an ID '''
        print(self.get_argument('id'))
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

    @gen.coroutine
    def put(self):
        ''' Inserts and Returns an event '''
        users_entity_manager = UsersEntityManager(self.request)

        result = yield users_entity_manager.insert()
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))