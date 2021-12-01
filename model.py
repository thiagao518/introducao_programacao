

def codigo1():
    c = float(input('informe a temperatura em ºC: '))
    f = ((9 * c) / 5) + 32
    print('A tempretarura de {}ºC corresponde a {}ºF!'.format(c, f))

def codigo2():
    c = float(input('informe a temperatura em ºC: '))
    k = c + 273,15
    print('A temperatura de {}ºC corresponde a {}ºK!'.format(c, k))
def codigo3():
    p = float(input('informe o Psi em Bar: '))
    b =  p / 14,504
    print('A pressão de {}Psi coressponde a {}Bar!'.format(p, b))

def codigo8():
    print('Programa para conversão de temperatura e Psi')
    print('Ao abrir o programa o usuário deve escolher qual opção ele deseja usar, colocando o valor que deseja que seja convertido')

    print('Opção 1- o programa converte ºC para Kelvin')

    print('Opção 2- o programa converte ºC Fahrenheit')

    print('Opção 3- o programa converte Psi para Bar')

    print('Opção 4- o programa é encerrado')

