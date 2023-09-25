import re

def analisador_lexico(entrada):

    if entrada[-3:] != 'bab':
        return False

    entrada = entrada[:-3]

    #modulo re
    if re.match('^[ab]*$', entrada):
        return True
    else:
        return False

entrada1 = "ababbab"
entrada2 = "ababcbab"
entrada3 = "abbaab"
entrada4 = "abab"

print(analisador_lexico(entrada1))
print(analisador_lexico(entrada2))
print(analisador_lexico(entrada3))
print(analisador_lexico(entrada4))
