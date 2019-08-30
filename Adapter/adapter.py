#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod

# Adaptee
class Banner:
    def __init__(self, string: str):
        self.__string = string

    def showWithParen(self):
        print("("+self.__string+")")

    def showWithAster(self):
        print("*"+self.__string+"*")

# Target
class Print(metaclass=ABCMeta):
    @abstractmethod
    def printWeak(self):
        pass

    @abstractmethod
    def printStrong(self):
        pass

# Adapter
class PrintBanner(Print):
    def __init__(self, string:str):
        self.banner = Banner(string)

    def printWeak(self):
        self.banner.showWithParen()

    def printStrong(self):
        self.banner.showWithAster()


# Client
if __name__ == "__main__":
    p = PrintBanner("Hello")
    p.printWeak()
    p.printStrong()
