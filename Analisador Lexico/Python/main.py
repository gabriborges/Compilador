
tokens_list = []

numeros= [0,1,2,3,4,5,6,7,8,9]
numeros_char = ['1','2','3','4','5','6','7','8','9','0',]
lista_letras_maiusculas = [chr(i) for i in range(65, 91)]
lista_letras_minusculas = [chr(i) for i in range(97, 123)]
lista_letras = lista_letras_maiusculas + lista_letras_minusculas + numeros_char

class Token:
    def __init__(self, tipo, lexema) -> None:
        self.tipo = tipo
        self.lexema = lexema

    @property
    def get_token(self):
        return f"<{self.tipo}, {self.lexema}>"



def extrair_palavra_reservada(lista):
    for index, char in enumerate(lista):
        if char not in lista_letras_maiusculas:
            return (lista[:index], index)
        
# def extrair_palavra(lista):
#     for index, char in enumerate(lista):
#         if char not in lista_letras:
#             if index == 0:
#                 return (None, index)
#             return (lista[:index], index)
#     # If no valid token is found, return (None, 0)
#     return (None, 0)

def extrair_palavra(lista):
    return extrair_palavra_recursive(lista, 0)

def extrair_palavra_recursive(lista, index):
    if index >= len(lista) or lista[index] not in lista_letras:
        return (None, index)
    
    while index < len(lista) and lista[index] in lista_letras:
        index += 1
    
    return (lista[:index], index)
        
def extrair_numero(lista):
    for index, char in enumerate(lista):
        if char.isdigit() or (char == '.' and lista[:index].count('.') < 1):
            pass
        elif char == '.':
            num, index2 = extrair_numero(lista[:index+1])
            return (lista[:index]+"."+ num, index + index2 + 1)
        else:
            return (lista[:index], index)

def extrair_str(lista):
    for index, char in enumerate(lista):
        if char == '"':
            return (lista[:index], index)



#nao possui tratamento de erros
def ler_caractere(lista: list): 
    if not lista:
        return
    
    elif lista[0] == ' ':
        ler_caractere(lista[1:])

    elif lista[0] in lista_letras_maiusculas:
        if lista[0] == 'E' and lista[1] not in lista_letras_maiusculas:
            palavra, index = extrair_palavra_reservada(lista)
            tokens_list.append(Token("OpBool", palavra).get_token)
            ler_caractere(lista[index:])
        elif  lista[:2] =="OU":
            palavra, index = extrair_palavra_reservada(lista)
            tokens_list.append(Token("OpBool", palavra).get_token)
            ler_caractere(lista[index:])
        else:
            palavra, index = extrair_palavra_reservada(lista)
            tokens_list.append(Token("PR", palavra).get_token)
            ler_caractere(lista[index:])

    elif lista[0] in ['*','/','+','-']:
        if lista[0] == '*':
            tokens_list.append(Token("OpArit", lista[0]).get_token)
            ler_caractere(lista[1:])
        elif lista[0] == '/':
            tokens_list.append(Token("OpArit", lista[0]).get_token)
            ler_caractere(lista[1:])
        elif lista[0] == '+':
            tokens_list.append(Token("OpArit", lista[0]).get_token)
            ler_caractere(lista[1:])
        else: 
            tokens_list.append(Token("OpArit", lista[0]).get_token)
            ler_caractere(lista[1:])

    elif lista[0] in ['<', '>', '=']:
        if lista[:2] == "<=":
            tokens_list.append(Token("OpRel", lista[:2]).get_token)
            ler_caractere(lista[2:])
        elif lista[:2] == ">=":
            tokens_list.append(Token("OpRel", lista[:2]).get_token)
            ler_caractere(lista[2:])
        elif lista[:2] == "<>":
            tokens_list.append(Token("OpRel", lista[:2]).get_token)
            ler_caractere(lista[2:])
        elif lista[0] == "<":
            tokens_list.append(Token("OpRel", lista[0]).get_token)
            ler_caractere(lista[1:])
        elif lista[0] == ">":
            tokens_list.append(Token("OpRel", lista[0]).get_token)
            ler_caractere(lista[1:])
        else:
            tokens_list.append(Token("OpRel", lista[0]).get_token)
            ler_caractere(lista[1:])

    elif lista[0] == ':':
        tokens_list.append(Token("Delim", lista[0]).get_token)
        ler_caractere(lista[1:])

    elif lista[0] == '(' or lista[0] == ')':
        if lista[0] == '(':
            tokens_list.append(Token("AP", lista[0]).get_token)
            ler_caractere(lista[1:])
        else:
            tokens_list.append(Token("FP", lista[0]).get_token)
            ler_caractere(lista[1:])

    elif lista[0] in lista_letras_minusculas:
        palavra, index = extrair_palavra(lista)
        tokens_list.append(Token("Var", palavra).get_token)
        ler_caractere(lista[index:])
        
    elif int(lista[0]) in numeros:
        num, index = extrair_numero(lista)
        if '.' in num:
            tokens_list.append(Token("NumR", num).get_token)
            ler_caractere(lista[index:])
        else:
            tokens_list.append(Token("NumI", num).get_token)
            ler_caractere(lista[index:])
    elif lista[0] == '"':
        palavra, index = extrair_str(lista)
        tokens_list.append(Token("Str", palavra).get_token)
        ler_caractere(lista[index:])


file_contents = ""
with open(r"C:\Users\carva\OneDrive\Documentos\Computacao\6 semestre\Compiladores\Compilador\programa.txt", 'r') as file:
    
    file_contents = file.read()
    file_contents = file_contents.replace('\n', ' ').replace('\r', ' ')

ler_caractere(file_contents)
print(tokens_list)