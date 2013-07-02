class Singleton(object):
    """ A Pythonic Singleton
    Just have your class inherit from Singleton,
    and don't override __new__. Then, all calls to that class
    (normally creations of new instances) return the same instance.
    (The instance is created once, on the first such call to each given
    subclass of Singleton during each run of your program.)
    """

    def __new__(cls, *args, **kwargs):
        if '_inst' not in vars(cls):
            cls._inst = object.__new__(cls, *args, **kwargs)
        return cls._inst

