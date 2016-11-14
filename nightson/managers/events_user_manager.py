from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from tornado import gen

class EventUsersManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(EventUsersManager, self).__init__(request)


    @gen.coroutine
    def get_users(self):
        event_id = self.get_value('event_id')
        sql = ''' SELECT
                  Users.id,
                  Users.first_name,
                  Users.last_name,
                  Users.photo_url,
                  ST_AsGeoJson(location) AS location,
                  Users.location_recorded_at
                  FROM UsersEvents INNER JOIN Users ON Users.id = UsersEvents.user_id
                  WHERE event_id = {0} ; '''.format(event_id)
        result = yield self.execute_sql(sql)
        raise gen.Return(result)
