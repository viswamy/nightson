from __future__ import absolute_import

import httplib
from nightson.handlers.auth import AuthHandler
from tornado import gen
import ujson

from nightson.managers.events_entity_manager import EventsEntityManager


class EventsHandler(AuthHandler):

    @gen.coroutine
    def get(self):
        ''' Returns an event given an ID '''
        events_entity_manager = EventsEntityManager(self.request)

        result = yield events_entity_manager.fetch_one()
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))

    @gen.coroutine
    def post(self):
        ''' Updates and Returns an event '''
        events_entity_manager = EventsEntityManager(self.request)
        result = yield events_entity_manager.update()

        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))

    @gen.coroutine
    def put(self):
        ''' Inserts and Returns an event '''
        events_entity_manager = EventsEntityManager(self.request)
        result = yield events_entity_manager.insert(self.current_user)

        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))