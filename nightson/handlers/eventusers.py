from __future__ import absolute_import

import httplib

from nightson.handlers.auth import AuthHandler
from tornado import gen
from nightson.managers.events_user_manager import EventUsersManager
import ujson


class EventUsersHandler(AuthHandler):

    @gen.coroutine
    def get(self):
        ''' Subscribes a User for an Event! '''
        event_users_manager= EventUsersManager(self.request)
        result = yield event_users_manager.get_users()
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))

