from plugins.stockpile.app.parsers.base_parser import BaseParser
from app.objects.c_relationship import Relationship


class Parser(BaseParser):

    def parse(self, blob):
        relationships = []
        for email in self.email(blob):
            for mp in self.mappers:
                relationships.append(
                    Relationship(source=(mp.source, email),
                                 edge=mp.edge,
                                 target=(mp.target, None))
                )
        return relationships
