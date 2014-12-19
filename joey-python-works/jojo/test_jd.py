import abc
import inspect


def foo(name, age=10, sex=0):
    print name
    print age
    print sex

name = ['jiadong']
kwargs = {'age': 33, 'sex': 1}
args = inspect.getcallargs(foo, *name)
#args = inspect.getcallargs(foo, *name, **kwargs)
print args


class Foo(object):
    def __init__(self):
        self.name = None

    def bar(self, name=None):
        self.name = name or 'jiadong'
        print self.name

    @staticmethod
    def output():
        print 'jiadong'

print Foo.bar
print Foo.output
Foo.bar(Foo(), 'jd')

"""bound method"""
m = Foo().bar
m()


class Foo2(Foo):

    default_val = 'jiadong'

    @staticmethod
    def output():
        print 'jd'
    @classmethod
    @abc.abstractmethod
    def input(cls):
        """this is an abstract method"""
        return cls.default_val


class Foo3(Foo2):

    def input(self):
        return '[Ok.' + super(Foo3, self).input()

print Foo3().input()



