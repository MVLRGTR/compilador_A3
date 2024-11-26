import ply.yacc as yacc
from lexer import tokens

# def p_program(p):
#     '''program : PROGRAM statement_list END_PROGRAM'''
#     print("Programa reconhecido")

def p_literal(t):
    '''literal : NUMERO
               | VARIAVEL
               | TEXTONORMAL'''
    t[0]=t[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_define_tipo(p):
    '''statement : INTEIRO VARIAVEL OP_PONTO_VIRGULA
                 | REAL VARIAVEL OP_PONTO_VIRGULA
                 | TEXTO VARIAVEL OP_PONTO_VIRGULA'''
    print(f"Declaração de variável: nome - {p[2]} | tipo - {p[1]} ")

def p_statement_atribuicao(p):
    '''statement : VARIAVEL OP_IGUAL expression OP_PONTO_VIRGULA'''
    print(f"Atribuição {p[1]} = {p[3]}")

def p_expression_arit(p):
    '''expression : expression OP_MAIS expression
                  | expression OP_MENOS expression
                  | expression OP_MULT expression
                  | expression OP_DIV expression'''
    pass

def p_expression_rel(p):
    '''expression : expression MAIOR expression
                  | expression MENOR expression
                  | expression MAIORIGUAL expression
                  | expression MENORIGUAL expression
                  | expression OP_IGUALDADE expression
                  | expression OP_DIFERENTE expression'''
    pass

def p_expression(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_var(p):
    '''expression : NUMERO
                  | VARIAVEL'''
    p[0] = p[1]

def p_statement_se(p):
    '''statement : SE LPAREN expression RPAREN statement SENAO statement
                 | SE LPAREN expression RPAREN statement'''
    print("Condição SE/SENAO identificada.")

def p_statement_enquanto(p):
    '''statement : ENQUANTO LPAREN expression RPAREN statement'''
    print("Laço ENQUANTO identificado.")

def p_statement_para(p):
    '''statement : PARA LPAREN expression RPAREN statement'''
    print("Laço ENQUANTO identificado.")

def p_statement_imprimir(p):
    '''imprimir_statement : IMPRIMIR LPAREN literal RPAREN'''
    print ("Impressão: "+str(p[3]))

def p_statement_leia(p):
    '''leia_statement : LEIA variavel'''
    print(f"Lendo valor para variável {p[2]}")
    p[2].value = input()

def p_error(p):
    if p:
        print(f"Erro de sintaxe {p.type}, encontrando na linha {p.lineno}")
        parser.errok()
    else:
        print("Sintaxe erro :/")


parser = yacc.yacc()