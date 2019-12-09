from typing import Optional, List, Dict
from abc import ABC, abstractmethod
import re


class Product:
    def __init__(self, name_: str, price_: float):
        self.name = name_
        self.price = price_

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


class ServerErr(Exception):
    def __init__(self, msg="Server Error"):
        super().__init__(msg)


class TooManyProductsFoundError(ServerErr):
    def __init__(self, msg="To many products found"):
        super().__init__(msg)


class Server(ABC):
    n_max_returned_entries = 3

    @abstractmethod
    def get_entries(self, n: int) -> List[Product]:
        pass

    @abstractmethod
    def to_many_products_error(self) -> TooManyProductsFoundError:
        pass


class ListServer(Server):

    def __init__(self, products_list_: List[Product]):
        self.products_list = products_list_[:]

    def to_many_products_error(self) -> TooManyProductsFoundError:
        raise TooManyProductsFoundError

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        result = []
        for product in self.products_list:
            search_pattern = re.compile('^[a-zA-Z]{{{n}}}\\d{{2,3}}$'.format(n=n_letters))
            if re.match(search_pattern, product.name):
                result.append(product)

        if len(result) > self.n_max_returned_entries:
            self.to_many_products_error()

        return quicksort_product_list(result)


class MapServer(Server):

    def __init__(self, products_list_: List[Product]):
        self.products_dict = {}

        for product in products_list_:
            self.products_dict[product.name] = product

    def to_many_products_error(self) -> TooManyProductsFoundError:
        raise TooManyProductsFoundError

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        result = []
        for name, product in self.products_dict.items():
            search_pattern = re.compile('^[a-zA-Z]{{{n}}}\\d{{2,3}}$'.format(n=n_letters))
            if re.match(search_pattern, product.name):
                result.append(product)

        if len(result) > self.n_max_returned_entries:
            self.to_many_products_error()

        return quicksort_product_list(result)


class Client:
    def __init__(self, server_: Server):
        self.server = server_

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        total_price = 0

        try:
            list_of_products = self.server.get_entries(n_letters)
        except TooManyProductsFoundError:
            return None

        for elem in list_of_products:
            total_price = total_price + elem.price
        return total_price


def quicksort_product_list(lst: List[Product]) -> List[Product]:
    def quicksort_inplace(lst_in: List[Product], start_: int = 0, stop_: int = None) -> None:
        i = start_
        j = stop_
        piv = lst_[(i+j)//2]
        while i < j:
            while lst_in[i].price < piv.price:
                i = i + 1
            while lst_in[j].price > piv.price:
                j = j - 1
            if i <= j:
                lst_in[i], lst_in[j] = lst_in[j], lst_in[i]
                i = i + 1
                j = j - 1
        if start_ < j:
            quicksort_inplace(lst_in, start_, j)
        if i < stop_:
            quicksort_inplace(lst_in, i, stop_)

    if len(lst) <= 0:
        return lst
    stop = len(lst) - 1
    start = 0
    lst_ = lst[:]
    quicksort_inplace(lst_, start, stop)
    return lst_
