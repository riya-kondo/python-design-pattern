#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class AggregateInterface(metaclass=ABCMeta):
    @abstractmethod
    def iterator(self):
        pass

class IteratorInterface(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self) -> bool:
        pass

    def next(self) -> object:
        pass

class Book:
    def __init__(self, name: str):
        self.__name = name

    def getName(self):
        return self.__name

class BookShelf(AggregateInterface):
    def __init__(self, maxSize: int):
        self.__books = []
        self.__last = maxSize

    def getBookAt(self, index: int):
        return self.__books[index]

    def appendBook(self, book: Book):
        self.__books.append(book)

    def getLength(self):
        return len(self.__books)

    def iterator(self):
        return BookShelfIterator(self)

class BookShelfIterator(IteratorInterface):
    def __init__(self, bookshelf: BookShelf):
        self.__bookshelf = bookshelf
        self.__index = 0

    def hasNext(self):
        if self.__index < self.__bookshelf.getLength():
            return True
        else:
            return False

    def next(self):
        book = self.__bookshelf.getBookAt(self.__index)
        self.__index += 1
        return book

if __name__ == '__main__':
    bookShelf = BookShelf(4)
    bookShelf.appendBook(Book("Japanese"))
    bookShelf.appendBook(Book("Math"))
    bookShelf.appendBook(Book("Society"))
    bookShelf.appendBook(Book("Science"))
    it = bookShelf.iterator()
    while it.hasNext():
        book = it.next()
        print(book.getName())
