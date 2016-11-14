from __future__ import absolute_import

from nightson.handlers.events import EventsHandler
from nightson.handlers.health import HealthHandler
from nightson.handlers.logout import LogoutHandler
from nightson.handlers.signup import SignUpHandler
from nightson.handlers.users import UsersHandler
from nightson.handlers.login import LoginHandler
from nightson.handlers.temp import TempHandler
from nightson.handlers.subscribe import SubscribeHandler
from nightson.handlers.upload import UploadHandler
from nightson.handlers.update_password import UpdatePasswordHandler
from nightson.handlers.search import SearchHandler
from nightson.handlers.tokenauthenticate import TokenAuthenticateHandler
from nightson.handlers.eventusers import EventUsersHandler
from nightson.handlers.eventsownedbyuser import EventsOwnedByUser

from tornado import web

def get_routes():
    return [
        (r'/health', HealthHandler),
        (r'/events', EventsHandler),
        (r'/users', UsersHandler),
        (r'/login', LoginHandler),
        (r'/temp', TempHandler),
        (r'/logout', LogoutHandler),
        (r'/subscribe', SubscribeHandler),
        (r'/upload', UploadHandler),
        (r'/static/(.*)', web.StaticFileHandler, {'path': './uploads'}),
        (r'/signup', SignUpHandler),
        (r'/updatepassword', UpdatePasswordHandler),
        (r'/search', SearchHandler),
        (r'/tokenauthenticate', TokenAuthenticateHandler),
        (r'/eventusers', EventUsersHandler),
        (r'/eventsownedbyuser', EventsOwnedByUser),
    ]
