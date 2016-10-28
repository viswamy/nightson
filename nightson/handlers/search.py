from __future__ import absolute_import

import httplib
from nightson.handlers.auth import AuthHandler
from tornado import gen
import ujson

from nightson.managers.search_manager import SearchManager


class SearchHandler(AuthHandler):

    @gen.coroutine
    def get(self):
        ''' Returns list of events given location and radius '''
        search_manager = SearchManager(self.request)

        result = yield search_manager.get_events()
        self.set_status(httplib.OK)
        self.write(ujson.dumps(result))
