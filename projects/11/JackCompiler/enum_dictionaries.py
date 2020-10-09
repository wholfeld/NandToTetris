from enum import Enum, auto


class TokenTypes(Enum):
    KEYWORD = auto()
    SYMBOL = auto()
    IDENTIFIER = auto()
    INT_CONST = auto()
    STRING_CONST = auto()

    # My extras.
    NONE_TYPE = auto()
    COMMENT_START = auto()
    COMMENT = auto()


class KindTypes(Enum):
    STATIC = auto()
    FIELD = auto()
    ARGUMENT = auto()
    VAR = auto()
    FUNCTION = auto()
    SUBROUTINE = auto()
    CLASS = auto()


kind_dict = {
    KindTypes.STATIC: 'static',
    KindTypes.FIELD: 'field',
    KindTypes.ARGUMENT: 'argument',
    KindTypes.VAR: 'var',
    KindTypes.FUNCTION: 'function',
    KindTypes.SUBROUTINE: 'subroutine',
    KindTypes.CLASS: 'class'
}

types_dict = {
    TokenTypes.KEYWORD: 'keyword',
    TokenTypes.SYMBOL: 'symbol',
    TokenTypes.IDENTIFIER: 'identifier',
    TokenTypes.INT_CONST: 'integerConstant',
    TokenTypes.STRING_CONST: 'stringConstant'
}

arithmetic_dictionary = {
    '+': 'add',
    # '-':'sub',
    '*': 'call Math.multiply 2',
    '/': 'call Math.divide 2',
    '=': 'eq',
    '&gt;': 'gt',
    '&lt;': 'lt',
    '&amp;': 'and',
    '|': 'or',
    '~': 'not',
    '-': 'neg',
}

vm_type_dictionary = {
    'this': 'pointer 0',
    'that': 'pointer 1',
    'true': 'constant 0',
    'false': 'constant 0',
    'null': 'constant 0',
}

keyword_set = frozenset([
    'class',
    'constructor',
    'function',
    'method',
    'field',
    'static',
    'var',
    'int',
    'char',
    'boolean',
    'void',
    'true',
    'false',
    'null',
    'this',
    'let',
    'do',
    'if',
    'else',
    'while',
    'return'
])

arithmetic_set = frozenset([
    '+',
    '-',
    '~',
    '*',
    '/',
    '&amp;',
    '|',
    '&lt;',
    '&gt;',
    '=',
])

symbol_set = frozenset([
    '{',
    '}',
    '(',
    ')',
    '[',
    ']',
    '.',
    ',',
    ';',
    '+',
    '-',
    '*',
    '/',
    '&',
    '|',
    '<',
    '>',
    '=',
    '~',
])
