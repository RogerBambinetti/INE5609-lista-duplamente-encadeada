class Element:

    def __init__(self, previous, value: int, next):
        self.__previous = previous
        self.__value = value
        self.__next = next

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, previous):
        self.__previous = previous

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next
