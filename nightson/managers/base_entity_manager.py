from __future__ import absolute_import

import momoko
from tornado import gen
from psycopg2.extras import RealDictConnection


def initialize_database():
    db = momoko.Pool(
        dsn='''dbname=nightson user=vswamy password=vswamy host=localhost port=5432''',
        size=5,
        connection_factory=RealDictConnection,
    )
    db.connect()
    return db

class BaseEntityManager:

    db = initialize_database()

    def __init__(self, *args, **kwargs):
        pass

    @gen.coroutine
    def execute_sql(self, sql):
        ''' Executes an sql statement and returns the value '''
        cursor = yield BaseEntityManager.db.execute(sql)
        raise gen.Return(cursor)