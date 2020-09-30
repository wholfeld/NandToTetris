from symbol_table import SymbolTable


class SymbolBuilder():
    def __init__(self):
        self.current_identifier = ''
        self.class_table = None
        self.function_table = SymbolTable()
        self.class_name = ''
        self.identifier_kind = None
        self.function_args = False
        self.identifier_type = ''
        self.kind_types = frozenset([
            'field',
            'static',
            'var',
            'class',
            'function',
            'constructor',
            'method'
        ])
        self.function_types = frozenset([
            'constructor',
            'method',
            'function'
        ])

    def get_class_table(self):
        return self.class_table

    def get_function_table(self):
        return self.function_table

    def get_xml(self, symbol_type: str, symbol_name: str):
        b_type = self.identifier_kind
        if symbol_name in self.kind_types:
            self.identifier_kind = symbol_name
            if self.identifier_kind == 'class':
                self.class_table = SymbolTable()
            # new function reset function table
            elif self.identifier_kind in self.function_types:
                self.function_table.start_subroutine()
                if self.identifier_kind == 'method':
                    self.function_table.define('this', self.class_name, 'argument')
        if b_type:
            if b_type in self.function_types:
                self._building_function(symbol_name)
            elif b_type == 'class':
                self.class_name = symbol_name
                self.identifier_kind = None
            else:
                self._build_variables(symbol_name)
        table_info = self._get_identifier(symbol_name)
        return f'<{symbol_type}> {symbol_name} </{symbol_type}{table_info}>'

    def _get_identifier(self, symbol_name: str):
        id_string = ''
        if bool(self.function_table.type_of(symbol_name)):
            id_string = f''' {symbol_name}, {self.function_table.type_of(symbol_name)}\
, {self.function_table.kind_of(symbol_name)}, {self.function_table.index_of(symbol_name)}'''
        elif bool(self.class_table.type_of(symbol_name)):
            id_string = f''' {symbol_name}, {self.class_table.type_of(symbol_name)}\
, {self.class_table.kind_of(symbol_name)}, {self.class_table.index_of(symbol_name)}'''
        # return (type, index) or None
        return id_string

    def _building_function(self, symbol_name: str):
        if symbol_name == 'int':
            print('stop')
        # if arguments are finished
        if symbol_name == ')':
            self.identifier_kind = None
            self.function_args = False
            return
        # if arguments starting
        if symbol_name == '(':
            self.function_args = True
            self.identifier_type = None
            return
        # add arguemtns to function table
        if self.identifier_type:
            self.function_table.define(symbol_name, self.identifier_type, 'argument')
            self.identifier_type = None
        elif self.function_args and not bool(self.identifier_type):
            self.identifier_type = symbol_name
        if symbol_name == ',':
            self.identifier_type = None

    def _build_variables(self, symbol_name: str):
        if symbol_name == (';'):
            self.identifier_type = None
            self.identifier_kind = None
        elif not self.identifier_kind:
            self.identifier_kind = symbol_name
        elif not self.identifier_type:
            self.identifier_type = symbol_name
        elif symbol_name != ',':
            if self.identifier_kind == 'var':
                self.function_table.define(symbol_name, self.identifier_type, self.identifier_kind)
            else:
                self.class_table.define(symbol_name, self.identifier_type, self.identifier_kind)
