from __future__ import absolute_import

import httplib

from nightson.handlers.auth import AuthHandler
from tornado import gen
from nightson.managers.subscribe_manager import SubscribeManager
import ujson


class SubscribeHandler(AuthHandler):

    @gen.coroutine
    def post(self):
        ''' Subscribes a User for an Event! '''
        subscribe_manager = SubscribeManager(self.request)
        result = yield subscribe_manager.subscribe_user(self.current_user)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))


    @gen.coroutine
    def delete(self):
        ''' Unsubscribes a User for an Event! '''
        subscribe_manager = SubscribeManager(self.request)
        result = yield subscribe_manager.unsubscribe_user(self.current_user)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))