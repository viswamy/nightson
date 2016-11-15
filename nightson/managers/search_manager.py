from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from nightson.managers.session_manager import SessionManager
from tornado import gen
import bcrypt

class SearchManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(SearchManager, self).__init__(request)

    @gen.coroutine
    def get_events(self):
        latitude = self.get_value('latitude')
        longitude = self.get_value('longitude')
        radius = self.get_value('radius')
        sql = ''' SELECT
                    id,
                    name,
                    description,
                    photo_url,
                    created_by_user_id,
                    ST_AsGeoJson(location) AS location,
                    start_time,
                    end_time
                    FROM Events WHERE
                    ST_DWithin(location, ST_GeomFromText('POINT({0} {1})', 4326), {2});
                    '''.format(longitude, latitude, radius)
        cursor = yield self.execute_sql(sql)
        result = cursor.fetchall()

        raise gen.Return(result)



