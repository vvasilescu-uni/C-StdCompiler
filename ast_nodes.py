class Program():
    def __init__(self, declaration_list):
        self.declaration_list = declaration_list


class VariableDeclaration():
    def __init__(self, data_type, name, size=1):
        self.data_type = data_type
        self.name = name
        self.size = size


class FunctionDeclaration():
    def __init__(self, data_type, name, params, body):
        self.data_type = data_type
        self.name = name
        self.params = params
        self.body = body


class FunctionParameter():
    def __init__(self, data_type, name, is_array):
        self.data_type = data_type
        self.name = name
        self.is_array = is_array


class CompoundStatement():
    def __init__(self, local_decl, statements):
        self.local_declarations = local_decl
        self.statements = statements


class SelectionStatement():
    def __init__(self, condition, then, otherwise=None):
        self.condition = condition
        self.then = then
        self.otherwise = otherwise


class IterationStatement():
    def __init__(self, condition, then):
        self.condition = condition
        self.then = then


class ReturnStatement():
    def __init__(self, expression):
        self.expression = expression


class VariableAsignation():
    def __init__(self, var_name, var_index, new_value):
        self.var_name = var_name
        self.var_index = var_index
        self.new_value = new_value


class RelationalOperation():
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class BinaryOperation():
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class FunctionCall():
    def __init__(self, fun_name, args):
        self.fun_name = fun_name
        self.args = args
