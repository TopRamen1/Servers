#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List
from abc import ABC, abstractmethod


class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    def __init__(self, name_: str, price_: float):
        self.name = name_
        self.price = price_
        name_char_ = []
        for char in self.name:
            if char.isalpha():
                name_char_.append(char)

        self.name_char = name_char_


    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


class ServerErr(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = "Error occured"

        super().__init__(msg)

class TooManyProductsFoundError(ServerErr):
    def __init__(self):
        msg = "To many products found"
        super().__init__(msg)



# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania


class Server(ABC):

    @abstractmethod
    def get_entries(self, n: int) -> List[Product]:
        pass

    @abstractmethod
    def to_many_products_error(self) -> TooManyProductsFoundError:
        pass

class ListServer(Server):

    def __init__(self, products_list_: List[Product], n_max_returned_entries_: int = 1):
        self.products_list=products_list_[:]
        self.n_max_returned_entries = n_max_returned_entries_

    def to_many_products_error(self) -> TooManyProductsFoundError:
        raise TooManyProductsFoundError

    def get_entries(self, n: int) -> List[Product]:
        result = []
        for e in self.products_list:
            if len(e.name_char) == n:
                result.append(e)

        if len(result) > self.n_max_returned_entries:
            self.to_many_products_error()

        return result


class MapServer:
    pass


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        pass

    pass