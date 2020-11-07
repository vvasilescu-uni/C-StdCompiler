from ast_nodes import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

def p_program(p):
    'program : declaration_list'
    p[0] = Program(p[1])

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    if len(p) == 3: p[0] = p[1] + [p[2]]
    else: p[0] = [p[1]]

def p_declaration(p):
    '''declaration : var_declaration
                   | fun_declaration'''
    p[0] = p[1]

def p_var_declaration(p):
    '''var_declaration : type_specifier ID SEMI
                       | type_specifier ID LBRACKET NUM RBRACKET SEMI'''
    if len(p) == 4: p[0] = VariableDeclaration(p[1], p[2])
    else: p[0] = VariableDeclaration(p[1], p[2], p[4])

def p_type_specifier(p):
    '''type_specifier : INT
                      | VOID'''
    p[0] = p[1]

def p_fun_declaration(p):
    'fun_declaration : type_specifier ID LPAREN params RPAREN compound_stmt'
    p[0] = FunctionDeclaration(p[1], p[2], p[4], p[6])

def p_params(p):
    '''params : param_list
              | VOID'''
    p[0] = p[1]

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param'''
    if len(p) == 4: p[0] = p[1] + [p[3]]
    else: p[0] = [p[1]]

def p_param(p):
    '''param : type_specifier ID
             | type_specifier ID LBRACKET RBRACKET'''
    if len(p) == 3: p[0] = FunctionParameter(p[1], p[2], False)
    else: p[0] = FunctionParameter(p[1], p[2], True)

def p_compound_stmt(p):
    'compound_stmt : LBRACE local_declarations statement_list RBRACE'
    p[0] = CompoundStatement(p[2], p[3])

def p_local_declarations(p):
    '''local_declarations : local_declarations var_declaration
                          | empty'''
    if len(p) == 3: p[0] = p[1] + [p[2]]
    else: p[0] = []

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 3: p[0] = p[1] + [p[2]]
    else: p[0] = []

def p_statement(p):
    '''statement : expression_stmt
                 | compound_stmt
                 | selection_stmt
                 | iteration_stmt
                 | return_stmt'''
    p[0] = p[1]

def p_expression_stmt(p):
    '''expression_stmt : expression SEMI
                       | SEMI'''
    if len(p) == 3: p[0] = p[1]

def p_selection_stmt(p):
    '''selection_stmt : IF LPAREN expression RPAREN statement
                      | IF LPAREN expression RPAREN statement ELSE statement'''
    if len(p) == 6: p[0] = SelectionStatement(p[3], p[5])
    else: p[0] = SelectionStatement(p[3], p[5], p[7])

def p_iteration_stmt(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'
    p[0] = IterationStatement(p[3], p[5])

def p_return_stmt(p):
    '''return_stmt : RETURN SEMI
                   | RETURN expression SEMI'''
    if len(p) == 3: p[0] = ReturnStatement(None)
    else: p[0] = ReturnStatement(p[2])

def p_expression(p):
    '''expression : var ASIGN expression
                  | relational_operation
                  | binary_operation'''
    if len(p) == 4:
        if type(p[1]) is tuple: p[0] = VariableAsignation(p[1][0], p[1][1], p[3])
        else: p[0] = VariableAsignation(p[1], 0, p[3])
    else: p[0] = p[1]

def p_var(p):
    '''var : ID
           | ID LBRACKET expression RBRACKET'''
    if len(p) == 2: p[0] = p[1]
    else: p[0] = (p[1], p[3])

def p_relational_operation(p):
    '''relational_operation : binary_operation LT binary_operation
                            | binary_operation LE binary_operation
                            | binary_operation GT binary_operation
                            | binary_operation GE binary_operation
                            | binary_operation EQ binary_operation
                            | binary_operation NE binary_operation'''
    p[0] = RelationalOperation(p[1], p[2], p[3])

def p_binary_operation(p):
    '''binary_operation : binary_operation PLUS term
                        | binary_operation MINUS term
                        | binary_operation TIMES term
                        | binary_operation DIVIDE term'''
    p[0] = BinaryOperation(p[1], p[2], p[3])

def p_binary_operation_term(p):
    'binary_operation : term'
    p[0] = p[1]

def p_term(p):
    '''term : LPAREN expression RPAREN
            | var
            | call
            | NUM'''
    if len(p) == 4: p[0] = p[2]
    else: p[0] = p[1]

def p_call(p):
    'call : ID LPAREN args RPAREN'
    p[0] = FunctionCall(p[1], p[3])

def p_args(p):
    '''args : arg_list
            | empty'''
    p[0] = p[1]

def p_arg_list(p):
    '''arg_list : arg_list COMMA expression
                | expression'''
    if len(p) == 4: p[0] = p[1] + [p[3]]
    else: p[0] = [p[1]]

def p_empty(p):
    'empty : '
    pass

def p_error(p):
    print('Syntax error at line {}'.format(p.lineno))
