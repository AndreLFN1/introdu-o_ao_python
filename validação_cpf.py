'''
Nesse link é explicado como se valida um CPF:
https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
Ele também diz que CPF's com números repetidos (111.111.111-11) também são
validáveis.
A ideia aqui é criar um programa verificador de CPF's e depois tentar gerar
um outro programa que gere CPF's aleatórios que passem no teste.
'''
def valida_cpf(cpf):

    #aqui o programa vai avaliar as condições em que o algoritimo falha, mas
    #que também são números inválidos
    if cpf == '11111111111':
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro
    elif cpf == '22222222222':
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro
    elif cpf == '33333333333':
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro
    elif cpf == '44444444444':
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro
    elif cpf == '55555555555':
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro
    elif cpf == '66666666666':
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro
    elif cpf == '99999999999':
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro
    elif cpf == '00000000000':
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro


    #essa lista vai agrupar os numeros do CPF individualmente
    lista_cpf = []

    #aqui vamos adicionar numero a numero do CPF em forma de string, convertê-lo
    #para int e adcionar a lista-cpf
    for x in cpf:
        lista_cpf.append(int(x))

    if len(lista_cpf) != 11:
        mensagem_erro = print('Este CPF é inválido!')
        return mensagem_erro

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
    if num_validação == 10:
        num_validação = 0
    print(f'O primeiro numero de validação é: {num_validação}')


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
        if num_validação == 10:
            num_validação = 0
        print(f'O segundo número de validação é: {num_validação}')
        if num_validação == lista_cpf[10]:
            print('Este é um CPF válido!')
        else:
            print('Este CPF é inválido!')

'''
Pedindo input para o usuario e validando o CPF:
'''


cpf = input('Digite um numero de CPF sem pontos ou traços: ')
valida_cpf(cpf)
