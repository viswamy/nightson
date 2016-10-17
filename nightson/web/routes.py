from __future__ import absolute_import

from nightson.handlers.events import EventsHandler
from nightson.handlers.health import HealthHandler
from nightson.handlers.users import UsersHandler


def get_routes():
    return [
        (r'/health', HealthHandler),
        (r'/events', EventsHandler),
        (r'/users', UsersHandler),
    ]
