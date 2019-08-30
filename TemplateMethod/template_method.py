#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod

class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def op(self):
        pass

    @abstractmethod
    def pp(self):
        pass

    @abstractmethod
    def ed(self):
        pass
    
    def display(self):
        self.op()
        for i in range(5):
            self.pp()
        self.ed()


class CharDisplay(AbstractDisplay):
    def __init__(self, char: str):
        self.__char = char

    def op(self):
        print("<<", end="")

    def pp(self):
        print(self.__char, end="")

    def ed(self):
        print(">>")


class StringDisplay(AbstractDisplay):
    def __init__(self, string:str):
        self.__string = string
        self.__width = len(string.encode())

    def op(self):
        self.printLine()

    def pp(self):
        print("|"+self.__string+"|")

    def ed(self):
        self.printLine()

    def printLine(self):
        print("+", end="")
        for i in range(self.__width):
            print("-", end="")
        print("+")


if __name__ == "__main__":
    chardisp = CharDisplay("H")
    chardisp.display()
    stringdisp = StringDisplay("Hello, World")
    stringdisp.display()
