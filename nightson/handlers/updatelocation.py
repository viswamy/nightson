from __future__ import absolute_import

import httplib
from nightson.handlers.auth import AuthHandler
from tornado import gen
import ujson

from nightson.managers.users_entity_manager import UsersEntityManager


class UpdateLocationHandler(AuthHandler):

    @gen.coroutine
    def post(self):
        ''' Updates location for the current user '''
        users_entity_manager = UsersEntityManager(self.request)

        result = yield users_entity_manager.update_location(self.current_user)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))
