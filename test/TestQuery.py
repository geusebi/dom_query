import unittest
from os import path
from xml.dom.minidom import Document
from dom_query import select, select_all
from .utils import parse_dom

__all__ = ("TestQuery", )


def beginning_text(elem):
    try:
        return elem.childNodes[0].data.strip()
    except (IndexError, AttributeError):
        return None


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.doc_path = path.join(path.dirname(__file__), "html")
        self.trees = {}

        self.loadTree("doc1")
        self.loadTree("doc2")
        self.loadTree("doc3")

    def loadTree(self, name):
        filename = f"{name}.html"
        filepath = path.join(self.doc_path, filename)

        with open(filepath) as fh:
            self.trees[name] = parse_dom(fh)

    def testTreeLoaded(self):
        self.assertIsInstance(self.trees["doc1"], Document)

    def testElementsOrder(self):
        pars = select_all(self.trees["doc1"], "p")

        count = 7
        with self.subTest(count=count):
            self.assertEqual(count, len(pars))

        for i, par in enumerate(pars, 1):
            with self.subTest(p=i):
                text = beginning_text(par)
                expect = f"paragraph{i}"
                self.assertEqual(text, expect)

    def testTagType(self):
        pars = select_all(self.trees["doc1"], "p")

        for i, par in enumerate(pars, 1):
            with self.subTest(p=i):
                self.assertEqual(par.tagName, "p")

    def testTagCapitalization(self):
        with self.subTest(msg="tag name"):
            pars = select_all(self.trees["doc1"], "P")
            self.assertAlmostEqual(len(pars), 7)

        with self.subTest(msg="attr name"):
            pars = select_all(self.trees["doc1"], "p[DATA-user]")
            self.assertAlmostEqual(len(pars), 1)

    def testChildren(self):
        doc = self.trees["doc1"]
        foot = select(doc, "footer#foot1")
        pars = select_all(doc, "footer#foot1 > p")
        count = 2

        self.assertEqual(len(pars), count)

        for i, par in enumerate(pars, 1):
            with self.subTest(p=i):
                self.assertEqual(par.tagName, "p")
                self.assertIn(par, foot.childNodes)

    def testAttributes(self):
        doc = self.trees["doc2"]

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
                pars = select_all(doc, selector)
                self.assertEqual(len(pars), 1)
                self.assertEqual(beginning_text(pars[0]), text)

        #  This is for coverage of a 'begins match' with
        #  missing attribute
        with self.subTest(type="missing begins"):
            pars = select(doc, "#p0[data-missing|=value]")
            self.assertEqual(pars, None)

    def testClasses(self):
        doc = self.trees["doc1"]

        with self.subTest():
            pars = select_all(doc, "*.cls1")
            self.assertEqual(len(pars), 2)
            self.assertEqual(beginning_text(pars[0]), "paragraph2")
            self.assertEqual(beginning_text(pars[1]), "paragraph4")

        with self.subTest():
            pars = select_all(doc, "*.cls1.cls2")
            self.assertEqual(len(pars), 1)
            self.assertEqual(beginning_text(pars[0]), "paragraph4")

        with self.subTest():
            pars = select_all(doc, "*.cls2.cls3")
            self.assertEqual(len(pars), 0)

    def testSiblingsNext(self):
        doc = self.trees["doc3"]
        pars = select_all(doc, "p + p")
        par_nums = (1, 2, 4, 5, 6, 7, )

        self.assertEqual(len(pars), len(par_nums))

        for i, par in zip(par_nums, pars):
            with self.subTest(p=i):
                text = beginning_text(par)
                expect = f"paragraph{i}"
                self.assertEqual(text, expect)

    def testSiblingsSubsequent(self):
        doc = self.trees["doc3"]
        pars = select_all(doc, "h1 ~ p")
        par_nums = (3, 4, 5, 6, 7, )

        self.assertEqual(len(pars), len(par_nums))

        for i, par in zip(par_nums, pars):
            with self.subTest(p=i):
                text = beginning_text(par)
                expect = f"paragraph{i}"
                self.assertEqual(text, expect)
