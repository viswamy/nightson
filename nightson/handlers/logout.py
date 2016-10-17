from __future__ import absolute_import

import httplib
from nightson.handlers.auth import AuthHandler
from tornado import gen
import ujson

from nightson.managers.logout_manager import LogoutManager


class LogoutHandler(AuthHandler):

    @gen.coroutine
    def post(self):
        ''' Updates and Returns an event '''
        logout_manager = LogoutManager(self.request)
        result = yield logout_manager.logout(self.current_user)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))
