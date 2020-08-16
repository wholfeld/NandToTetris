class JackCompiler:

    def JackCompiler(self):
        self.x = 1


# Compiles a complete class
def compile_class():
    return ''


# Compiles a static declaration or field declaration.
def compile_class_var_dec():
    return ''


# Compiles a complete method, function, or constructor.
def compile_subroutine():
    return ''


# Compiles a (possibly empty) parameter list, not including the enclosing "()".
def compile_parameter_list():
    return ''


# Compiles a var declaration.
def compile_var_dec():
    return ''


# Compiles a sequence of statements, not including the enclosing "{}".
def compile_statements():
    return ''


# Compiles a do statement.
def compile_do():
    return ''


# Compiles a let statement.
def compile_let():
    return ''


# Compiles a while statement.
def compile_while():
    return ''


# Compiles a return.
def compile_return():
    return ''


# Compiles an if statement, possibly with a trailing else clause.
def compile_if():
    return ''


# Compiles an expression.
def compile_expression():
    return ''


# Compiles a term. This routine is faced with a slight difficulty when traing to decide between some of the alternative parsing rules.
def compile_term():
    return ''


# Compiles a (possibly empty) comma-seperated list of expressions.
def compile_expression_list():
    return ''
