# Regras para expressões
def p_expressao(p):
    '''
    expressao : VARIAVEL
              | NUMERO
              | expressao OP_SOMA expressao
              | expressao OP_SUB expressao
              | expressao OP_MULT expressao
              | expressao OP_DIV expressao
    '''
    if len(p) == 2:  # VARIAVEL ou NUMERO
        p[0] = p[1]
    elif len(p) == 4:  # Operações binárias (SOMA, SUB, MULT, DIV)
        p[0] = {'tipo': 'operacao', 'operador': p[2], 'esquerda': p[1], 'direita': p[3]}

# Bloco de comandos
def p_bloco(p):
    '''
    bloco : comando
          | comando bloco
    '''
    if len(p) == 2:  # Comando único
        p[0] = [p[1]]
    else:  # Comando seguido de mais blocos
        p[0] = [p[1]] + p[2]

# Regra para a declaração de variáveis
def p_declaracao(p):
    '''
    declaracao : tipo VARIAVEL OP_IGUAL expressao OP_PONTO_VIRGULA
    '''
    p[0] = {'tipo': 'declaracao', 'variavel': p[2], 'valor': p[4]}

# Tipos de variáveis
def p_tipo(p):
    '''
    tipo : INTEIRO
         | REAL
         | TEXTO
    '''
    p[0] = p[1]  # Apenas armazena o tipo

# Regras para estruturas de controle e outros comandos

def p_enquanto(p):
    '''
    enquanto : ENQUANTO LPAREN expressao RPAREN LBRACE bloco RBRACE
    '''
    p[0] = {'tipo': 'enquanto', 'condicao': p[3], 'bloco': p[6]}

def p_imprimir(p):
    '''
    imprimir : IMPRIMIR LPAREN expressao RPAREN
    '''
    p[0] = {'tipo': 'imprimir', 'valor': p[3]}

def p_leia(p):
    '''
    leia : LEIA LPAREN VARIAVEL RPAREN
    '''
    p[0] = {'tipo': 'leia', 'variavel': p[3]}

def p_para(p):
    '''
    para : PARA VARIAVEL OP_IGUAL NUMERO OP_TO NUMERO LBRACE bloco RBRACE
    '''
    p[0] = {'tipo': 'para', 'variavel': p[2], 'inicio': p[4], 'fim': p[6], 'bloco': p[8]}

def p_se(p):
    '''
    se : SE LPAREN expressao RPAREN LBRACE bloco RBRACE
    '''
    p[0] = {'tipo': 'se', 'condicao': p[3], 'bloco': p[6]}

def p_senao(p):
    '''
    senao : SENAO LBRACE bloco RBRACE
    '''
    p[0] = {'tipo': 'senao', 'bloco': p[3]}

def p_senaose(p):
    '''
    senaose : SENAOSE LPAREN expressao RPAREN LBRACE bloco RBRACE
    '''
    p[0] = {'tipo': 'senaose', 'condicao': p[3], 'bloco': p[6]}

def p_fimse(p):
    '''
    fimse : FIMSE
    '''
    pass

def p_fimenquanto(p):
    '''
    fimenquanto : FIMENQUANTO
    '''
    pass

def p_fimpara(p):
    '''
    fimpara : FIMPARA
    '''
    pass

def p_texto_normal(p):
    '''
    texto_normal : TEXTONORMAL
    '''
    p[0] = p[1]  # Apenas armazena o texto normal como string

# Caso de erro
def p_error(p):
    print("Erro de sintaxe:", p)

# Gerar código em Python
from codegen import gerar_codigo

# Suponha que 'ast' seja a árvore de sintaxe gerada
ast = ...  # Gerada pelo parser após a análise do código-fonte

# Gerando o código Python correspondente
codigo_python = gerar_codigo(ast)

# Salvando o código gerado em um arquivo Python
with open('saida.py', 'w') as f:
    f.write(codigo_python)
