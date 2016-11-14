from __future__ import absolute_import

import httplib

from nightson.handlers.auth import AuthHandler
from tornado import gen
from nightson.managers.user_events_manager import UserEventsManager

import ujson


class UserEventsHandler(AuthHandler):

    @gen.coroutine
    def get(self):
        ''' Get all events subscribed by an user! '''
        user_events_manager= UserEventsManager(self.request)
        result = yield user_events_manager.get_events(self.current_user)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))

