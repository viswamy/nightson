from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from tornado import gen
import bcrypt
import uuid

class SessionManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(SessionManager, self).__init__(request)

    @gen.coroutine
    def create_token(self, user_id):
        ''' Creates a token for a particular user_id '''
        token_hash = bcrypt.hashpw(str(uuid.uuid4()), bcrypt.gensalt())
        sql = '''
                INSERT INTO Sessions(
                    user_id,
                    token,
                    created_at
                  )
                  VALUES
                  (
                    {0},
                    '{1}',
                    now()
                  )
                  RETURNING user_id, token, created_at, expires_at
            '''.format(user_id, token_hash)
        cursor = yield self.execute_sql(sql)
        result = cursor.fetchone()
        raise gen.Return(result)

    @gen.coroutine
    def authenticate_token(self):
        ''' Authenticates a token and returns the relevant User Object!'''

        headers = self.request.headers
        token = headers.get('x-auth-token')
        if not token:
            raise gen.Return(None)

        sql = ''' SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.photo_url,
            u.phone,
            ST_AsGeoJson(u.location) as location,
            u.location_recorded_at,
            u.created_at,
            u.updated_at,
            u.deleted_at,
            s.token as token
        FROM Users AS u INNER JOIN Sessions s ON (u.id = s.user_id)
        WHERE s.token = '{0}';
        '''.format(token)

        cursor = yield self.execute_sql(sql)
        result = cursor.fetchone()
        raise gen.Return(result)



