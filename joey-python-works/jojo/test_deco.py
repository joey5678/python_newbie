import sys

from sortedcontainers import SortedList, SortedSet, SortedDict

def is_author(f):
    """ add a wrapper func
    """

    def wrapper(*args, **kwargs):

        if kwargs.get('username', '') != 'jiadong':
            # raise Exception('This is a exception')
            kwargs['error_info'] = 'error occurs.'
        else:
            kwargs['error_info'] = 'no error.'
        return f(*args, **kwargs)

    return wrapper


def foo(msg, username='dongjia', error_info=None):
    print msg
    if error_info is not None:
        print error_info

is_author(foo)('it is a msg', username='jiadong1')


@is_author
def foo_me(msg, username='', error_info=None):
    print msg
    if error_info is not None:
        print error_info

foo_me('is another msg', username='jiadong')


GLOBAL_MAP = {}


def is_me_params(*args, **kwargs):

    if kwargs['extra'] is not None:
        print kwargs['extra']
    global GLOBAL_MAP

    def _deco(f):
        def wrapper(*fargs, **fkwargs):
            print 'is deco...'
            return f(*fargs, **fkwargs)

        return wrapper

    return _deco


@is_me_params(extra='good boy')
def foo_me_params(msg):
    print msg


foo_me_params('foo with deco + params')

_dict = SortedDict({'c': '1c', '123': 'c123', 'a': 'a'})
print _dict