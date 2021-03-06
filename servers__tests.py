import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError, quicksort_product_list

server_types = (ListServer, MapServer)


class ServerTest(unittest.TestCase):

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertListEqual([products[2], products[1]], entries)

    def test_get_entries_returns_empty_list(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(3)
            self.assertEqual(Counter([]), Counter(entries))

    def test_get_entries_exception_occurs(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1), Product('PP24', 2), Product('PP34', 2)]
        for server_type in server_types:
            server = server_type(products)
            with self.assertRaises(TooManyProductsFoundError):
                entries = server.get_entries(2)


class ClientTest(unittest.TestCase):

    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))

    def test_total_price_for_empty_list(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertIsNone(client.get_total_price(3))

    def test_total_price_for_None(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1), Product('PP24', 2), Product('PP34', 2)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertIsNone(client.get_total_price(2))


if __name__ == '__main__':
    unittest.main()
