from app.objects.c_relationship import Relationship
from plugins.stockpile.app.parsers.base_parser import BaseParser
from app.utility.logger import Logger
import re


class Parser(BaseParser):

    def __init__(self, parser_info):
        super().__init__(parser_info)
        self.mappers = parser_info['mappers']
        self.used_facts = parser_info['used_facts']
        self.log = Logger('parsing_svc')

    def sudo_parser(self, text):
        if text and len(text) > 0:
            value = re.search(r'\s+\(\S*\)\s\S+\s(.*)', text)
            if value:
                return [value.group(1)]

    def parse(self, blob):
        relationships = []
        try:
            parse_data = self.sudo_parser(blob)
            for match in parse_data:
                for mp in self.mappers:
                    relationships.append(
                        Relationship(source=(mp.source, match),
                                     edge=mp.edge,
                                     target=(mp.target, None)
                                     )
                    )
        except Exception:
            pass
        return relationships
