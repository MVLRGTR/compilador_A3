import ply.yacc as yacc
from lexer import tokens

# Definição de precedência das operações
precedence = (
    ('left', 'OP_SOMA', 'OP_SUB'),
    ('left', 'OP_MULT', 'OP_DIV'),
)

# Variável global para armazenar as variáveis declaradas e seus tipos
variaveis = {}

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
    t[0] = t[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_define_tipo(p):
    '''statement : INTEIRO VARIAVEL
                 | REAL VARIAVEL
                 | TEXTO VARIAVEL'''
    # Verifica se a variável já foi declarada
    if p[2] in variaveis:
        print(f"Erro: Variável '{p[2]}' já foi declarada anteriormente.")
    else:
        tipo = 'inteiro' if p[1] == 'inteiro' else 'real' if p[1] == 'real' else 'texto' if p[1] == 'texto' else 'desconhecido'
        variaveis[p[2]] = tipo
        print(f"Declaração de variável: nome - {p[2]} | tipo - {tipo}")

def p_define_tipo_com_atribuicao(p):
    '''statement : INTEIRO VARIAVEL OP_IGUAL expression
                 | REAL VARIAVEL OP_IGUAL expression
                 | TEXTO VARIAVEL OP_IGUAL expression'''
    # Verifica se a variável já foi declarada
    if p[2] in variaveis:
        print(f"Erro: Variável '{p[2]}' já foi declarada anteriormente.")
    else:
        tipo = 'inteiro' if p[1] == 'inteiro' else 'real' if p[1] == 'real' else 'texto' if p[1] == 'texto' else 'desconhecido'
        valor = p[4]

        # Determinando o tipo do valor atribuído
        if isinstance(valor, int):
            tipo_valor = 'inteiro'
        elif isinstance(valor, float):
            tipo_valor = 'real'
        elif isinstance(valor, str):
            tipo_valor = 'texto'
        else:
            tipo_valor = 'desconhecido'

        # Verificação de compatibilidade de tipos
        if tipo == 'inteiro' and tipo_valor != 'inteiro':
            print(f"Erro: Atribuição incompatível para '{p[2]}'. Tipo esperado: inteiro, tipo recebido: {tipo_valor}.")
        elif tipo == 'real' and tipo_valor != 'real':
            print(f"Erro: Atribuição incompatível para '{p[2]}'. Tipo esperado: real, tipo recebido: {tipo_valor}.")
        elif tipo == 'texto' and tipo_valor != 'texto':
            print(f"Erro: Atribuição incompatível para '{p[2]}'. Tipo esperado: texto, tipo recebido: {tipo_valor}.")
        else:
            variaveis[p[2]] = tipo
            print(f"Declaração e atribuição: nome - {p[2]} | tipo - {tipo} | valor - {valor}")


def p_statement_atribuicao(p):
    '''statement : VARIAVEL OP_IGUAL expression'''
    
    if p[1] not in variaveis:
        # Verifica se a variável foi declarada
        print(f"Erro: Variável '{p[1]}' não foi declarada.")
    else:
        tipo_variavel = variaveis[p[1]]
        valor = p[3]
        
        if isinstance(valor, int):  # Se for um número inteiro
            tipo_valor = 'inteiro'
        elif isinstance(valor, float):  # Se for um número real
            tipo_valor = 'real'
        elif isinstance(valor, str):  # Se for uma string
            tipo_valor = 'texto'
        else:
            tipo_valor = 'desconhecido'

        # Verificação do tipo da variável e tipo do valor
        if tipo_variavel == 'inteiro' and tipo_valor != 'inteiro':
            print(f"Erro: Atribuição incompatível para '{p[1]}'. Tipo esperado: inteiro, tipo recebido: {tipo_valor}.")
        elif tipo_variavel == 'real' and tipo_valor != 'real':
            print(f"Erro: Atribuição incompatível para '{p[1]}'. Tipo esperado: real, tipo recebido: {tipo_valor}.")
        elif tipo_variavel == 'texto' and tipo_valor != 'texto':
            print(f"Erro: Atribuição incompatível para '{p[1]}'. Tipo esperado: texto, tipo recebido: {tipo_valor}.")
        else:
            print(f"Atribuição válida: {p[1]} = {valor} ({tipo_valor})")

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
    
    if isinstance(p[1], str):
        if p[1].isdigit():
            p[0] = int(p[1])
        elif p[1] in variaveis:
            p[0] = p[1]
        else:
            print(f"Erro: Variável '{p[1]}' não foi declarada.")
            p[0] = None
    else:
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
    print("Impressão: " + str(p[3]))

def p_statement_leia(p):
    '''statement : LEIA variavel'''
    
    if p[2] not in variaveis:
        print(f"Erro: Variável '{p[2]}' não foi declarada.")
    else:
        print(f"Lendo valor para variável {p[2]}")
        p[2].value = input()

def p_error(p):
    if p:
        print(f"Erro de sintaxe: token inesperado '{p.value}', encontrado na linha {p.lineno}")
        parser.errok()
    else:
        print("Erro de sintaxe: fim inesperado.")

parser = yacc.yacc()
