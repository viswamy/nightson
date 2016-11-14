from __future__ import absolute_import

import httplib

from nightson.handlers.auth import AuthHandler
from tornado import gen
from nightson.managers.user_events_manager import SubscribeManager
import ujson
import uuid

__UPLOADS__ = 'uploads/'
__STATIC__ = 'static/'
class UploadHandler(AuthHandler):

    @gen.coroutine
    def post(self):
        ''' Uploads a file and returns the url of the file! '''
        file = self.request.files['file_name'][0]
        file_extension = file['filename'].split('.')[-1]
        cname = str(uuid.uuid4()) + '.' + file_extension
        path = __UPLOADS__ + cname
        fp  = open(path, 'w')
        fp.write(file['body'])
        self.set_status(httplib.OK)
        self.write({
            'message': 'file succesfully uploaded',
            'path': __STATIC__ + cname
        })