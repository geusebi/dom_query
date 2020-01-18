import unittest
from os import path
from .utils import parse_dom

from xml.dom.minidom import Document

from pydom_query import query

__all__ = ("TestQuery", )


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.doc_path = path.join(path.dirname(__file__), "html")
        self.trees = {}

        self.loadTree("doc1")

    def loadTree(self, name):
        filename = f"{name}.html"
        filepath = path.join(self.doc_path, filename)

        with open(filepath) as fh:
            self.trees[name] = parse_dom(fh)

    def testTreeLoaded(self):
        self.assertIsInstance(self.trees["doc1"], Document)

    def testElementsOrder(self):
        pars = query(self.trees["doc1"], "p")

        count = 7
        with self.subTest(count=count):
            self.assertEqual(count, len(pars))

        for i, par in enumerate(pars, 1):
            with self.subTest(i=i):
                text = par.childNodes[0].data.strip()
                expect = f"paragraph{i}"
                self.assertEqual(text, expect)

    def testTagType(self):
        pars = query(self.trees["doc1"], "p")

        for i, par in enumerate(pars, 1):
            with self.subTest(i=i):
                self.assertEqual(par.tagName, "p")

    def testChildren(self):
        doc = self.trees["doc1"]
        foot = query(doc, "footer#foot1")[0]
        pars = query(doc, "footer#foot1 > p")
        count = 2

        self.assertEqual(len(pars), count)

        for i, par in enumerate(pars, 1):
            with self.subTest(i=i):
                self.assertEqual(par.tagName, "p")
                self.assertIn(par, foot.childNodes)
