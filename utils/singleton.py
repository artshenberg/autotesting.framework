class Singleton:
    def __new__(cls, *args, **kwargs):
        """
        A metaclass that creates a Singleton base class when called.
        (Checks if instance is not presence already.)
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance