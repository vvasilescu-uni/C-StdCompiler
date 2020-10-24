def p_program(p):
    'program : declaration_list'

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''

def p_declaration(p):
    '''declaration : var_declaration
                   | fun_declaration'''

def p_var_declaration(p):
    '''var_declaration : type_specifier ID SEMI
                       | type_specifier ID LBRACKET NUM RBRACKET SEMI'''

def p_type_specifier(p):
    '''type_specifier : INT
                      | VOID'''

def p_fun_declaration(p):
    'fun_declaration : type_specifier ID LPAREN params RPAREN compound_stmt'

def p_params(p):
    '''params : param_list
              | VOID
              | empty'''

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param'''

def p_param(p):
    '''param : type_specifier ID
             | type_specifier ID LBRACKET RBRACKET'''

def p_compound_stmt(p):
    'compound_stmt : LBRACE local_declarations statement_list RBRACE'

def p_local_declarations(p):
    '''local_declarations : local_declarations var_declaration
                          | empty'''

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''

def p_statement(p):
    '''statement : expression_stmt
                 | compound_stmt
                 | selection_stmt
                 | iteration_stmt
                 | return_stmt'''

def p_expression_stmt(p):
    '''expression_stmt : expression SEMI
                       | SEMI'''

def p_selection_stmt(p):
    '''selection_stmt : IF LPAREN expression RPAREN statement
                      | IF LPAREN expression RPAREN statement ELSE statement'''

def p_iteration_stmt(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'

def p_return_stmt(p):
    '''return_stmt : RETURN SEMI
                   | RETURN expression SEMI'''

def p_expression(p):
    '''expression : var ASIGN expression
                  | simple_expression'''

def p_var(p):
    '''var : ID
           | ID LBRACKET expression RBRACKET'''

def p_simple_expression(p):
    '''simple_expression : additive_expression relop additive_expression
                         | additive_expression'''

def p_relop(p):
    '''relop : LT
             | LE
             | GT
             | GE
             | EQ
             | NE'''

def p_additive_expression(p):
    '''additive_expression : additive_expression addop term
                           | term'''

def p_addop(p):
    '''addop : PLUS
             | MINUS'''

def p_term(p):
    '''term : term mulop factor
            | factor'''

def p_mulop(p):
    '''mulop : TIMES
             | DIVIDE'''

def p_factor(p):
    '''factor : LPAREN expression RPAREN
              | var
              | call
              | NUM'''

def p_call(p):
    'call : ID LPAREN args RPAREN'

def p_args(p):
    '''args : arg_list
            | empty'''

def p_arg_list(p):
    '''arg_list : arg_list COMMA expression
                | expression'''

def p_empty(p):
    'empty : '

def p_error(p):
    print('Syntax error at line {}'.format(p.lineno))