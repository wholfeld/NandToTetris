import unittest
import assemblyParser
import symbolTable


class TestAssemblyParser(unittest.TestCase):

    def test_command(self):
        self.assertEqual(assemblyParser.commandType('@5'), symbolTable.commands.A_COMMAND)
        self.assertEqual(assemblyParser.commandType('(hi)'), symbolTable.commands.L_COMMAND)
        self.assertEqual(assemblyParser.commandType('D=D+A;JGT'), symbolTable.commands.C_COMMAND)


if __name__ == "__main__":
    unittest.main()
