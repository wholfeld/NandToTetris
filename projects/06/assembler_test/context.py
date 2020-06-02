import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../assembler')))

import symbol_table
import assembly_parser
import binary_generator

# print(symbol_table.instructions_dict)

# print(sys.path)