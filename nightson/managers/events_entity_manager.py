from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from tornado import gen


class EventsEntityManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(EventsEntityManager, self).__init__(request)

    @gen.coroutine
    def fetch_one(self):
        ''' returns one event given an id '''

        id = self.get_value('id')
        sql = ''' SELECT
                    id,
                    name,
                    ST_AsGeoJson(location) AS location,
                    start_time,
                    end_time,
                    created_at,
                    deleted_at,
                    updated_at
                    FROM Events WHERE id={};
            '''.format(id)
        cursor = yield self.execute_sql(sql)
        raise gen.Return(cursor.fetchone())

    @gen.coroutine
    def update(self):
        ''' updates a given event and returns the updated object!'''

        update_sql = ''' UPDATE Events SET
                          (
                            name,
                            location,
                            start_time,
                            end_time,
                            updated_at
                            )
                            =
                            (
                              '{0}',
                              ST_GeomFromText('POINT({1} {2})', 4326),
                              to_timestamp({3}),
                              to_timestamp({4}),
                              now()
                            ) where id = {5};
                    '''.format(self.get_value('name'),
                               self.get_value('latitude'),
                               self.get_value('longitude'),
                               self.get_value('start_time'),
                               self.get_value('end_time'),
                               self.get_value('id')
                       )
        yield self.execute_sql(update_sql)

        ''' query the update record and return it back!'''
        result = yield self.fetch_one()
        raise gen.Return(result)

    @gen.coroutine
    def insert(self):
        ''' insert a given into and returns the inserted object!'''

        insert_sql = ''' INSERT INTO Events
                            (
                              name,
                              location,
                              start_time,
                              end_time,
                              created_at
                            )
                            VALUES
                            (
                              '{0}',
                              ST_GeomFromText('POINT({1} {2})', 4326),
                              to_timestamp({3}),
                              to_timestamp({4}),
                              now()
                            )
                            RETURNING
                            id, name, ST_AsGeoJson(location) AS location, start_time, end_time, created_at;
                    '''.format(self.get_value('name'),
                               self.get_value('latitude'),
                               self.get_value('longitude'),
                               self.get_value('start_time'),
                               self.get_value('end_time')
                    )
        cursor = yield self.execute_sql(insert_sql)
        raise gen.Return(cursor.fetchone())



