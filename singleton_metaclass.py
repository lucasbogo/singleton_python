# Metaclass that creates a Singleton base type when called.

class Singleton(type):
    # Dictionary: the uderscore means that it is not meant to be consumed
    _instances = {}

    # Call method> Check whether or not the class is in the set of instances
    # If it is not, then we construct it and subsequently return it
    def __call__(cls, *args: Any, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
