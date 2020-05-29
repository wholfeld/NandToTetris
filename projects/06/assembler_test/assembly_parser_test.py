import unittest
from context import symbol_table
from context import assembly_parser


class TestAssemblyParser(unittest.TestCase):

    def test_test(self):
        pass

    def test_command(self):
        self.assertEqual(assembly_parser.command_type('@5'), symbol_table.CommandType.A_COMMAND)
        self.assertEqual(assembly_parser.command_type('(hi)'), symbol_table.CommandType.L_COMMAND)
        self.assertEqual(assembly_parser.command_type('D=D+A;JGT'), symbol_table.CommandType.C_COMMAND)

    def test_symbol(self):
        self.assertEqual(assembly_parser.symbol('@2'), '2')
        self.assertEqual(assembly_parser.symbol('(hi)'), 'hi')
        self.assertEqual(assembly_parser.symbol('@symbol'), 'symbol')

    def test_get_command(self):
        self.assertEqual(assembly_parser.get_command_part('D=A+1;JMP', symbol_table.CommandPart.JUMP), 'JMP')
        self.assertEqual(assembly_parser.get_command_part('D=A+1;JMP', symbol_table.CommandPart.DEST), 'D')
        self.assertEqual(assembly_parser.get_command_part('D=A+1;JMP', symbol_table.CommandPart.COMP), 'A+1')
        self.assertEqual(assembly_parser.get_command_part('D=A+1', symbol_table.CommandPart.JUMP), '')
        self.assertEqual(assembly_parser.get_command_part('D;JMP', symbol_table.CommandPart.DEST), 'D')
        self.assertEqual(assembly_parser.get_command_part('0;JMP', symbol_table.CommandPart.DEST), '0')
        self.assertEqual(assembly_parser.get_command_part('D;JMP', symbol_table.CommandPart.COMP), '0')

    def test_dest(self):
        self.assertEqual(assembly_parser.dest('0'), '000')
        self.assertEqual(assembly_parser.dest('A'), '100')
        self.assertEqual(assembly_parser.dest('D'), '010')
        self.assertEqual(assembly_parser.dest('M'), '001')
        self.assertEqual(assembly_parser.dest('ADM'), '111')

    def test_comp(self):
        self.assertEqual(assembly_parser.comp('0'), '101010')
        self.assertEqual(assembly_parser.comp('-D'), '001111')
        self.assertEqual(assembly_parser.comp('A+1'), '110111')

    def test_jump(self):
        self.assertEqual(assembly_parser.jump(''), '000')
        self.assertEqual(assembly_parser.jump('JMP'), '111')
        self.assertEqual(assembly_parser.jump('JEQ'), '010')


if __name__ == "__main__":
    unittest.main()
