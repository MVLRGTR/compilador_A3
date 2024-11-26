# Regra para expressão (simplificada)
def p_expressao(p):
    '''
    expressao : VARIAVEL
              | NUMERO
              | expressao OP_SOMA expressao
              | expressao OP_SUB expressao
              | expressao OP_MULT expressao
              | expressao OP_DIV expressao
    '''
    pass

# Bloco de comandos
def p_bloco(p):
    '''
    bloco : declaracao
          | declaracao bloco
    '''
    pass

# Regra para a declaração de variáveis
def p_declaracao(p):
    '''
    declaracao : tipo VARIAVEL OP_IGUAL expressao OP_PONTO_VIRGULA
    '''
    pass

# Tipos de variáveis
def p_tipo(p):
    '''
    tipo : INTEIRO
         | REAL
         | TEXTO
    '''
    pass

# Adicionando as regras que utilizam os tokens não utilizados

def p_enquanto(p):
    '''
    enquanto : ENQUANTO LPAREN expressao RPAREN LBRACE bloco RBRACE
    '''
    pass

def p_imprimir(p):
    '''
    imprimir : IMPRIMIR LPAREN expressao RPAREN
    '''
    pass

def p_leia(p):
    '''
    leia : LEIA LPAREN VARIAVEL RPAREN
    '''
    pass

def p_para(p):
    '''
    para : PARA VARIAVEL OP_IGUAL NUMERO OP_TO NUMERO LBRACE bloco RBRACE
    '''
    pass

def p_se(p):
    '''
    se : SE LPAREN expressao RPAREN LBRACE bloco RBRACE
    '''
    pass

def p_senao(p):
    '''
    senao : SENAO LBRACE bloco RBRACE
    '''
    pass

def p_senaose(p):
    '''
    senaose : SENAOSE LPAREN expressao RPAREN LBRACE bloco RBRACE
    '''
    pass

def p_texto_normal(p):
    '''
    texto_normal : TEXTONORMAL
    '''
    pass

from codegen import gerar_codigo

# Suponha que 'ast' seja a árvore de sintaxe gerada
ast = ...  # Gerada pelo parser

codigo_python = gerar_codigo(ast)

# Salve ou execute o código Python gerado
with open('saida.py', 'w') as f:
    f.write(codigo_python)

# testeeeeeeeeee