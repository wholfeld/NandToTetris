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
    'field',
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
