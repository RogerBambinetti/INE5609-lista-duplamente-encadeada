class Element:

    def __init__(self, value: int, next):
        self.__value = value
        self.__next = next

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
