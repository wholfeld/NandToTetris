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
    'neg': command_types.C_ARITHMETIC,
    'eq': command_types.C_ARITHMETIC,
    'gt': command_types.C_ARITHMETIC,
    'lt': command_types.C_ARITHMETIC,
    'and': command_types.C_ARITHMETIC,
    'or': command_types.C_ARITHMETIC,
    'not': command_types.C_ARITHMETIC,
    'push': command_types.C_PUSH,
    'pop': command_types.C_POP,
}
