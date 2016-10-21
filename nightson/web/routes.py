from __future__ import absolute_import

from nightson.handlers.events import EventsHandler
from nightson.handlers.health import HealthHandler
from nightson.handlers.logout import LogoutHandler
from nightson.handlers.users import UsersHandler
from nightson.handlers.login import LoginHandler
from nightson.handlers.temp import TempHandler
from nightson.handlers.userevents import UserEventsHandler

def get_routes():
    return [
        (r'/health', HealthHandler),
        (r'/events', EventsHandler),
        (r'/users', UsersHandler),
        (r'/login', LoginHandler),
        (r'/temp', TempHandler),
        (r'/logout', LogoutHandler),
        (r'/userevents', UserEventsHandler),
    ]
