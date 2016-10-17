from __future__ import absolute_import

from nightson.handlers.base import BaseHandler
from nightson.managers.session_manager import SessionManager

from tornado import gen
import httplib

class AuthHandler(BaseHandler):

    @gen.coroutine
    def prepare(self):
        session_manager = SessionManager(self.request)
        self.current_user = yield session_manager.authenticate_token()
        if(self.current_user is None):
            self.write({
                'message': 'Invalid token received!'
            })
            self.set_status(httplib.UNAUTHORIZED)
            self.finish()


