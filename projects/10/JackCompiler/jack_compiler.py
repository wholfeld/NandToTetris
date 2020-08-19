class JackCompiler:

    def __init__(self, parser, file_name):
        self.indentation = 0
        self.file = open(f'{file_name}', 'w')
        self.parser = parser
        token = self.parser.get_token()
        while self.parser.has_more_commands():
            token = self.parser.get_token()
            if token[1] == 'class':
                self.compile_class()
            self.parser.advance()

    # Compiles a complete class
    def compile_class(self):
        self.write('<class>')
        self.indentation += 1
        token = ''
        keyword = self.parser.get_token()[1]

        # check for class var dec
        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            if keyword == 'static' or keyword == 'field':
                self.compile_class_var_dec()
            elif keyword == 'method':
                break
            else:
                print(token)
                self.write(token[2])
                self.parser.advance()

        while self.parser.has_more_commands():
            token = self.parser.get_token()
            if keyword == 'method':
                self.compile_subroutine()
            else:
                self.write(token[2])
                self.parser.advance()

        self.indentation -= 1
        self.write('</class>')

    # Compiles a static declaration or field declaration.
    def compile_class_var_dec(self):
        self.write('<classVarDec>')
        self.indentation += 1
        token = ''
        keyword = self.parser.get_token()[1]
        break_words = {'function', 'method', '}'}

        # check for class var dec
        while self.parser.has_more_commands():
            token = self.parser.get_token()
            keyword = token[1]
            if keyword in break_words:
                break
            else:
                print(token)
                self.write(token[2])
                self.parser.advance()

        self.indentation -= 1
        self.write('</classVarDec>')

    # Compiles a complete method, function, or constructor.
    def compile_subroutine(self):
        self.parser.advance()
        return ''

    # Compiles a (possibly empty) parameter list, not including the enclosing "()".
    def compile_parameter_list(self):
        return ''

    # Compiles a var declaration.
    def compile_var_dec(self):
        return ''

    # Compiles a sequence of statements, not including the enclosing "{}".
    def compile_statements(self):
        return ''

    # Compiles a do statement.
    def compile_do(self):
        return ''

    # Compiles a let statement.
    def compile_let(self):
        return ''

    # Compiles a while statement.
    def compile_while(self):
        return ''

    # Compiles a return.
    def compile_return(self):
        return ''

    # Compiles an if statement, possibly with a trailing else clause.
    def compile_if(self):
        return ''

    # Compiles an expression.
    def compile_expression(self):
        return ''

    # Compiles a term. This routine is faced with a slight difficulty when traing to decide between some of the alternative parsing rules.
    def compile_term(self):
        return ''

    # Compiles a (possibly empty) comma-seperated list of expressions.
    def compile_expression_list(self):
        return ''

    def write(self, str_to_write):
        #self.file.write('\t' * self.indentation + str_to_write + '\n')
        # str_to_wrtie = '\t' * self.indentation + str_to_write + '\n'
        # print(str_to_write)
        self.file.write('\t' * self.indentation + str_to_write + '\n')
