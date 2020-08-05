from enum import Enum, auto


class command_types(Enum):
    C_ARITHMETIC = auto()
    C_PUSH = auto()
    C_POP = auto()
    C_LABEL = auto()
    C_GOTO = auto()
    C_IF = auto()
    C_FUNCTION = auto()
    C_RETURN = auto()
    C_CALL = auto()


vm_command = {
    'add': command_types.C_ARITHMETIC,
    'sub': command_types.C_ARITHMETIC,
    'eq': command_types.C_ARITHMETIC,
    'gt': command_types.C_ARITHMETIC,
    'lt': command_types.C_ARITHMETIC,
    'and': command_types.C_ARITHMETIC,
    'or': command_types.C_ARITHMETIC,
    'not': command_types.C_ARITHMETIC,
    'neg': command_types.C_ARITHMETIC,
    'push': command_types.C_PUSH,
    'pop': command_types.C_POP,
}

math_commands = {
    'add': '+',
    'sub': '-',
    'eq': 'JEQ',
    'gt': 'JGT',
    'lt': 'JLT',
    'and': '&',
    'or': '|',
    'not': '!',
    'neg': '-',
}

two_operands = ('add', 'sub', 'and', 'or')

comparative = ('lt', 'eq', 'gt')

symbols_dict = {
    'SP': '0',
    'LCL': '1',
    'ARG': '2',
    'THIS': '3',
    'THAT': '4',
    'R0': '0',
    'R1': '1',
    'R2': '2',
    'R3': '3',
    'R4': '4',
    'R5': '5',
    'R6': '6',
    'R7': '7',
    'R8': '8',
    'R9': '9',
    'R9': '9',
    'R10': '10',
    'R11': '11',
    'R12': '12',
    'R13': '13',
    'R14': '14',
    'R15': '15',
    'SCREEN': '16384',
    'KBD': '24576',
    'STATIC': '16'
}

location_table = {
    'local': 'LCL',
    'this': 'THIS',
    'that': 'THAT',
    'argument': 'ARG',
    'temp': '5',
    'static': '16'
}
