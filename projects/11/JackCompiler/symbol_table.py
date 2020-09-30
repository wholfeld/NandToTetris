from enum_dictionaries import KindTypes


class SymbolTable():
    def __init__(self):
        self.symbol_dictionary = {}
        self.kind_dictionary = {}

    def start_subroutine(self):
        self.symbol_dictionary = {}
        self.kind_dictionary = {}

    def define(self, name: str, type: str, kind: KindTypes):
        index = self.kind_dictionary.get(kind, -1)
        index += 1
        lex_object = LexObject(name, type, kind, index)
        self.symbol_dictionary.update({name: lex_object})
        self.kind_dictionary[kind] = index

    def var_count(self, kind: KindTypes) -> int:
        return self.kind_dictionary[kind]

    def kind_of(self, name: str) -> KindTypes:
        return self.symbol_dictionary[name].kind

    def type_of(self, name: str) -> str:
        if name in self.symbol_dictionary:
            return self.symbol_dictionary[name].type
        return None

    def index_of(self, name: str) -> int:
        return self.symbol_dictionary[name].index


class LexObject:
    def __init__(self, name: str, type: str, kind: KindTypes, index: int):
        self.name = name
        self.type = type
        self.kind = kind
        self.index = index
