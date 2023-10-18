import sys
from antlr4 import *
from interpreter.DescLexer import DescLexer
from interpreter.DescParser import DescParser
from interpreter.DescProcessor import DescProcessor


def main(argv):
    tree_and_parser = get_tree_and_parser(argv[1])
    if len(argv) > 2:
        processor = DescProcessor(argv[2])
        start_walking(tree_and_parser[1], processor)
    else:
        get_processor(tree_and_parser[0], tree_and_parser[1])


def get_tree_and_parser(filename):
    input_stream = FileStream(filename)
    lexer = DescLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DescParser(stream)
    return [parser, parser.script()]


def get_processor(parser, tree, repo_path=None):
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
        return None
    else:
        processor = DescProcessor(repo_path)
        walker = ParseTreeWalker()
        walker.walk(processor, tree)
        return processor

def start_walking(tree, processor):
    walker = ParseTreeWalker()
    walker.walk(processor, tree)


if __name__ == '__main__':
    main(sys.argv)