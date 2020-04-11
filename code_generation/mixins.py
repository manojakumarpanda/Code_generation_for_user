
import uuid



class CustomMixin(object):
    def get_uid(self):
        def getid():
            uid = uuid.uuid4()
            uid = str(uid).split('-')
            code = ''.join(uid)[:14:]
            yield code


        code=getid()
        return code.__next__()

        
