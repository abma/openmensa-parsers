import importlib

from utils import ParserNotFound, CanteenPrefixer, ParserRenamer


parsers = {}


def register_parser(parser):
    parsers[parser.name] = parser


def parse(request, parser_name, *args):
    if parser_name in parsers:
        return parsers[parser_name].parse(request, *args)
    else:
        raise ParserNotFound(parser_name)


for module in [
    'aachen',
    'dresden',
    'hamburg',
    'hannover',
    'karlsruhe',
    'leipzig',
    'magdeburg',
    'muenchen',
    'marburg',
    'niederbayern_oberpfalz',
    'ostniedersachsen',
    'wuerzburg',
]:
    register_parser(importlib.import_module(module).parser)


register_parser(CanteenPrefixer('braunschweig', 'ostniedersachsen'))
register_parser(ParserRenamer('clausthal', 'ostniedersachsen'))
register_parser(CanteenPrefixer('braunschweig', 'ostniedersachsen'))
register_parser(ParserRenamer('suderburg', 'ostniedersachsen'))
register_parser(CanteenPrefixer('wolfenbuettel', 'ostniedersachsen'))
register_parser(CanteenPrefixer('holzminden', 'ostniedersachsen'))
