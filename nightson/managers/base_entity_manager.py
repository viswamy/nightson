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

class BaseEntityManager(object):

    db = initialize_database()

    def __init__(self):
        pass

    def __init__(self, request):
        self.request = request

    @gen.coroutine
    def execute_sql(self, sql):
        ''' Executes an sql statement and returns the value '''
        cursor = yield BaseEntityManager.db.execute(sql)
        raise gen.Return(cursor)

    def get_value(self, key):
        ''' Gets a value given dictionary like arguments'''
        params = {}
        if(self.request.method == 'GET'):
            params = self.request.query_arguments
        elif(self.request.method == 'POST'):
            params = self.request.body_arguments
        elif(self.request.method == 'PUT'):
            params = self.request.arguments
        elif(self.request.method == 'DELETE'):
            params = self.request.body_arguments

        if(key not in params):
            return None

        ''' Params will always be of the form key:[values] '''
        return params.get(key)[0]