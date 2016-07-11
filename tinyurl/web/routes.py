from __future__ import absolute_import

from tinyurl.handlers.health import HealthHandler


def get_routes():
    return [
        (r'/health', HealthHandler),
    ]
