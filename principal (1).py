import os
from time import sleep

veiculos = ["GOL","HB20","PEJOUT","CLASSIC","PALIO","MUSTANG"]
clientes = ["JOAO","PEDRO","MARIA","FILIPE","JOSE","CLAUDIA"]
vendas = [20000,45000,35000,40000,37500,99500]
novo_veiculo = ' '
novo_cliente = ' '
novo_venda = ' '
aux_loop_insert = ' '
aux_loop_menu = 'S'
aux_loop_pesquisa = ''
aux_loop_atualizar = ''
pesquisa_cliente = ''
pesquisa_veiculo = ''
pesquisa_valor = 0
aux_loop_remover = ''
remover_cliente =  ''
remover_veiculo =  ''
remover_valor =  0
pos = 0
wait_time = 0
consulta = 0
cont_cliente = 0
cont_veiculo = 0
cont_venda = 0
def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    sleep(wait_time)
    os.system("cls")
while aux_loop_menu == 'S':
    clear_console(1)
    print("""
        #########################################################
        #            SISTEMA DE VENDAS DE VEICULOS              #        
        #                                                       # 
        #      MENU PRINCIPAL:                                  #
        #      1 - INSERIR DADOS:                               #
        #      2 - CONSULTAR DADOS:                             #
        #      3 - REMOVER DADOS:                               #  
        #      4 - ATUALIZAR DADOS:                             #
        #                                                       #
        #                                                       #
        #  CRIADO POR: FILIPE CAJADO E PEDRO HENRIQUE XIBILI    #
        #                                                       #
        #########################################################
    """)

      
    n = int(input('INFORME A OPÇÃO DO MENU A SE FAZER : '))
    
    # INSERIR DADOS DE CLIENTE / VEÍCULOS / VALOR DA VENDA :
    
    if n == 1:
        
        aux_loop_insert = 'S'
        while aux_loop_insert == 'S':
            novo_cliente = input('\nINFORME NO NOME DO CLIENTE: ').upper()
            clientes.append(novo_cliente)
            novo_veiculo = input('INFORME NO NOME DO VEÍCULO VENDIDO: ').upper()
            veiculos.append(novo_veiculo)
            novo_venda = float(input('INFORME O VALOR VENDIDO: R$'))
            vendas.append(novo_venda)
            aux_loop_insert = input('\n----- DESEJA INSERIR UMA NOVA VENDA? S ou N: ').upper()
 
        if aux_loop_insert == 'N':
             aux_loop_menu == 'S'
          
     #  CONSULTAR DADOS DE CLIENTE / VEÍCULOS / VALOR DA VENDA :
    if n == 2:
        aux_loop_pesquisa = 'S'
        while aux_loop_pesquisa == "S":
            

            print("""
            #########################################################
            #                  CONSULTAS                            #
            #      1 - CONSULTA PERSONALIZADA:                      #
            #      2 - CONSULTAR TODOS OS VEICULOS:                 #
            #      3 - CONSULTAR TODOS OS CLIENTES:                 #  
            #      4 - CONSULTAR TODAS AS VENDAS:                   #
            #########################################################
            """)
            consulta = int(input('INFORME O TIPO DE CONSULTA: '))

            if consulta == 1:
                modo = int(input("Modo de Consulta: \n1 - NOME\n2 - CARRO\n3 - VALOR DA VENDA\n\nINFORME O MODO DE CONSULTA PARA REMOÇÃO: "))
                if modo == 1:
                    pesquisa_cliente = input("---- INFORME O NOME:  ").upper()   
                    if pesquisa_cliente in clientes:
                      pos = clientes.index(pesquisa_cliente)
                      print("NOME: {}\nVEICULO: {}\nVALOR: {}\n".format(clientes[pos],veiculos[pos],vendas[pos]))
                    else:
                      print('O cliente informado não existe no sistema.')
                elif modo == 2:
                    pesquisa_veiculo = input("INFORME O MODELO:  ").upper()   
                    if pesquisa_veiculo in veiculos:
                      pos = veiculos.index(pesquisa_veiculo)
                      print("NOME: {}\nVEICULO: {}\nVALOR: {}\n".format(clientes[pos],veiculos[pos],vendas[pos]))
                    else:
                      print('O veículo informado não existe no sistema.')
                elif modo == 3:
                    pesquisa_valor= float(input("INFORME O VALOR:  "))  
                    if pesquisa_valor in vendas:
                      pos = vendas.index(pesquisa_valor)
                      print("NOME: {}\nVEICULO: {}\nVALOR: {}\n".format(clientes[pos],veiculos[pos],vendas[pos]))
                    else:
                      print('O valor informado não pertence a nenhuma venda.')
                aux_loop_pesquisa = input('\nDeseja realizar uma nova consulta? S ou N: ').upper()
            
            elif consulta == 2:
                 cont_veiculo = len(veiculos)
                 print('\nVEÍCULOS')
                 for i in range(0,cont_veiculo):
                    print(f'{i+1} - {veiculos[i]}')
                 aux_loop_pesquisa = input('\nDeseja realizar uma nova consulta? S ou N: ').upper()

            elif consulta == 3:
                 cont_cliente = len(clientes)
                 print('\nCLIENTES')
                 for i in range(0,cont_cliente):
                    print(f'{i+1} - {clientes[i]}')
                 aux_loop_pesquisa = input('\nDeseja realizar uma nova consulta? S ou N: ').upper()
            
            elif consulta == 4:
                 cont_venda = len(vendas)
                 print('\nVENDAS')
                 print('\n  CLIENTES | VEÍCULOS | VALOR DA VENDA ')
                 for i in range(0,cont_venda):
                    print(f'{i+1} - {clientes[i]} - {veiculos[i]} - {vendas[i]}')
                 aux_loop_pesquisa = input('\nDeseja realizar uma nova consulta? S ou N: ').upper()

        if aux_loop_pesquisa == 'N':
             aux_loop_menu == 'S'
                 
     #  REMOVER DADOS DE CLIENTE / VEÍCULOS / VALOR DA VENDA :
    if n == 3:
        aux_loop_remover = 'S'
        while aux_loop_remover == "S":
            print('\nREMOVER REGISTRO PELO: ')
            modo = int(input("1 - NOME\n2 - CARRO\n3 - VALOR DA VENDA\n\nINFORME O MODO DE CONSULTA PARA REMOÇÃO: "))
            if modo == 1:
              remover_cliente = input("INFORME O NOME:  ").upper()
              if remover_cliente in clientes:   
                  print('--------------Cliente Encontrado--------------')
                  remover = input('\nDeseja realmente remover os dados desse cliente? S ou N: ').upper()
                  if remover == 'S':
                    pos = clientes.index(remover_cliente)
                    clientes[pos] = '#'
                    veiculos[pos] = '#'
                    vendas[pos] = '#'
                    print("---DADOS REMOVIDOS COM SUCESSO---")
              else:
                print('O cliente informado não está resgitrado no sistema.')  
            if modo == 2:
              remover_veiculo = input("INFORME O VEICULO:  ").upper()   
              if remover_veiculo in veiculos:
                print('--------------Veículo Encontrado--------------')
                remover = input('\nDeseja realmente remover os dados desse veículo? S ou N: ').upper()
                if remover == 'S':
                  pos = veiculos.index(remover_veiculo)
                  clientes[pos] = '#'
                  veiculos[pos] = '#'
                  vendas[pos] = '#'
                  print("---DADOS REMOVIDOS COM SUCESSO---")
              else:
                print('O veículo não está registrado no sistema.')
            if modo == 3:
              remover_valor = float(input("INFORME O VALOR:  ")) 
              if remover_valor in vendas: 
                print('--------------Valor da Venda Encontrado--------------')
                remover = input('\nDeseja realmente remover os dados dessa venda? S ou N: ').upper()
                if remover == 'S':
                  pos = vendas.index(remover_valor)
                  clientes[pos] = '#'
                  veiculos[pos] = '#'
                  vendas[pos] = '#'
                  print("---DADOS REMOVIDOS COM SUCESSO---")
              else:
                print('O valor da venda digitado não está associado a nenhuma venda.')
            aux_loop_remover = input('DESEJA REMOVER MAIS REGISTROS? S ou N: ').upper()
        
        if aux_loop_remover == 'N':
             aux_loop_menu == 'S'
    if n == 4:
      
      aux_loop_atualizar ='S'
      while aux_loop_atualizar == 'S':
         att = int(input('\n1 - NOME\n2 - VEICULO\n3 - VALOR DA VENDA\nO QUE VOCÊ DESEJA ALTERAR?:'))
         if att == 1:
           cont_cliente = len(clientes)
           print('\n NÚMERO | CLIENTES')
           for i in range(0,cont_cliente):
             print(f'    {i+1}  -  {clientes[i]}')
           num_att = int(input('INFORME O NUMERO DO CLIENTE QUE DESEJA ALTERAR: '))          
           att_cliente = input(f'DIGITE UM NOVO NOME PARA {clientes[(num_att - 1)]} : ').upper()
           clientes[(num_att - 1)] = att_cliente
           print('---- CLIENTE ALTERADO COM SUCESSO -----')
           aux_loop_atualizar = input('\nDESEJA ALTERAR MAIS ALGUM DADO? S ou N : ').upper()

         elif att == 2:
           cont_veiculo = len(veiculos)
           print('\n NÚMERO |  VEÍCULOS')
           for i in range(0,cont_veiculo):
             print(f'    {i+1}  -  {veiculos[i]}')
           num_att = int(input('INFORME O NUMERO DO VEÍCULO QUE DESEJA ALTERAR: '))          
           att_veiculo = input(f'DIGITE UM NOVO VEÍCULO PARA {veiculos[(num_att - 1)]} : ').upper()
           veiculos[(num_att - 1)] = att_veiculo
           print('---- VEÍCULO ALTERADO COM SUCESSO -----')
           aux_loop_atualizar = input('\nDESEJA ALTERAR MAIS ALGUM DADO? S ou N : ').upper()
         elif att == 3:
           cont_venda = len(vendas)
           print('\n NÚMERO |      VENDA  ')
           for i in range(0,cont_venda):
             print(f'    {i+1}  -  {clientes[i]}  -  {veiculos[i]}  -  {vendas[i]}')
           num_att = int(input('INFORME O NUMERO DA VENDA QUE DESEJA ALTERAR O VALOR: '))          
           att_vendas = input(f'DIGITE UM NOVO VALOR DA VENDA PARA R${vendas[(num_att - 1)]} : R$')
           vendas[(num_att - 1)] = att_vendas
           print('---- VALOR DA VENDA ALTERADO COM SUCESSO -----') 
           aux_loop_atualizar = input('\nDESEJA ALTERAR MAIS ALGUM DADO? S ou N : ').upper() 
      if aux_loop_atualizar == 'N':
             aux_loop_menu == 'S'     