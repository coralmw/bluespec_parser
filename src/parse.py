#! python3
import tatsu
from tatsu.model import ModelBuilderSemantics
import sys
import argparse
import pathlib

srcdir = pathlib.Path(__file__).parent.absolute()

parser = argparse.ArgumentParser(description='parse a bsv file.')
parser.add_argument('--grammar', metavar='G', type=str,
                    help='EBNF file containing the bsv grammar.',
                    default=srcdir / "grammar_bsv.txt")
parser.add_argument('source', metavar='I', type=str,
                    help='bsv file.')
parser.add_argument('-t', '--trace', action="store_true",
                    help='Display parse trace (for debugging).')

args = parser.parse_args()

grammar = open(args.grammar, "r").read()
parser = tatsu.compile(grammar, semantics=ModelBuilderSemantics())
ast = parser.parse(open(args.source, "r").read(), trace=args.trace, colorize=True)
print("parsed.")
