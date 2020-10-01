from symbol_builders import SymbolBuilder
from vm_writer import VMWriter


class JackCompiler:

    def __init__(self, parser, file_name):
        self.indentation = 0
        print(file_name)
        self.file = open(f'{file_name}', 'w')
        self.parser = parser
        self.building_expression_list = False
        self.symbol_builder = SymbolBuilder()
        self.function_tokens = []
        token = self.parser.get_token()
        vm_file_name = str(file_name).replace('.xml', 'T.vm')
        vm_class_name = str(str(file_name).split('/')[-1])
        self.vm_writer = VMWriter(vm_file_name, vm_class_name)
        while self.parser.has_more_commands():
            token = self.parser.get_token()
            if token[1] == 'class':
                self.compile_class()
            self.parser.advance()

    # Compiles a complete class
    def compile_class(self):
        self.write('<class>')
        self.indentation += 1
        class_var = {'static', 'field'}
        function_types = {'constructor', 'method', 'function'}
        # check for class var dec
        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            if keyword in class_var:
                self.compile_class_var_dec()
            elif keyword in function_types:
                break
            else:
                self.write_advance()

        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            if keyword in function_types:
                self.compile_subroutine()
            else:
                self.write_advance()

        self.indentation -= 1
        self.vm_writer.close()
        self.write('</class>')

    # Compiles a static declaration or field declaration.
    def compile_class_var_dec(self):
        self.write('<classVarDec>')
        self.indentation += 1
        break_words = {'function', 'method', '}'}

        # check for class var dec
        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            if keyword in break_words:
                break
            elif keyword == ';':
                self.write_advance()
                break
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</classVarDec>')

    # Compiles a complete method, function, or constructor.
    def compile_subroutine(self):
        self.write('<subroutineDec>')
        self.indentation += 1
        word_counter = 0
        function_type = None
        function_name = None

        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            if word_counter == 0:
                function_type = keyword
            if word_counter == 2:
                function_name = keyword
                # self.vm_writer.write_function(function_type, function_name, 2)
            word_counter += 1

            if keyword == '(':
                self.compile_parameter_list()
            elif keyword == '{':
                self.compile_subroutine_body(function_type, function_name)
                break
            elif keyword == '}':
                break
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</subroutineDec>')

    def compile_subroutine_body(self, function_type, function_name):
        self.write('<subroutineBody>')
        self.indentation += 1
        break_words = {'}'}
        self.function_tokens = []

        statements_starter = {'let', 'do', 'if', 'while'}

        # check for class var dec
        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            if keyword in break_words:
                self.write_advance()
                break
            elif keyword == 'var':
                self.compile_var_dec()
            elif keyword in statements_starter:
                self.compile_statements()
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</subroutineBody>')
        self.vm_writer.write_function(self.symbol_builder, self.function_tokens, function_type, function_name, 2)

    # Compiles a (possibly empty) parameter list, not including the enclosing "()".
    def compile_parameter_list(self):
        self.write_advance()
        self.write('<parameterList>')
        self.indentation += 1

        # check for class var dec
        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            if keyword == ')':
                break
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</parameterList>')

    # Compiles a var declaration.
    def compile_var_dec(self):
        self.write('<varDec>')
        self.indentation += 1
        while self.parser.has_more_commands():
            keyword = self.parser.get_token()[1]
            if keyword == '=':
                self.compile_expression()
            elif keyword == ';':
                self.write_advance()
                break
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</varDec>')

    # Compiles a sequence of statements, not including the enclosing "{}".
    def compile_statements(self):
        self.write('<statements>')
        self.indentation += 1
        while self.parser.has_more_commands():
            keyword = self.parser.get_token()[1]
            if keyword == 'if':
                self.compile_if()
            elif keyword == 'let':
                self.compile_let()
            elif keyword == 'do':
                self.compile_do()
            elif keyword == 'while':
                self.compile_while()
            elif keyword == 'return':
                self.compile_return()
            elif keyword == '}':
                break
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</statements>')

    # Compiles a do statement.
    def compile_do(self):
        self.write('<doStatement>')
        self.indentation += 1

        while self.parser.has_more_commands():
            keyword = self.parser.get_token()[1]
            if keyword == '(':
                self.write_advance()
                self.compile_expression_list()
            elif keyword == ';':
                self.write_advance()
                break
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</doStatement>')

    # Compiles a let statement.
    def compile_let(self):
        self.write('<letStatement>')
        self.indentation += 1

        while self.parser.has_more_commands():
            keyword = self.parser.get_token()[1]
            if keyword == '=':
                self.write_advance()
                self.compile_expression()
            elif keyword == ';':
                self.write_advance()
                break
            elif keyword == '[':
                self.write_advance()
                self.compile_expression()
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</letStatement>')

    # Compiles a while statement.
    def compile_while(self):
        self.write('<whileStatement>')
        self.indentation += 1

        while self.parser.has_more_commands():
            keyword = self.parser.get_token()[1]
            if keyword == '(':
                self.write_advance()
                self.compile_expression()
            elif keyword == '{':
                self.write_advance()
                self.compile_statements()
            elif keyword == '}':
                self.write_advance()
                break
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</whileStatement>')

    # Compiles a return.
    def compile_return(self):
        self.write('<returnStatement>')
        self.indentation += 1

        while self.parser.has_more_commands():
            keyword = self.parser.get_token()[1]
            if keyword == ';':
                self.write_advance()
                break
            elif keyword != 'return':
                self.compile_expression()
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</returnStatement>')

    # Compiles an if statement, possibly with a trailing else clause.
    def compile_if(self):
        self.write('<ifStatement>')
        self.indentation += 1

        while self.parser.has_more_commands():
            keyword = self.parser.get_token()[1]
            if keyword == '(':
                self.write_advance()
                self.compile_expression()
            elif keyword == '}':
                self.write_advance()
                keyword = self.parser.get_token()[1]
                if keyword != 'else':
                    break
            elif keyword == '{':
                self.write_advance()
                self.compile_statements()
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</ifStatement>')

    # Compiles an expression.
    def compile_expression(self):
        self.write('<expression>')
        self.indentation += 1
        term_types = {'stringConstant', 'identifier', 'integerConstant'}
        term_keywords = {'this', 'that', 'false', 'true', 'null', '(', '-', '~', '^'}
        has_seen_term = False
        # term_operands = {'-', '~', '^'}
        break_keywords = {')', ';', ']', ','}

        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            token_type = token[0]
            if keyword in break_keywords:
                break
            elif has_seen_term and keyword == '-':
                self.write_advance()
                has_seen_term = False
            elif token_type in term_types or keyword in term_keywords:
                self.compile_term()
                has_seen_term = True
            elif keyword == '[':
                self.write_advance()
                self.compile_expression()
            else:
                self.write_advance()

        self.indentation -= 1
        self.write('</expression>')

    def compile_term(self):
        self.write('<term>')
        self.indentation += 1
        writing_call = False
        expression_set = {'(', '['}
        unary_set = {'-', '~'}
        continue_set = {'.', '('}

        while self.parser.has_more_commands():
            token = self.parser.get_token()
            token_type = token[0]
            keyword = token[1]
            if keyword in expression_set:
                self.write_advance()
                if writing_call:
                    self.compile_expression_list()
                else:
                    self.compile_expression()
            elif keyword in unary_set:
                self.write_advance()
                self.compile_term()
                break
            elif keyword == '.':
                self.write_advance()
            elif token_type == 'identifier':
                self.write_advance()
                keyword = self.parser.get_token()[1]
                if keyword in continue_set:
                    writing_call = True
                elif keyword == '[':
                    continue
                else:
                    break
            else:
                self.write_advance()
                break

        self.indentation -= 1
        self.write('</term>')

    # Compiles a (possibly empty) comma-seperated list of expressions.
    def compile_expression_list(self):
        self.write('<expressionList>')
        self.indentation += 1

        while self.parser.has_more_commands():
            keyword = self.parser.get_token()[1]
            if keyword == ')':
                break
            elif keyword == ',':
                self.write_advance()
            else:
                self.compile_expression()

        self.indentation -= 1
        self.write('</expressionList>')

    def write_advance(self):
        # line = self.parser.get_token()[2]
        token = self.parser.get_token()
        self.function_tokens.append(token)
        s_type = token[0]
        s_name = token[1]
        line = self.symbol_builder.get_xml(s_type, s_name)
        self.write(line)
        self.parser.advance()

    def write(self, str_to_write):
        # self.file.write('\t' * self.indentation + str_to_write + '\n')
        # str_to_wrtie = '\t' * self.indentation + str_to_write + '\n'
        # print(str_to_write)
        self.file.write('  ' * self.indentation + str_to_write + '\n')
