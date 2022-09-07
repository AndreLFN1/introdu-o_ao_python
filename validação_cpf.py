'''
Nesse link é explicado como se valida um CPF:
https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
Ele também diz que CPF's com números repetidos (111.111.111-11) também são
validáveis.
A ideia aqui é criar um programa verificador de CPF's e depois tentar gerar
um outro programa que gere CPF's aleatórios que passem no teste.
'''
def valida_cpf(lista_cpf):

    #contadores para a função while
    soma = 0
    i = 0
    n = 10
    #o while tem como objetivo fazer o produto e a soma dos digitos do CPF
    #é etapa para verificação do primeiro digito
    while i < 9:
        num = lista_cpf[i]*n
        i += 1
        n -= 1
        soma = soma + num

        #o resto dessa equação valida o primeiro digito do CPF caso ele seja igual
        #a esse resto
    num_validação = (soma*10)%11
    #print(f'O primeiro numero de validação é: {num_validação}')
    if num_validação == 10:
        num_validação = 0


    if num_validação == lista_cpf[9]:

        soma = 0
        i = 0
        n = 11

        while i < 10:
            num = lista_cpf[i]*n
            i += 1
            n -= 1
            soma = soma + num

        num_validação = (soma*10)%11
        #print(f'O segundo número de validação é: {num_validação}')
        if num_validação == 10:
            num_validação = 0
        if num_validação == lista_cpf[10]:
            print('Este é um CPF válido!')
            print(lista_cpf)
            condição = 1
        else:
            condição = 0

        return condição
'''
Vamos agora gerar CPF's
'''


import random

condição = 0
contador = 1
while condição != 1:
    random_cpf = []

    for x in range(11):

        random_num = random.randint(0,9)
        random_cpf.append(random_num)
    valida_cpf(random_cpf)
    print(condição)
    contador += 1
    #if condição == 1:
    #    break  ''''''''''''''''''''''''''''''''''''''

print(f'O numero de tentativas foi:  + {contador}')
print(f'O CPF válido gerado foi:  + {random_cpf}')
