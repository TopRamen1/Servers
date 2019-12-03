#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List
from abc import ABC, abstractmethod


class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    def __init__(self, name: str, price: float):
        self.name_=name
        self.price_=price



    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass


# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania


class Server(ABC):

    @abstractmethod
    def search_in_products(self, n: int) -> List[Product]:
        pass

    @abstractmethod
    def to_many_products_error(self) -> TooManyProductsFoundError:
        pass

class ListServer(Server):

    def __init__(self, products_list: List[Product], n_max_returned_entries: int):
        self.products_list_=products_list[:]
        self.n_max_returned_entries_=n_max_returned_entries

    def search_in_products(self, n: int) -> List[Product]:
        result=[]
        for e in self.products_list_:
            if e.
        pass

    def to_many_products_error(self) -> TooManyProductsFoundError:
        pass


class MapServer:
    pass


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]: