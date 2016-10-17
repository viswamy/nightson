from __future__ import absolute_import

import httplib
from nightson.handlers.base import BaseHandler
from tornado import gen
import ujson

from nightson.managers.login_manager import LoginManager


class LoginHandler(BaseHandler):

    @gen.coroutine
    def post(self):
        ''' Updates and Returns an event '''
        events_entity_manager = LoginManager(self.request)
        result = yield events_entity_manager.get_token()

        if(result == {}):
            self.set_status(httplib.UNAUTHORIZED)
            self.write( {
                'message': 'Invalid Username/Password Combination!'
            })
        else:
            self.set_status(httplib.OK)
            self.write(ujson.dumps(result))
