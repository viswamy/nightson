from __future__ import absolute_import

import httplib

from nightson.handlers.auth import AuthHandler
from nightson.managers.events_owned_by_user_manager import EventsOwnedByUserManager
from tornado import gen
import ujson


class EventsOwnedByUser(AuthHandler):

    @gen.coroutine
    def get(self):
        ''' Subscribes a User for an Event! '''
        events_owned_by_user_manager= EventsOwnedByUserManager(self.request)
        result = yield events_owned_by_user_manager.get_events(self.current_user)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))

