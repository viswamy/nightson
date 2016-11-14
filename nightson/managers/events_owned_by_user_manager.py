from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from tornado import gen

class EventsOwnedByUserManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(EventsOwnedByUserManager, self).__init__(request)


    @gen.coroutine
    def get_events(self, current_user):
        user_id = current_user.get('id')
        sql = ''' SELECT
                  id,
                  name,
                  ST_AsGeoJson(location) AS location,
                  start_time,
                  end_time
                  FROM Events
                  WHERE created_by_user_id = {0} ; '''.format(user_id)
        result = yield self.execute_sql(sql)
        raise gen.Return(result)
