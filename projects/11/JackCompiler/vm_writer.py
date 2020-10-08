from enum_dictionaries import arithmetic_set, arithmetic_dictionary


class VMWriter:

    def __init__(self, file_name, class_name):
        self.file = open(f'{file_name}', 'w')
        self.class_name = class_name.split('.')[0]
        self.if_count = 0
        self.while_count = 0
        self.show_comment = False
        self.tokens_index = 0
        self.function_tokens = []
        self. symbol_builder = None

    def write_push(self, segment: str, index: int):
        if segment == 'field':
            segment = 'this'
        elif segment == 'this':
            segment = 'pointer'
        elif segment == 'var':
            segment = 'local'
        self.file.write(f'push {segment} {str(index)}\n')

    def write_pop(self, segment: str, index: int):
        if segment == 'field':
            segment = 'this'
        elif segment == 'var':
            segment = 'local'
        self.file.write(f'pop {segment} {str(index)}\n')

    def write_arithmetic(self, command, previous_value=False):
        arithmetic_symbol = arithmetic_dictionary.get(command)
        if command == '-' and previous_value:
            arithmetic_symbol = 'sub'
        self.tokens_index += 1
        token = self._get_current_token()
        if token == '(':
            self._process_parameters()
        if token != '(':
            self._push_var_name(token)
        self.file.write(f'{arithmetic_symbol}\n')

    def write_label(self, label):
        self.file.write(f'label {label}')

    def write_goto(self, label):
        self.file.write(f'goto {label}')

    def write_if(self):
        self.tokens_index += 1
        self._process_parameters()
        self.file.write(f'if-goto IF_TRUE{self.if_count}\n')
        self.file.write(f'goto IF_FALSE{self.if_count}\n')
        self.file.write(f'label IF_TRUE{self.if_count}\n')
        self._process_function_tokens()
        self.tokens_index += 1
        token = self._get_current_token()
        if token == 'else':
            self.file.write(f'goto IF_END{self.if_count}\n')
            self.file.write(f'label IF_FALSE{self.if_count}\n')
            self._process_function_tokens()
            self.file.write(f'label IF_END{self.if_count}\n')
        else:
            self.file.write(f'label IF_FALSE{self.if_count}\n')
            self._process_function_tokens()
        self.tokens_index += 1
        self.if_count += 1

    def write_while(self):
        self.tokens_index += 1
        self.file.write(f'label WHILE_EXP{self.while_count}\n')
        self._process_parameters()
        self.file.write(f'not\n')
        self.file.write(f'if-goto WHILE_END{self.while_count}\n')
        self._process_function_tokens()
        self.file.write(f'goto WHILE_EXP{self.while_count}\n')
        self.file.write(f'label WHILE_END{self.while_count}\n')
        self.tokens_index += 1
        self.while_count += 1

    def write_call(self, name: str, n_args: int):
        self.file.write(f'call {name} {n_args}\n')

    def write_function(self, symbol_builder, function_tokens, function_type: str, function_name: str, n_locals: int):
        self.function_tokens = function_tokens
        self.symbol_builder = symbol_builder
        self.tokens_index = 0
        local_count = symbol_builder.get_locals_count()
        if function_type == 'constructor':
            class_fields_count = symbol_builder.get_field_count()
            self.write_comments(f'// writing construction {function_name}')
            self.file.write(f'''function {self.class_name}.{function_name} {local_count}\n''')
            self.file.write(f'''push constant {class_fields_count}
call Memory alloc 1
pop pointer 0
''')
        elif function_type == 'method':
            self.write_comments(f'\n// writing method {function_name}')
            self.file.write(f'''function {self.class_name}.{function_name} {local_count}\n''')
            self.file.write(f'''push argument 0
pop pointer 0
''')
        else:
            self.write_comments(f'\n// writing method {function_name}')
            self.file.write(f'''function {self.class_name}.{function_name} {local_count}\n''')

        self._process_function_tokens()

    def _process_function_tokens(self):
        skip_line = False
        while self.tokens_index < len(self.function_tokens):
            token = self._get_current_token()
            if skip_line:
                if token == ';':
                    self.tokens_index += 1
                    skip_line = False
                else:
                    self.tokens_index += 1
            elif token == 'var':
                skip_line = True
                self.tokens_index += 1
            elif token == 'let':
                self._write_let()
            elif token == 'return':
                self.write_return()
            elif token == 'if':
                self.write_if()
            elif token == 'while':
                self.write_while()
            elif token == 'do':
                self.tokens_index += 1
                self._process_expression()
                self.file.write(f'pop temp 0\n')
            elif token == '}':
                break
            else:
                self.tokens_index += 1

    def _call_function(self):
        token = self._get_current_token()
        call_name = ''
        while token != '(':
            call_name = call_name + token
            self.tokens_index += 1
            token = self._get_current_token()
        parameter_count = self._process_parameters()
        self.write_call(call_name, parameter_count)

    def _process_parameters(self):
        self.tokens_index += 1
        token = self._get_current_token()
        if token == ')':
            return 0
        closing_count = 1
        parameter_count = 1
        while closing_count > 0:
            token = self._get_current_token()
            if token == ')':
                closing_count -= 1
                continue
            elif token == '(':
                closing_count += 1
                self.tokens_index += 1
                self._process_parameters()
            elif token == ',':
                parameter_count += 1
            else:
                self._process_expression()
                token = self._get_current_token()
                continue
            self.tokens_index += 1
        return parameter_count

    def _process_expression(self):
        token = self._get_current_token()
        previous_value = False
        while token != ';':
            if token == 'startAddress':
                print('hi')
            if token.isnumeric():
                self.file.write(f'push constant {token}\n')
            elif self.symbol_builder.is_var(token):
                print(token)
                # self.tokens_index += 1
                next_token = self.function_tokens[self.tokens_index + 1][1]
                var_id = self._get_id_array(token)
                if next_token == '.' or next_token == '(':
                    self._call_function()
                    break
                # elif next_token == ',' or next_token == ')':
                #     self.write_push(var_id[2], var_id[3])
                # Is a var array
                elif next_token == '[':
                    # TODO
                    array_index_token = self.function_tokens[self.tokens_index + 2][1]
                    self.tokens_index += 3
                else:
                    self.write_push(var_id[2], var_id[3])
            elif token in ['false', 'true', 'null']:
                self.file.write(f'push constant 0\n')
                if token == 'true':
                    self.file.write(f'not\n')
            elif token == '(':
                self._process_parameters()
            elif token == ')' or token == ',':
                break
            elif token in arithmetic_set:
                self.write_arithmetic(token, previous_value)
            else:
                self._call_function()
                break
            self.tokens_index += 1
            previous_value = True
            token = self._get_current_token()

    def _get_current_token(self):
        return self.function_tokens[self.tokens_index][1]

    def write_return(self):
        self.write_comments(f'// writing return')
        self.tokens_index += 1
        token = self._get_current_token()
        if token != ';':
            self._process_expression()
        else:
            self.file.write(f'push constant 0\n')

        self.file.write(f'return\n')

    # def _write_expression(self):
    #     token = self._get_current_token()
    #     while token != ';':
    #         if token in arithmetic_set:
    #             self.write_arithmetic()
    #         else:
    #             self._push_var_name(token)
    #         self.tokens_index += 1
    #         token = self._get_current_token()

    def close(self):
        self.file.close()

    def write_comments(self, comment_str):
        if self.show_comment:
            self.file.write(f'{comment_str}\n')

    def _push_var_name(self, var_name):
        if var_name == 'this':
            self.write_push('pointer', '0')
        elif var_name.isnumeric():
            self.write_push('constant', var_name)
        else:
            var_id = self._get_id_array(var_name)
            self.write_push(var_id[2], var_id[3])

    def _pop_var_name(self, var_name):
        var_id = self._get_id_array(var_name)
        self.write_pop(var_id[2], var_id[3])

    def _get_id_array(self, var_name):
        var_id = self.symbol_builder._get_identifier(var_name)
        var_split = var_id.split(',')
        return [x.strip() for x in var_split]

    def _write_let(self):
        self.tokens_index += 1
        var_name = self._get_current_token()
        self.tokens_index += 1
        self.tokens_index += 1
        self._process_expression()
        self._pop_var_name(var_name)
        # while self.tokens_index < len(self.function_tokens):
        #     symbol = self._get_current_token()
        #     if symbol == ';':
        #         break
        #     elif symbol == '=':
        #         self.tokens_index += 1
        #         self._write_expression()
        #         break
        #     self.tokens_index += 1
