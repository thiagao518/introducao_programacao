# Programa para conversão de temperatura e Psi
 # Ao abrir o programa o usuário deve escolher qual opção ele deseja usar, colocando o valor que deseja que seja convertido.

#*Opção 1- o programa converte ºC para Kelvin

#*Opção 2- o programa converte ºC Fahrenheit

#*Opção 3- o programa converte Psi para Bar

#*Opção 4- o programa é encerrado

   


import model
opcao = 0

print('Digite uma das opções abaixo para começar') 
print('digite 8 para opção ajuda')
print('Digite opção 1 para ºC para Kelvin,')
print('Digite opção 2 para ºC Fahrenheit, ')
print('Digite opção 3 para Psi em Bar, ')
print('Digite opção 4 para sair do programa, ')

while opcao !='4':
    opcao =input('Digite sua escolha: ')

    if opcao =='1':
    
        model.codigo1()
    elif opcao =='2':
       
        model.codigo2()
    elif opcao =='3':
       
        model.codigo3()
    elif opcao =='4':
        print('O programa esta sendo encerrado até a próxima.')
    elif opcao =='8':
        model.codigo8()

    else:
        print('Opção inválida tente novamente')
