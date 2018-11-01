
class SayHello:
    def __init__(self, name):
        self.__name__ = name

    def hello(self):
        print("Hello, " + self.__name__)
