import tkinter as tk
from tkinter import messagebox
from lexer import lexer
from grammar import parser
import re

# Função para traduzir o código para Python
def traduzir_para_python(codigo):    
    # Substituições simples de palavras-chave e estruturas
    substituicoes = {
        "se": "if",
        "senao": "else",
        "enquanto": "while",
        "para": "for",
        "inteiro": "int",
        "real": "float",
        "texto": "str",
        "imprimir": "print",
        "leia": "input",
        ";": "",
        "{": "",
        "}": ""
    }
    
    for chave, valor in substituicoes.items():
        # Use \b para garantir que as palavras sejam completas e não partes de outras palavras
        codigo = re.sub(r'\b' + re.escape(chave) + r'\b', valor, codigo)
    
    return codigo

# Função para formatar os tokens em um formato mais simples
def formatar_tokens(tokens):    
    token_formatado = "\n\n\n\n---------------ANALISADOR LÉXICO---------------\n"
    token_formatado += "---------------TABELA DE SIMBOLOS-------------\n"
    token_formatado += "-" * 63 + "\n"
    
    for token in tokens:
        token_formatado += f"TIPO: {token.type:<8} | NOME: {token.value:<8} | LINHA: {token.lineno}\n"
    
    return token_formatado

# Função para compilar o código escrito
def compilar_codigo():
    print("Botão 'Compilar' clicado!")
    codigo = entrada_texto.get("1.0", "end-1c")
    try:
        saida_texto.delete("1.0", "end-1c")
        
        # Realiza a análise léxica
        lexer.input(codigo)
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(tok)
        
        # Realiza a análise sintática
        parser.parse(codigo)
        
        # Traduz para Python
        codigo_python = traduzir_para_python(codigo)
        
        # Exibe os resultados na área de saída
        saida_texto.insert("1.0", "Código traduzido para Python:\n")
        saida_texto.insert("2.0", codigo_python + "\n\n")
        
        # Exibe os tokens de maneira simples
        saida_texto.insert("end", formatar_tokens(tokens))
        
    except Exception as e:
        messagebox.showerror("Erro na Compilação", f"Ocorreu um erro durante a compilação: {str(e)}")

# Função para limpar os campos
def limpar_campos():
    entrada_texto.delete("1.0", "end-1c")
    saida_texto.delete("1.0", "end-1c")

# Criação da interface gráfica
root = tk.Tk()
root.title("Compilador Portugol para Python")
root.geometry("750x750")

# Estilo da interface
root.config(bg="#f0f0f0")

# Layout da Entrada - Portugol
entrada_label = tk.Label(root, text="Entrada - Portugol", font=("Arial", 16, "bold"), bg="#f0f0f0", anchor="w")
entrada_label.pack(pady=10, padx=20, fill=tk.X)

entrada_texto = tk.Text(root, height=15, width=80, font=("Arial", 12), bg="#e0e0e0", wrap="word", bd=2, relief="sunken")
entrada_texto.pack(pady=10, padx=20, fill=tk.BOTH)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# Botão Compilar
botao_compilar = tk.Button(button_frame, text="Compilar", bg="green", fg="white", font=("Arial", 16), width=20, height=2, command=compilar_codigo)
botao_compilar.pack(side=tk.LEFT, padx=20)

# Botão Limpar
botao_limpar = tk.Button(button_frame, text="Limpar", bg="red", fg="white", font=("Arial", 16), width=20, height=2, command=limpar_campos)
botao_limpar.pack(side=tk.LEFT, padx=20)

# Layout da Saída - Python
saida_label = tk.Label(root, text="Saída - Python", font=("Arial", 16, "bold"), bg="#f0f0f0", anchor="w")
saida_label.pack(pady=10, padx=20, fill=tk.X)

saida_texto = tk.Text(root, height=20, width=80, font=("Arial", 12), bg="#e0e0e0", wrap="word", bd=2, relief="sunken")
saida_texto.pack(pady=10, padx=20, fill=tk.BOTH)

root.mainloop()