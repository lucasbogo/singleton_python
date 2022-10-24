# The database runs only once
# The initializer doesnt get called several times
# This solves the problem enccountered in singleton_allocator, where the the initilizer gets called more than once


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

# decorator = @singleton
@singleton
class Database:
    def __init__(self):
        print('Loading Database')

if __name__== '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)