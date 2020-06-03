import unittest
from context import vm_parser


class TestVmParser(unittest.TestCase):

    def test_remove_whitespace(self):
        self.assertEqual(vm_parser.remove_whitespace('//comments'), '')
        self.assertEqual(vm_parser.remove_whitespace(
            'push constant 7//comments'), 'push constant 7')
        self.assertEqual(vm_parser.remove_whitespace(
            'push constant 7      //comments'), 'push constant 7')


if __name__ == "__main__":
    unittest.main()
