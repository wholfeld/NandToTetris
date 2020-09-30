class VMWriter:

    def __init__(self, file_name, class_name):
        self.file = open(f'{file_name}', 'w')
        self.class_name = class_name
        self.if_count = 0
        self.show_comment = True

    def write_push(self, segment: str, index: int):
        self.file.write(f'push {segment} {str(index)}')

    def write_pop(self, segment: str, index: int):
        self.file.write(f'pop {segment} {str(index)}')

    def write_arithmetic(self, command):
        self.file.write(f'{command}')

    def write_label(self, label):
        self.file.write(f'label {label}')

    def write_goto(self, label):
        self.file.write(f'goto {label}')

    def write_if(self, label):
        self.file.write(f'''if-goto ''')
        self.if_count += 1

    def write_call(self, name: str, n_args: int):
        self.file.write(f'call {name} {n_args}')

    def write_function(self, function_type: str, function_name: str, n_locals: int):
        if function_type == 'constructor':
            self.write_comments(f'// writing construction {function_name}')
            self.file.write(f'''function {self.class_name}.{function_name}\n''')
            self.file.write(f'''push constant {n_locals}
call Memory alloc 1
pop pointer 0
''')
        elif function_type == 'method':
            self.write_comments(f'// writing method {function_name}')
            self.file.write(f'''function {self.class_name}.{function_name}\n''')
            self.file.write(f'''push argument 0
pop pointer 0
''')
        else:
            self.write_comments(f'// writing method {function_name}')
            self.file.write(f'''function {self.class_name}.{function_name}\n''')

    def write_return(self):
        self.write_comments(f'// writing return')
        self.file.write(f'return/n')

    def close(self):
        self.file.close()
    
    def write_comments(self, comment_str):
        if self.show_comment:
            self.file.write(f'{comment_str}\n')
