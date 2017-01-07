class GoodLock(object):
    def __init__(self):
        print "intialize it"

    def __enter__(self):
        print "lock it"
        return "got it"

    def __exit__(self, exc_type, exc_value, traceback):
        print "release it"
        print exc_type, exc_value, traceback

def return_in_lock():
    with GoodLock() as lock:
        print lock
        print "execute it"
        return

return_in_lock()
