#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from iterator import Book, BookShelfIterator, BookShelf


class BookShelfPython(BookShelf):
    def __init__(self, *books):
        self.__books = books

    def getBookAt(self, index: int):
        return self.__books[index]

    def appendBook(self, book: Book):
        self.__books.append(book)

    def iterator(self):
        return BookShelfIteratorPython(self)

    def getLength(self):
        return len(self.__books)


class BookShelfIteratorPython(BookShelfIterator):
    def __init__(self, bookShelf: BookShelf):
        super().__init__(bookShelf)
        
    def __iter__(self):
        return self

    def __next__(self):
        '''
        Iterator Interface in python
        '''
        if self.hasNext():
            book = self.next()
            return book
        else:
            raise StopIteration()
    
if __name__ == '__main__':
    bookShelf = BookShelfPython(Book("Japanese"),
                                Book("Math"),
                                Book("Society"),
                                Book("Science"))
    it = bookShelf.iterator()
    for book in it:
        print(book.getName())

    while(it.hasNext()):
        book = it.next()
        print(book.getName())
