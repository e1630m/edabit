class Employee:
    def __init__(self, name, **kwargs):
        self.name, self.lastname = name.split()
        self.__dict__.update(kwargs)
