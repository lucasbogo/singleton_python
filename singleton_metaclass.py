# Metaclass that creates a Singleton base type when called.
# Message 'Loading Database' only gets invoked once, thus, completing the functionality of a singleton class
# The code is very similar to the 'decorator' example

class Singleton(type):
    # Dictionary: the uderscore means that it is not meant to be consumed
    _instances = {}

    # Call method> Check whether or not the class is in the set of instances
    # If it is not, then we construct it and subsequently return it
    def __call__(cls, *args, **kwargs):
        # Check if cls is in instance
        if cls not in cls._instances:
             # If it is not, then we construct it
            cls._instances[cls] = super(Singleton, cls)\
            .__call__(*args, **kwargs) # Call the initializer with the arguments and keyword arguments
        return cls._instances[cls] # Then return instances

# Use the metaclass singleton
class Database(metaclass=Singleton):
    # Initialize
    def __init__(self):
        print('Loading database')

# Test
if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
