from enum_dictionaries import arithmetic_set


class VMWriter:

    def __init__(self, file_name, class_name):
        self.file = open(f'{file_name}', 'w')
        self.class_name = class_name.split('.')[0]
        self.if_count = 0
        self.show_comment = False
        self.tokens_index = 0
        self.function_tokens = []
        self. symbol_builder = None

    def write_push(self, segment: str, index: int):
        new_seg = segment
        if segment == 'field':
            new_seg = 'this'
        if segment == 'this':
            new_seg = 'pointer'
        self.file.write(f'\npush {new_seg} {str(index)}')

    def write_pop(self, segment: str, index: int):
        if segment == 'field':
            segment = 'this'
        self.file.write(f'pop {segment} {str(index)}')

    def write_arithmetic(self, command):
        arithmetic_symbol = command
        self.tokens_index += 1
        token = self._get_current_token()
        self._push_var_name(token)
        self.file.write(f'{arithmetic_symbol}')

    def write_label(self, label):
        self.file.write(f'label {label}')

    def write_goto(self, label):
        self.file.write(f'goto {label}')

    def write_if(self, label):
        self.file.write(f'''if-goto ''')
        self.if_count += 1

    def write_call(self, name: str, n_args: int):
        self.file.write(f'call {name} {n_args}')

    def write_function(self, symbol_builder, function_tokens, function_type: str, function_name: str, n_locals: int):
        self.function_tokens = function_tokens
        self. symbol_builder = symbol_builder
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
        while self.tokens_index < len(self.function_tokens):
            token = self._get_current_token()
            if token == 'let':
                self._write_let()
            elif token == 'return':
                self.write_return()
            else:
                self.tokens_index += 1

    def _get_current_token(self):
        return self.function_tokens[self.tokens_index][1]

    def write_return(self):
        self.write_comments(f'\n// writing return')
        self.tokens_index += 1
        token = self._get_current_token()
        if token != ';':
            self._write_expression()

        self.file.write(f'\nreturn')

    def _write_expression(self):
        token = self._get_current_token()
        while token != ';':
            if token in arithmetic_set:
                self.write_arithmetic()
            else:
                self._push_var_name(token)
            self.tokens_index += 1
            token = self._get_current_token()

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
            var_id = self.symbol_builder._get_identifier(var_name)
            var_split = var_id.split(',')
            var_split = [x.strip() for x in var_split]
            self.write_push(var_split[2], var_split[3])

    def _write_let(self):
        self.tokens_index += 1
        var_name = self.function_tokens[self.tokens_index][1]
        while self.tokens_index < len(self.function_tokens):
            symbol = self.function_tokens[self.tokens_index][1]
            if symbol == ';':
                break
            elif symbol == '=':
                self._write_equals()
                break
            self.tokens_index += 1
        self._push_var_name(var_name)

    def _write_equals(self):
        pass
