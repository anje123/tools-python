import json
from spdx import document
from spdx.parsers import jsonyamlxml

class Parser(jsonyamlxml.Parser):
    """
    Wrapper class for jsonyamlxml.Parser to provide an interface similar to 
    RDF and TV Parser classes (i.e., spdx.parsers.<format name>.Parser) for JSON parser.
    It also avoids to repeat jsonyamlxml.Parser.parse code for JSON, YAML and XML parsers
    """
    def __init__(self, builder, logger):
        super(Parser, self).__init__(builder, logger)
    
    def parse(self, file):
        self.document_object = json.load(file).get('Document')
        return super(Parser, self).parse()