from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from tornado import gen

class UserEventsManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(UserEventsManager, self).__init__(request)


    @gen.coroutine
    def get_events(self, current_user):
        user_id = current_user.get('id')
        sql = ''' SELECT
                  Events.id AS id,
                  Events.name AS name,
                  Events.description AS description,
                  Events.photo_url AS photo_url,
                  ST_AsGeoJson(Events.location) AS location,
                  Events.start_time AS start_time,
                  Events.end_time AS end_time
                  FROM UsersEvents INNER JOIN Events ON Events.id = UsersEvents.event_id
                  WHERE UsersEvents.user_id = {0} ; '''.format(user_id)
        result = yield self.execute_sql(sql)
        raise gen.Return(result)
