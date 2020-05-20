import unittest
import assemblyParser
import symbolTable


class TestAssemblyParser(unittest.TestCase):

    def test_command(self):
        self.assertEqual(assemblyParser.commandType('@5'), symbolTable.commands.A_COMMAND)
        self.assertEqual(assemblyParser.commandType('(hi)'), symbolTable.commands.L_COMMAND)
        self.assertEqual(assemblyParser.commandType('D=D+A;JGT'), symbolTable.commands.C_COMMAND)

    def test_symbol(self):
        self.assertEqual(assemblyParser.symbol('@2'), '2')
        self.assertEqual(assemblyParser.symbol('(hi)'), 'hi')
        self.assertEqual(assemblyParser.symbol('@symbol'), 'symbol')

    def test_get_command(self):
        self.assertEqual(assemblyParser.getCommandPart('D=A+1;JMP'), symbolTable.commands.A_COMMAND)

    # def test_dest(self):
    #     self.assertEqual(assemblyParser.)

    # def test_address(self):
    #     self.assertEqual(Assembler.get_address('@2'), '0000000000000010')
    #     self.assertEqual(Assembler.get_address('@3'), '0000000000000011')
    #     self.assertEqual(Assembler.get_address('@0'), '0000000000000000')

    # def test_instruction(self):
    #     self.assertEqual(Assembler.get_instruction('D=A', '='), '1110110000010000')
    #     self.assertEqual(Assembler.get_instruction('D=D+A', '='), '1110000010010000')
    #     self.assertEqual(Assembler.get_instruction('M=D', '='), '1110001100001000')
    #     self.assertEqual(Assembler.get_instruction('D;JGT', ';'), '1110001100000001')
    #     self.assertEqual(Assembler.get_instruction('D;JGT', ';'), '1110001100000001')

    # def test_destination(self):
    #     self.assertEqual(Assembler.get_destination(''), '000')
    #     self.assertEqual(Assembler.get_destination('AMD'), '111')
    #     self.assertEqual(Assembler.get_destination('A'), '100')

    # def test_jump(self):
    #     self.assertEqual(Assembler.get_jump(''), '000')
    #     self.assertEqual(Assembler.get_jump('JGT'), '001')
    #     self.assertEqual(Assembler.get_jump('JMP'), '111')
    #     self.assertEqual(Assembler.get_jump('JLE'), '110')

    # def test_goto(self):
    #     self.assertEqual(Assembler.add_goto('(TEST)'), 'TEST')

if __name__ == "__main__":
    unittest.main()
