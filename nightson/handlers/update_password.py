from __future__ import absolute_import

import ujson

from nightson.handlers.auth import AuthHandler
from nightson.managers.users_entity_manager import UsersEntityManager

from tornado import gen
import httplib

class UpdatePasswordHandler(AuthHandler):

    @gen.coroutine
    def post(self):
        users_entity_manager = UsersEntityManager(self.request)
        result = yield users_entity_manager.update_password(self.current_user)
        if(result == {}):
            self.set_status(httplib.BAD_REQUEST)
            self.write({
                'message': 'Invalid old password!'
            })
        else:
            self.set_status(httplib.OK)
            self.write(result)


