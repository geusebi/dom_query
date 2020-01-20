import unittest
from os import path
from xml.dom.minidom import Document
from pydom_query import query
from .utils import parse_dom

__all__ = ("TestQuery", )


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.doc_path = path.join(path.dirname(__file__), "html")
        self.trees = {}

        self.loadTree("doc1")
        self.loadTree("doc2")

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
            with self.subTest(p=i):
                text = par.childNodes[0].data.strip()
                expect = f"paragraph{i}"
                self.assertEqual(text, expect)

    def testTagType(self):
        pars = query(self.trees["doc1"], "p")

        for i, par in enumerate(pars, 1):
            with self.subTest(p=i):
                self.assertEqual(par.tagName, "p")

    def testChildren(self):
        doc = self.trees["doc1"]
        foot = query(doc, "footer#foot1")[0]
        pars = query(doc, "footer#foot1 > p")
        count = 2

        self.assertEqual(len(pars), count)

        for i, par in enumerate(pars, 1):
            with self.subTest(p=i):
                self.assertEqual(par.tagName, "p")
                self.assertIn(par, foot.childNodes)

    def testSiblings(self):
        doc = self.trees["doc2"]
        pars = query(doc, "p + p")
        count = 6

        self.assertEqual(len(pars), count)

        par_nums = (1, 2, 4, 5, 6, 7, )
        for i, par in zip(par_nums, pars):
            with self.subTest(p=i):
                text = par.childNodes[0].data.strip()
                expect = f"paragraph{i}"
                self.assertEqual(text, expect)

    def testAttributes(self):
        doc = self.trees["doc2"]

        def beginning_text(elem):
            try:
                return elem.childNodes[0].data.strip()
            except (IndexError, AttributeError):
                return None

        expected = [
            ["paragraph0", "p#p0[data-attr]",        "presence"],
            ["paragraph1", "p#p1[data-attr=value1]", "equal"],
            ["paragraph2", "p#p2[data-attr~=word]",  "word"],
            ["paragraph3", "p#p3[data-attr^=val]",   "starts"],
            ["paragraph4", "p#p4[data-attr$=lue4]",  "ends"],
            ["paragraph5", "p#p5[data-attr|=val]",   "begins"],
            ["paragraph6", "p#p6[data-attr|=val]",   "begins dash"],
            ["paragraph7", "p#p7[data-attr*=alu]",   "contains"],
        ]

        for text, selector, message in expected:
            with self.subTest(type=message):
                pars = query(doc, selector)
                self.assertEqual(len(pars), 1)
                self.assertEqual(beginning_text(pars[0]), text)
