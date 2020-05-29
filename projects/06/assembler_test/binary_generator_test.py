import unittest
from context import binary_generator


class TestBinaryGenerator(unittest.TestCase):

    def test_address(self):
        self.assertEqual(binary_generator.get_address('@2'), '0000000000000010')
        self.assertEqual(binary_generator.get_address('@3'), '0000000000000011')
        self.assertEqual(binary_generator.get_address('@0'), '0000000000000000')

    def test_instruction(self):
        self.assertEqual(binary_generator.get_instruction_binary('D=A'), '1110110000010000')
        self.assertEqual(binary_generator.get_instruction_binary('D=D+A'), '1110000010010000')
        self.assertEqual(binary_generator.get_instruction_binary('M=D'), '1110001100001000')
        self.assertEqual(binary_generator.get_instruction_binary('D;JGT'), '1110001100000001')
        self.assertEqual(binary_generator.get_instruction_binary('D=D+A;JGT'), '1110000010010001')

    def test_get_computation(self):
        self.assertEqual(binary_generator.get_computation('D=A'), '0110000')
        self.assertEqual(binary_generator.get_computation('D=M'), '1110000')
        self.assertEqual(binary_generator.get_computation('0;JMP'), '0101010')
        self.assertEqual(binary_generator.get_computation('ADM=D+M;JMP'), '1000010')

    def test_get_jump(self):
        self.assertEqual(binary_generator.get_jump('D=D+A;JGT'), '001')
        self.assertEqual(binary_generator.get_jump('D;JMP'), '111')
        self.assertEqual(binary_generator.get_jump('D=D+A'), '000')

    def test_get_destination(self):
        self.assertEqual(binary_generator.get_destination('0;JMP'), '000')
        self.assertEqual(binary_generator.get_destination('D=D+A;JGT'), '010')
        self.assertEqual(binary_generator.get_destination('ADM=A'), '111')
        self.assertEqual(binary_generator.get_destination('A=D'), '100')


if __name__ == "__main__":
    unittest.main()
