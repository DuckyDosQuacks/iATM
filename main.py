# Importar Bilbiotecas
from os import system

# Inciar Variaveis
saldo_conta = 0.00
montante_levantar = None

# Funções
def MenuPrincipal():
    system('cls')
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('[1] Levantar')
    print('[2] Depositar')
    print('[3] Ver Saldo')
    print('[0] Sair')
    print('-=-=-=-=-=-=-=-=-=-=-=')

def MenuLevantar():
    system('cls')
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('[1] 10€')
    print('[2] 20€')
    print('[3] 60€')
    print('[4] 100€')
    print('[5] 150€')
    print('-=-=-=-=-=-=-=-=-=-=-=')

def OperacaoLevantar():
    menu_levantar_option = int(input('Utilizador > '))
        
    global saldo_conta
    global montante_levantar

    match menu_levantar_option:
        case 1:
            montante_levantar = 10.00
        case 2:
            montante_levantar = 20.00
        case 3:
            montante_levantar = 60.00
        case 4:
            montante_levantar = 100.00
        case 5:
            montante_levantar = 150.00

    if saldo_conta >= montante_levantar:
        print('-=-=-=-=-=-=-=-=-=-=-=')
        print(f'\033[32m[SUCESSO] Levantou {montante_levantar:.2f}€!\033[m')
        print('-=-=-=-=-=-=-=-=-=-=-=')
        input('Pressione ENTER para continuar...')

        saldo_conta -= montante_levantar
    else:
        print('-=-=-=-=-=-=-=-=-=-=-=')
        print('\033[31m[ERRO] Saldo Insuficiente! \033[m')
        print('-=-=-=-=-=-=-=-=-=-=-=')
        input('Pressione ENTER para continuar...')

def MenuMostrarSaldo():
    system('cls')
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print(f'\033[36mSaldo: {saldo_conta:.2f}€\033[m')
    print('-=-=-=-=-=-=-=-=-=-=-=')
    input('Pressione ENTER para continuar...')

def MenuDepositar():
    system('cls')

    global saldo_conta

    print('-=-=-=-=-=-=-=-=-=-=-=')
    montante_depositar = float(input('Montante > '))
    print('-=-=-=-=-=-=-=-=-=-=-=')

    saldo_conta += montante_depositar

    print(f'\033[32m[SUCESSO] Depositou {montante_depositar:.2f}€\033[m')
    print('-=-=-=-=-=-=-=-=-=-=-=')
    input('Pressione ENTER para continuar...')

# Ciclo Principal
while True:
    MenuPrincipal()

    main_menu_option = int(input('Utilizador > '))

    # Opção Inválida
    while main_menu_option < 0 or main_menu_option > 3:
        print('\033[31m[ERRO] Opção Inválida!\033[m')

    # Sair 
    if main_menu_option == 0:
        break

    # Levantar Dinheiro
    elif main_menu_option == 1:
        MenuLevantar()
        OperacaoLevantar()

    # Depositar Dinheiro
    elif main_menu_option == 2:
        MenuDepositar()

    # Mostrar Saldo
    elif main_menu_option == 3:
        MenuMostrarSaldo()
