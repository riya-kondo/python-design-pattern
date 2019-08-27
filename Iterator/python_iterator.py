#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from iterator import Book, BookShelfIterator, AggregateInterface

class BookShelf(AggregateInterface):
    def __init__(self, *books):
        self.__books = books
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        '''
        Iterator Interface in python
        '''
        if self.__index == len(self.__books):
            self.__index = 0
            raise StopIteration()
        book = self.__books[self.__index]
        self.__index += 1
        return book

    def iterator(self):
        return BookShelfIterator(self)

    def getBookAt(self, index: int):
        return self.__books[index]

    def getLength(self):
        return len(self.__books)

if __name__ == '__main__':
    bookShelf = BookShelf(Book("Japanese"),
                          Book("Math"),
                          Book("Society"),
                          Book("Science"))
    it = bookShelf.iterator()
    for book in bookShelf:
        print(book.getName())

    while(it.hasNext()):
        book = it.next()
        print(book.getName())
