#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError


class ServerTest(unittest.TestCase):

    def test_List_Server_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]

        server = ListServer(products, 2)
        entries = server.get_entries(2)
        self.assertEqual(Counter([products[2], products[1]]), Counter(entries))

    def test_List_Server_get_entries_returns_empty_list(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]

        server = ListServer(products)
        entries = server.get_entries(3)
        self.assertEqual(Counter([]), Counter(entries))

    def test_List_Server_get_entries_raises_error(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]

        server = ListServer(products)

        with self.assertRaises(Exception) as context:
            server.get_entries(2)

        self.assertTrue("To many products found" in str(context.exception))

if __name__ == '__main__':
    unittest.main()