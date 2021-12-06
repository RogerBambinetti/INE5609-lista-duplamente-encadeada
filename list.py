from element import Element


class List:

    def __init__(self, size: int):
        self.__cursor = None
        self.__start = None
        self.__ending = None
        self.__size = size
        self.__count = 0

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def ending(self):
        return self.__ending

    @ending.setter
    def ending(self, ending):
        self.__ending = ending

    # -----------

    def acessarAtual(self):
        return self.__cursor

    def inserirAntesDoAtual(self, value):
        if not self.cheia():

            previous = self.__cursor.previous
            cursor = self.__cursor

            element = Element(previous, value, cursor)

            previous.next = element
            cursor.previous = element

            self.__count += 1
        else:
            raise Exception

    def inserirApósAtual(self, value):
        if not self.cheia():

            next = self.__cursor.next
            cursor = self.__cursor

            element = Element(cursor, value, next)

            next.previous = element
            cursor.next = element

            self.__count += 1
        else:
            raise Exception

    def inserirNoFim(self, value):
        if self.vazio():

            element = Element(None, value, None)

            self.__cursor = element

            self.__start = element
            self.__ending = element

            self.__count += 1

        elif not self.cheia():

            self.irParaUltimo()
            cursor = self.__cursor

            element = Element(cursor, value, None)

            cursor.next = element
            self.__ending = element

            self.__cursor = element

            self.__count += 1
        else:
            raise Exception

    def inserirNaFrente(self, value):
        if self.vazio():

            element = Element(None, value, None)

            self.__cursor = element

            self.__start = element
            self.__ending = element

            self.__count += 1

        elif not self.cheia():

            self.irParaPrimeiro()
            cursor = self.__cursor

            element = Element(None, value, cursor)

            cursor.previous = element
            self.__start = element

            self.__cursor = element

            self.__count += 1
        else:
            raise Exception

    def inserirNaPosicao(self, k, value):
        if not self.cheia():

            p = self.posiçãoDe(self.__cursor)

            if k > p:
                n = k - p
                self.avançarKPosições(n)
            elif k < p:
                n = p - k
                self.retrocederKPosições(n)

            previous = self.__cursor.previous
            cursor = self.__cursor

            element = Element(previous, value, cursor)

            previous.next = element
            cursor.previous = element

            self.__count += 1

        else:
            raise Exception

    def excluirAtual(self):
        if not self.vazia():

            previous = self.__cursor.previous
            next = self.__cursor.next

            previous.next = next
            next.previous = previous
            self.__cursor = previous

            self.__count -= 1

        else:
            raise Exception

    def excluirPrim(self):
        if not self.vazia():

            if self.__ending == self.__start:

                self.__start = None
                self.__ending = None

                self.__cursor = None

                self.__count -= 1

            else:

                self.irParaPrimeiro()

                next = self.__cursor.next

                next.previous = None

                self.__cursor = next
                self.__start = next

                self.__count -= 1

        else:
            raise Exception

    def excluirUlt(self):
        if not self.vazia():

            if self.__ending == self.__start:

                self.__start = None
                self.__ending = None

                self.__cursor = None

                self.__count -= 1

            else:

                self.irParaUltimo()

                previous = self.__cursor.previous

                previous.next = None

                self.__cursor = previous
                self.__ending = previous

                self.__count -= 1

        else:
            raise Exception

    def excluirElem(self, key):
        if not self.vazia():

            if self.buscar(key):

                element = key

                previous = element.previous
                next = element.next

                previous.next = next
                next.previous = previous

                self.__count -= 1

        else:
            raise Exception

    def excluirDaPos(self, k):
        if not self.vazia():

            p = self.posiçãoDe(self.__cursor)

            if k > p:
                n = k - p
                self.avançarKPosições(n)
            elif k < p:
                n = p - k
                self.retrocederKPosições(n)

            previous = self.__cursor.previous
            next = self.__cursor.next

            previous.next = next
            next.previous = previous
            self.__cursor = previous

            self.__count -= 1

        else:
            raise Exception

    def buscar(self, key):
        return 1

    def avançarKPosições(self, K):
        cursor_position = self.posiçãoDe(self.__cursor)
        position = cursor_position + K

        if(position < self.__size):
            element = self.__cursor
            for x in range(cursor_position, position):
                element = element.next
            self.__cursor = element
        else:
            raise Exception

    def retrocederKPosições(self, K):
        cursor_position = self.posiçãoDe(self.__cursor)
        position = cursor_position - K

        if(position < self.__size):
            element = self.__cursor
            for x in range(position, cursor_position):
                element = element.previous
            self.__cursor = element
        else:
            raise Exception

    def irParaPrimeiro(self):
        self.__cursor = self.__start

    def irParaUltimo(self):
        self.__cursor = self.__ending

    def vazia(self):
        if (self.__count == 0):
            return True
        else:
            return False

    def cheia(self):
        if (self.__end == self.__size):
            return True
        else:
            return False

    def posiçãoDe(self, key):
        element = self.__start

        for x in range(0, self.__count):
            if element == key:
                return x
            element = element.next
