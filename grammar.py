import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''program : statement_list'''
    print("O programa foi identificado")


def p_variavel(t):
    'variavel : VARIAVEL'
    t[0] = t[1]


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
    if p[1] not in variaveis:
        print(f"Erro: Variável '{p[1]}' não foi declarada.")
    else:
        tipo_variavel = variaveis[p[1]]
        tipo_valor = type(p[3]).__name__
        if (tipo_variavel == 'inteiro' and not isinstance(p[3], int)) or \
        (tipo_variavel == 'real' and not isinstance(p[3], float)) or \
        (tipo_variavel == 'texto' and not isinstance(p[3], str)):
            print(f"Erro: Atribuição incompatível para '{p[1]}'. Tipo esperado: {tipo_variavel}, tipo recebido: {tipo_valor}.")
        else:
            print(f"Atribuição válida: {p[1]} = {p[3]} ({tipo_valor})")


def p_expression_arit(p):
    '''expression : expression OP_SOMA expression
                  | expression OP_SUB expression
                  | expression OP_MULT expression
                  | expression OP_DIV expression'''
    p[0] = f"({p[1]} {p[2]} {p[3]})"
    print(f"Expressão aritmética identificada: {p[0]}")


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
    '''statement : SE LPAREN expression RPAREN LBRACE statement RBRACE SENAO LBRACE statement RBRACE
                 | SE LPAREN expression RPAREN LBRACE statement RBRACE'''
    print("Condição SE/SENAO identificada.")


def p_statement_enquanto(p):
    '''statement : ENQUANTO LPAREN expression RPAREN LBRACE statement RBRACE'''
    print("Loop ENQUANTO identificado.")


def p_statement_para(p):
    '''statement : PARA LPAREN expression OP_PONTO_VIRGULA expression OP_PONTO_VIRGULA expression RPAREN LBRACE statement RBRACE'''
    print("Loop PARA identificado.")


def p_statement_imprimir(p):
    '''statement : IMPRIMIR LPAREN literal RPAREN'''
    print ("Impressão: "+str(p[3]))


def p_statement_leia(p):
    '''statement : LEIA variavel'''
    print(f"Lendo valor para variável {p[2]}")
    p[2].value = input()


def p_error(p):
    if p:
        print(f"Erro de sintaxe: token inesperado '{p.value}', encontrado na linha {p.lineno}")
        parser.errok()
    else:
        print("Sintaxe erro :/")


parser = yacc.yacc()