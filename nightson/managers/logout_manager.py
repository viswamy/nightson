from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from nightson.managers.session_manager import SessionManager
from tornado import gen
import bcrypt

class LogoutManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(LogoutManager, self).__init__(request)

    @gen.coroutine
    def logout_current_session(self, user):
        session_token = user['token']
        sql = '''DELETE FROM Sessions WHERE token = {0}'''.format(session_token)
        yield self.execute_sql(sql)
        raise gen.Return({
            'message': 'successfully terminated the session!'
        })

    @gen.coroutine
    def logout_all_sessions(self, user):
        current_user = user['id']
        sql = ''' DELETE FROM Sessions WHERE user_id = {0}'''.format(current_user)
        yield self.execute_sql(sql)
        raise gen.Return({
            'message': 'successfully terminated ALL sessions!'
        })

    @gen.coroutine
    def logout(self, user):
        all_sessions = (self.get_value('all_sessions') == 'true')
        result = {}
        if(all_sessions):
            result = yield self.logout_all_session(user)
        else:
            result = yield self.logout_current_session(user)
        raise gen.Return(result)


