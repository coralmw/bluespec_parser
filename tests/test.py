#! python3
import tatsu
from tatsu.model import ModelBuilderSemantics
import sys
import pathlib
import unittest

import unittest

srcdir = pathlib.Path(__file__).parent.parent.absolute()
grammar_path = srcdir / "src" / "grammar_bsv.txt"
grammar = open(grammar_path, 'r').read()

class TestExampleBSVs(unittest.TestCase):

    def test_build_parser(self):
        parser = tatsu.compile(grammar, semantics=ModelBuilderSemantics())

    def test_parse_examples(self):
        parser = tatsu.compile(grammar, semantics=ModelBuilderSemantics())
        for f in pathlib.Path(__file__).parent.glob("*.bsv"):
            with self.subTest(name=f.name):
                with open(f, 'r') as file:
                    ast = parser.parse(file.read())

if __name__ == '__main__':
    unittest.main()
