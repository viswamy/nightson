from __future__ import absolute_import

from nightson.managers.base_entity_manager import BaseEntityManager
from nightson.managers.session_manager import SessionManager
from tornado import gen
import bcrypt

class LoginManager(BaseEntityManager):

    def __init__(self):
        pass

    def __init__(self, request):
        super(LoginManager, self).__init__(request)

    @gen.coroutine
    def get_token(self):
        email = self.get_value('email')
        password = self.get_value('password')
        sql = ''' SELECT id, email, password FROM Users WHERE email = '{0}' '''.format(email)
        cursor = yield self.execute_sql(sql)
        result = cursor.fetchone()

        hashed_password = result.get('password')

        token_result = {}
        if(bcrypt.hashpw(password, hashed_password) == hashed_password):
            session_manager = SessionManager(self.request)
            token_result = yield session_manager.create_token(result.get('id'))

        raise gen.Return(token_result)



