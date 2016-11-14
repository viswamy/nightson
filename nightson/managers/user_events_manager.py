from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from nightson.managers.session_manager import SessionManager
from tornado import gen
import bcrypt

class SubscribeManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(SubscribeManager, self).__init__(request)

    @gen.coroutine
    def subscribe_user(self, current_user):
        event_id = self.get_value('event_id')
        user_id = current_user.get('id')
        sql = ''' INSERT INTO UsersEvents(
                    user_id,
                    event_id
                    )
                    VALUES
                    (
                    {0},
                    {1}
                    )
                    RETURNING user_id, event_id;
                    '''.format(user_id, event_id)
        cursor = yield self.execute_sql(sql)
        result = cursor.fetchone()
        raise gen.Return(result)


    @gen.coroutine
    def unsubscribe_user(self, current_user):
        event_id = self.get_value('event_id')
        user_id = current_user.get('id')
        sql = ''' DELETE FROM UsersEvents WHERE user_id = {0} AND event_id = {1}; '''.format(user_id, event_id)
        yield self.execute_sql(sql)
        raise gen.Return( {
            'message': 'unsubscibed user successfuly!'
        })


