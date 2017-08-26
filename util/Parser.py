
import argparse

class Parser:
    def __init__(self):
        pass

    def initilaize_arg_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--function", help="run statistical function process", choices=['iqr'])
        return parser.parse_args()
