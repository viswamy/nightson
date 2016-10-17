from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from tornado import gen


class EventsEntityManager(BaseEntityManager):

    def __init__(self, *args, **kwargs):
        pass

    @gen.coroutine
    def fetch_one(self, id):
        ''' returns one event given an id '''
        sql = ''' SELECT * FROM Events WHERE id={}; '''.format(id)
        cursor = yield self.execute_sql(sql)
        raise gen.Return(cursor.fetchone())

    @gen.coroutine
    def update(self, params):
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
                    '''.format(params.get('name')[0],
                       params.get('latitude')[0],
                       params.get('longitude')[0],
                       params.get('start_time')[0],
                       params.get('end_time')[0],
                       params.get('id')[0]
                       )
        yield self.execute_sql(update_sql)

        ''' query the update record and return it back!'''
        sql = ''' SELECT * FROM Events WHERE id={}; '''.format(params.get('id')[0])
        cursor = yield self.execute_sql(sql)
        raise gen.Return(cursor.fetchone())

    @gen.coroutine
    def insert(self, params):
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
                            id, name, location, start_time, end_time, created_at;
                    '''.format(params.get('name')[0],
                        params.get('latitude')[0],
                        params.get('longitude')[0],
                        params.get('start_time')[0],
                        params.get('end_time')[0]
                    )
        print(insert_sql)
        import pdb; pdb.set_trace();
        cursor = yield self.execute_sql(insert_sql)
        raise gen.Return(cursor.fetchone())



