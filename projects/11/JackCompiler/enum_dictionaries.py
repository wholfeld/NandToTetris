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
