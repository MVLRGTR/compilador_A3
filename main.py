import tkinter as tk
from tkinter import messagebox
from lexer import lexer
from grammar import parser
import re

# Função para traduzir o código para Python
def traduzir_para_python(codigo):
    substituicoes = {
        "se": "if",
        "senao": "else",
        "enquanto": "while",
        "para": "for",
        "inteiro": "",
        "real": "",
        "texto": "",
        "imprimir": "print",
        "leia": "input",
    }
    
    linhas = codigo.splitlines()
    codigo_python = []
    indentacao = 0

    for linha in linhas:
        # Remover espaços extras no início e no final
        linha = linha.strip()

        # Ignorar linhas em branco
        if not linha:
            continue
        
        # Ajustar indentação para fechamento de blocos
        if re.search(r'\}', linha):
            indentacao -= 1
        
        # Adicionar a indentação atual
        linha_python = '    ' * indentacao + linha
        
        # Substituir palavras reservadas usando regex
        for chave, valor in substituicoes.items():
            padrao = r'\b' + re.escape(chave) + r'\b'
            linha_python = re.sub(padrao, valor, linha_python)
        
        # Substituir abertura de bloco `{` por `:`
        linha_python = re.sub(r'\{\s*$', ':', linha_python)
        
        # Remover fechamento de bloco `}`
        linha_python = re.sub(r'\}', '', linha_python)
        
        # Adicionar a linha processada ao código Python
        codigo_python.append(linha_python)

        # Ajustar indentação para abertura de blocos
        if re.search(r':\s*$', linha_python):
            indentacao += 1

    return '\n'.join(codigo_python)




# Função para formatar os tokens em um formato mais simples
def formatar_tokens(tokens, variaveis_declaradas):
    token_formatado = "\n\n\n\n-------------------   ANALISADOR LÉXICO   ---------------------\n"
    token_formatado += "--------------------   TABELA DE SIMBOLOS   ------------------\n"
    token_formatado += "-" * 79 + "\n"
    
    for token in tokens:
        # Verificar se o token é uma variável
        if token.type == "VARIAVEL" and token.value in variaveis_declaradas:
            tipo_variavel = variaveis_declaradas[token.value]
            token_formatado += f"TIPO: VARIAVEL | NOME: {token.value:<8} | TIPO: {tipo_variavel:<8} | LINHA: {token.lineno}\n"
        else:
            token_formatado += f"TIPO: {token.type:<8} | NOME: {token.value:<8} | LINHA: {token.lineno}\n"
        token_formatado += "-" * 79 + "\n"
    
    return token_formatado

# Função para verificar erros de tipo
def verificar_erro_de_tipo(codigo):
    erros = []
    variaveis_declaradas = {}

    for linha in codigo.splitlines():
        palavras = linha.split()

        # Verificar declaração de variáveis
        if len(palavras) >= 2 and palavras[0] in ["inteiro", "real", "texto"]:
            tipo = palavras[0]
            nome_variavel = palavras[1]

            # Se a variável já foi declarada, verificar o tipo
            if nome_variavel in variaveis_declaradas:
                tipo_antigo = variaveis_declaradas[nome_variavel]
                if tipo_antigo != tipo:  # Verifica se o tipo é diferente
                    erros.append(f"Erro: variável '{nome_variavel}' já declarada como '{tipo_antigo}' e não pode ser redeclarada como '{tipo}'.")
            
            # Armazenar a variável e seu tipo corretamente no dicionário
            variaveis_declaradas[nome_variavel] = tipo
            
            # Se houver atribuição na mesma linha
            if len(palavras) > 3 and palavras[2] == "=":
                valor = palavras[3].strip(" ;")  # Retira ponto e vírgula, se houver

                # Verificar se a atribuição é compatível com o tipo
                if valor in variaveis_declaradas:  # Caso seja outra variável
                    tipo_valor = variaveis_declaradas.get(valor)
                    if tipo_valor != tipo:
                        erros.append(f"Erro: variável '{valor}' é do tipo '{tipo_valor}' e não pode ser atribuída à variável '{nome_variavel}' do tipo '{tipo}'.")
                else:
                    # Verificação de valores literais
                    if tipo == "inteiro":
                        try:
                            int(valor)  # Tenta converter o valor para inteiro
                        except ValueError:
                            erros.append(f"Erro: valor '{valor}' incompatível com tipo 'inteiro' para a variável '{nome_variavel}'.")
                    elif tipo == "real":
                        # Verificar se o valor contém ponto (parte decimal)
                        if '.' in valor:
                            try:
                                float(valor)  # Tenta converter o valor para real
                            except ValueError:
                                erros.append(f"Erro: valor '{valor}' incompatível com tipo 'real' para a variável '{nome_variavel}'.")
                        else:
                            erros.append(f"Erro: valor '{valor}' incompatível com tipo 'real' (deve ser decimal) para a variável '{nome_variavel}'.")
                    elif tipo == "texto":
                        if not (valor.startswith('"') and valor.endswith('"')):  # Verifica se é uma string entre aspas
                            erros.append(f"Erro: valor '{valor}' incompatível com tipo 'texto' para a variável '{nome_variavel}'.")
        
        # Verificar atribuições para variáveis já declaradas
        elif "=" in palavras:
            nome_variavel = palavras[0]
            if nome_variavel not in variaveis_declaradas:
                erros.append(f"Erro: variável '{nome_variavel}' não declarada.")
            else:
                tipo_variavel = variaveis_declaradas[nome_variavel]
                valor = palavras[2].strip(" ;")  # Valor atribuído
                
                # Verificar se o valor atribuído é compatível com o tipo da variável
                if valor in variaveis_declaradas:  # Caso seja outra variável
                    tipo_valor = variaveis_declaradas.get(valor)
                    if tipo_valor != tipo_variavel:
                        erros.append(f"Erro: variável '{valor}' é do tipo '{tipo_valor}' e não pode ser atribuída à variável '{nome_variavel}' do tipo '{tipo_variavel}'.")
                else:
                    if tipo_variavel == "inteiro":
                        try:
                            int(valor)
                        except ValueError:
                            erros.append(f"Erro: valor '{valor}' incompatível com tipo 'inteiro' para a variável '{nome_variavel}'.")
                    elif tipo_variavel == "real":
                        if '.' in valor:
                            try:
                                float(valor)
                            except ValueError:
                                erros.append(f"Erro: valor '{valor}' incompatível com tipo 'real' para a variável '{nome_variavel}'.")
                        else:
                            erros.append(f"Erro: valor '{valor}' incompatível com tipo 'real' (deve ser decimal) para a variável '{nome_variavel}'.")
                    elif tipo_variavel == "texto":
                        if not (valor.startswith('"') and valor.endswith('"')): 
                            erros.append(f"Erro: valor '{valor}' incompatível com tipo 'texto' para a variável '{nome_variavel}'.")
    
    if erros:
        return "\n".join(erros), variaveis_declaradas
    return None, variaveis_declaradas


# Função para compilar o código escrito
def compilar_codigo():
    print("A compilação foi iniciada!")
    codigo = entrada_texto.get("1.0", "end-1c")
    
    try:
        saida_texto.delete("1.0", "end-1c")
        
        erro_tipo, variaveis_declaradas = verificar_erro_de_tipo(codigo)
        if erro_tipo:
            messagebox.showerror("Erro de Tipo", erro_tipo)
            return
        
        lexer.input(codigo)
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(tok)
        
        try:
            parser.parse(codigo)
        except Exception as e:
            messagebox.showerror("Erro de Sintaxe", f"Erro de sintaxe: {str(e)}")
            return

        codigo_python = traduzir_para_python(codigo)
        
        saida_texto.insert("1.0", "Código traduzido para Python:\n")
        saida_texto.insert("2.0", codigo_python + "\n\n")
        saida_texto.insert("end", formatar_tokens(tokens, variaveis_declaradas))
        
    except Exception as e:
        messagebox.showerror("Erro na Compilação", f"Ocorreu um erro durante a compilação: {str(e)}")

# Função para limpar os campos de entrada e saída
def limpar_campos():
    entrada_texto.delete("1.0", "end-1c")
    saida_texto.delete("1.0", "end-1c")

# Criando a interface gráfica
root = tk.Tk()
root.title("Compilador Portugol para Python")
root.geometry("750x750")
root.config(bg="#f0f0f0")

entrada_label = tk.Label(root, text="Entrada - Portugol", font=("Arial", 16, "bold"), bg="#f0f0f0", anchor="w")
entrada_label.pack(pady=10, padx=20, fill=tk.X)

entrada_texto = tk.Text(root, height=15, width=80, font=("Arial", 12), bg="#e0e0e0", wrap="word", bd=2, relief="sunken")
entrada_texto.pack(pady=10, padx=20, fill=tk.BOTH)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

botao_compilar = tk.Button(button_frame, text="Compilar", bg="green", fg="white", font=("Arial", 16), width=20, height=2, command=compilar_codigo)
botao_compilar.pack(side=tk.LEFT, padx=20)

botao_limpar = tk.Button(button_frame, text="Limpar", bg="red", fg="white", font=("Arial", 16), width=20, height=2, command=limpar_campos)
botao_limpar.pack(side=tk.LEFT, padx=20)

saida_label = tk.Label(root, text="Saída - Python", font=("Arial", 16, "bold"), bg="#f0f0f0", anchor="w")
saida_label.pack(pady=10, padx=20, fill=tk.X)

saida_texto = tk.Text(root, height=20, width=80, font=("Arial", 12), bg="#e0e0e0", wrap="word", bd=2, relief="sunken")
saida_texto.pack(pady=10, padx=20, fill=tk.BOTH)

root.mainloop()
