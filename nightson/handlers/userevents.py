from __future__ import absolute_import

import httplib

from nightson.handlers.auth import AuthHandler
from tornado import gen
from nightson.managers.user_events_manager import UserEventsManager
import ujson


class UserEventsHandler(AuthHandler):

    @gen.coroutine
    def post(self):
        ''' Subscribes a User for an Event! '''
        user_events_manager = UserEventsManager(self.request)
        result = yield user_events_manager.subscribe_user(self.current_user)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))


    @gen.coroutine
    def delete(self):
        ''' Unsubscribes a User for an Event! '''
        user_events_manager = UserEventsManager(self.request)
        result = yield user_events_manager.unsubscribe_user(self.current_user)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))