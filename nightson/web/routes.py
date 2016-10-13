from __future__ import absolute_import

from nightson.handlers.events import EventsHandler
from nightson.handlers.health import HealthHandler


def get_routes():
    return [
        (r'/health', HealthHandler),
        (r'/events', EventsHandler),
    ]
