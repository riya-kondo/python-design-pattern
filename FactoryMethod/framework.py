#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def _createProduct(self, owner:str) -> Product:
        pass

    @abstractmethod
    def _registerProduct(self, product:Product):
        pass

    def create(self, owner: str) -> Product:
        p = self._createProduct(owner)
        self._registerProduct(p)
        return p
