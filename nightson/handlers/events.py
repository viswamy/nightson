from __future__ import absolute_import

import httplib
from nightson.handlers.base import BaseHandler
from tornado import gen
import ujson

from nightson.managers.events_entity_manager import EventsEntityManager


class EventsHandler(BaseHandler):

    events_entity_manager = EventsEntityManager()

    @gen.coroutine
    def get(self):
        ''' Returns an event given an ID '''
        arguments = self.request.query_arguments
        id = arguments['id'][0]

        result = yield EventsHandler.events_entity_manager.fetch_one(id)
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))

    @gen.coroutine
    def post(self):
        ''' Updates and Returns an event '''
        body_arguments = self.request.body_arguments
        result = yield EventsHandler.events_entity_manager.update(body_arguments)
        self.write(ujson.dumps(result))

    @gen.coroutine
    def put(self):
        ''' Inserts and Returns an event '''
        body_arguments = self.request.arguments
        result = yield EventsHandler.events_entity_manager.insert(body_arguments)
        self.write(ujson.dumps(result))