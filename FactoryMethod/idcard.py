#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from framework import *

class IDCard(Product):
    def __init__(self, owner:str):
        print("start to create" + owner + "'s card...")
        self.__owner = owner

    def use(self):
        print(self.__owner + "'s card is used...")

    def getOwner(self) -> str:
        return self.__owner


class IDCardFactory(Factory):
    def __init__(self):
        self.__owners = []

    def _createProduct(self, owner: str) -> Product:
        return IDCard(owner)

    def _registerProduct(self, product: Product):
        self.__owners.append(product.getOwner())

    def getOwners(self) -> list:
        return self.__owners


if __name__ == "__main__":
    factory = IDCardFactory()
    card1 = factory.create("Riiya Kondo")
    card2 = factory.create("Black Magician Girl")
    card1.use()
    card2.use()
    print(factory.getOwners())
