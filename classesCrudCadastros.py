import json # biblioteca pra manipulação do arquivo json

#obs: os parâmetros "self" dentro das funções não serão cobrados no momento da execução.
#Eles servem para que a máquina entenda que esta função está dentro de uma classe, sendo o parâmetro "self"
#a representação da mesma.

class crud_cadastro: # classe para as funções mais diretamente relacionadas com o crud de cadastros

    def menuFuncionalidadesProfissionalDeSaúde(): # menu para as funcionalidades do profissional de saúde

        while True:

            userChoise = str(input('\nqual funcionalidade você deseja utilisar\n\n[1] perfil\n[2] outras funcionalidades\n[3] sair do menu de funcionalidades\n\n'))

            try:
                userChoise = int(userChoise)

            except:
                print('\nresposta inválida, tente novamente')

            if userChoise in (1, 2, 3):
                break

            else:
                print('\nvalor inválido, tente novamente')

        return userChoise # retorna um valor inteiro que será posteriormente utilisado no "match" dessas opções

    def menuFuncionalidadesAdm(): # menu de funncionalidades do usuário administrador

        while True:       
        
            while True:

                userChoise = input('\nqual funcionalidade você deseja utilisar?\n\n[1] criar um usuário adiministrador\n[2] consultar um usuário cadastrado\n[3] editar seus dados de usuário\n[4] deletar um usuário\n\n')
           
                try:    
                    
                    userChoise = int(userChoise)
                    break

                except:
                    
                    print('\nresposta inválida')

            if userChoise in (1, 2, 3, 4):
                break
            
            else:

                print('\nresposta inválida, tente novamente')

        return userChoise # retorna um valor inteiro que será posteriormente utilisado no "match" dessas opções
    
    def menuPerfilUsuário(): # menu de opções relacionadas ao perfil de um usuário qualquer

        while True:

            userChoise = str(input('\nqual ação deseja realizar?\n\n[1] consultar os dados do seu perfil\n[2] editar o seu perfil\n[3] deletar o seu perfil\n\n'))

            try:
                userChoise = int(userChoise)

                if userChoise in (1, 2, 3):
                    break

                else:
                    print('\nvalor inválido, tente novamente')

            except:
                print('\nresposta inválida, tente novamente')

        return userChoise # retorna um valor inteiro que será posteriormente utilisado no "match" dessas opções
    
    def matchPerfilUsuário(userChoise, userName): 
        
        # "match" dos valores retornados na função "menuPerfilUsuário"

        from classesCrudCadastros import crud_cadastro # importação da classe "crud_cadastro"
        classe = crud_cadastro # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        match userChoise:

            case 1:
                classe.print_user_user(userName) # printa os dados do usuário no terminal, incluindo a senha

            case 2:

                classe.edição_usuário(userName) # contém menu e match de edição do perfil

            case 3:
                with open('crudCadastros.json', 'r+') as database:

                    dicCrud = json.load(database)
                    del dicCrud[userName]           # deleta o perfil
                    database.seek(0)
                    json.dump(dicCrud, database, indent=2)
                    database.truncate()
                    print('\nalterações salvas com sucesso!')

    def edição_usuário(userName): 
        
        # função geral para edição do perfil do usuário, contendo menu de opções e match de funcionalidades

        from classesCrudCadastros import Inputs # importação da classe "Inputs"
        classeInputs = Inputs # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        from classesCrudCadastros import crud_cadastro # importação da classe "crud_cadastro"
        classeCrud = crud_cadastro # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        with open('crudCadastros.json', 'r+') as database:

            dicCrud = json.load(database)

            try:

                userProfile = dicCrud[userName]
                classeCrud.print_user_user(userName) # printa os dados do usuário no console, incluindo sua senha
                userChoise2 = classeCrud.menu_edição() # imprime um menu de opções de edição do perfil do usuário

                match userChoise2: # match da opção de edição escolhida no menu de edições

                    case 1:
                        change = classeInputs.input_string('seu novo nome de usuário') # realiza o input do novo nome de usuário
                        del dicCrud[userName]
                        dicCrud[change] = userProfile

                    
                    case 2:
                        change = classeInputs.input_classe_usuario_comum() # faz o input da nova classe do usuário
                        userProfile[(userChoise2 - 2)] = change
                        dicCrud[userName] = userProfile

                    case 3:
                        change = classeInputs.input_tipo_diabetes() # faz o input do novo tipo de diabetes
                        userProfile[(userChoise2 - 2)] = change
                        dicCrud[userName] = userProfile

                    case 4:
                        change = str(input('\ndigite sua nova senha: ')).strip() # faz o input da nova senha do usuário
                        userProfile[(userChoise2 - 2)] = change
                        dicCrud[userName] = userProfile

                database.seek(0)
                json.dump(dicCrud, database, indent=2)
                database.truncate()
                print('\nalterações salvas com sucesso!')

            except:
                print('\nnome de usuário alterado, faça login novamente para alterar outros dados')


    def CreateOrdinaryUser(): # cria um novo usuário

        from classesCrudCadastros import Inputs # importação da classe "Inputs"
        classe = Inputs # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        listaIntermediária = [] # lista utilizada na blocação dos dados do usuário

        userName = classe.input_string('seu nome de usuário') # faz o input do nome do usuário
        userClass = classe.input_classe_usuario_comum() # faz o input da classe do usuário

        listaIntermediária.append(userClass) # salva a classe do usuário na lista intermediária

        match userClass: # match para o tipo de diabetes

            case 'paciente':
                userType = classe.input_tipo_diabetes() # faz o input do tipo de diabetes
                listaIntermediária.append(userType) # salva o tipo de diabetes na lista intermediária

            case 'profissional de saúde':
                userType = '-' # define como "vazio" o tipo de diabetes do profissional de saúde
                listaIntermediária.append(userType) # salva o tipo de diabetes na lista intermediária

        password = str(input('\ndigite a sua senha: ')).strip() # faz o input da senha do usuário
        listaIntermediária.append(password) # salva a senha do usuário na lista intermediária

        with open('crudCadastros.json', 'r+') as database:

            dicCrud = json.load(database) 

            dicCrud[userName] = listaIntermediária[:] # dicionário do crud recebe uma cópia dos dados da lista intermediária, usando como chave o nome de usuário digitado anteriormente

            database.seek(0)

            json.dump(dicCrud, database, indent=2)
        
        listaIntermediária.clear() # limpa os dados da lista intermediária

    def CreateAdmUser(): # função para criar um usuário adiministrador

        from classesCrudCadastros import Inputs # importação da classe "Inputs"
        classe = Inputs # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        listaIntermediária = [] # lista utilizada na blocação dos dados do usuário

        userName = classe.input_string('o nome de usuário do adiministrador') # faz o input do nome de usuário do adiministrador

        userClass = 'adiministrador' # define a classe do usuário como adiministrador
        listaIntermediária.append(userClass) # salva a classe do usuário na lista intermediária

        userType = '-' # define como "vazio" o tipo de diabetes do adiministrador
        listaIntermediária.append(userType) # salva o tipo de diabetes do adiministrador na lista intermediária

        password = str(input('\ndigite a sua senha de adiministrador: ')).strip() # faz o input da senha do adiministrador
        listaIntermediária.append(password) # salva a senha do adiministrador na lista intermediária

        with open('crudCadastros.json', 'r+') as database:

            dicCrud = json.load(database) 

            dicCrud[userName] = listaIntermediária[:] # dicionário do crud recebe uma cópia dos dados da lista intermediária, usando como chave o nome de usuário digitado anteriormente

            database.seek(0)

            json.dump(dicCrud, database, indent=2)
        
        listaIntermediária.clear()

    def Read(): # função para consulta dos dados pelo adiministrador

        from classesCrudCadastros import Inputs # importação da classe "Inputs"
        classeInputs = Inputs # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        from classesCrudCadastros import crud_cadastro # importação da classe "crud_cadastro"
        classeCrud = crud_cadastro # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        from classesCrudCadastros import Funcionalidades # importação da classe Funcionalidades
        classeFuncionalidades = Funcionalidades # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        classeCrud.print_users() # printa o nome de todos os usuários no console

        while True:

            userChoise = 1

            userKey = classeInputs.input_string('o nome do usuário a ser consultado') # faz o input do nome do usuário que terá os dados cadastrados

            with open('crudCadastros.json', 'r') as database:

                dicCrud = json.load(database)

                if userKey in dicCrud:

                    classeCrud.print_user(userKey) # printa os dados do usuário, sem expor a senha do usuário
                    break

                else:

                    print('\nusuário não encontrado em nosso banco de dados')
                    userChoise = classeFuncionalidades.verificacao_de_prossegimento('tentando', 'retornar ao menu anterior') # verifica se o usuário deseja continuar tentando consultar um usuário ou retornar ao menu anterior

                    if userChoise == 2: # caso o usuário tenha escolhido não continuar tentando
                        break
        
        if userChoise == 2: # caso o usuário tenha escolhido parar, retorna o valor numérico "2" para realizar o break no código principal
            return userChoise
    
    def Delete(): # função para deletar um usuário
        from classesCrudCadastros import Inputs # importação da classe "Inputs"
        classeInputs = Inputs # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        from classesCrudCadastros import Funcionalidades # importação da classe "Funcionalidades"
        classeFuncionalidades = Funcionalidades # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        from classesCrudCadastros import crud_cadastro # importação da classe "crud_cadastro"
        classeCrud = crud_cadastro # instanciando a classe importada em uma variável a fim de permitir sua utilisação

        while True:
            userChoise = 'defoult'

            classeCrud.print_users() # print o nome de todos os usuários 
            userDel = classeInputs.input_string('o nome do usuário a ser deletado') # faz o input do nome do usuário que terá seu perfil deletado

            with open('crudCadastros.json', 'r+') as database:

                dicCrud = json.load(database)

                if userDel in dicCrud:

                    del dicCrud[userDel]
                    database.seek(0)
                    json.dump(dicCrud, database, indent=2)
                    database.truncate()
                    print('\nalterações salvas com sucesso!')
                    break

                else:
                    print('\neste usuário não existe em nosso banco de dados')

                    userChoise = classeFuncionalidades.verificacao_de_prossegimento('tentando', 'retornar ao menu anterior') # verifica se o usuári deseja continuar tentando cadas

                    if userChoise == 2: # caso o usu
                        break

        return userChoise

    def login():

        from classesCrudCadastros import Inputs
        classe = Inputs

        while True:

            nameLogin = classe.input_string('seu nome de usuário')

            with open('crudCadastros.json', 'r') as database:

                dicCrud = json.load(database)

                if nameLogin in dicCrud:

                    passwordLogin = str(input('digite sua senha: ')).strip()

                    userProfile = dicCrud[nameLogin]

                    if passwordLogin == userProfile[2]:
                        return nameLogin
                    
                    else:
                        return 'defoult'
                else:
                    return 'defoult'
                
    def verificação_classe_usuário(key):

        with open('crudCadastros.json') as database:

            dicCrud = json.load(database)

            lista = dicCrud[key]

            userClass = lista[0]

            return userClass
        
    def menu_edição():

        while True:

            userChoise = str(input('\ndigite o que você deseja alterar no perfil selecionado\n\n[1] nome de usuário\n[2] classe do usuário\n[3] tipo de diabetes\n[4] alterar senha\n\n')).strip()

            try:

                userChoise = int(userChoise)
                break

            except:
                
                print('\nvalor inválido, tente novamente')

            if userChoise in (1, 2, 3, 4):
                break

            else:
                print('\nvalor inválido, tente novamente')

        return userChoise
    
    def print_user(userName):

        import json

        with open('crudCadastros.json') as database:

            dicCrud = json.load(database)
            userProfile = dicCrud[userName]

            print('=' * 45)
            print(f'\nnome do usuário: {userName}\nclasse do usuário: {userProfile[0]}\ntipo de diabetes: {userProfile[1]}\n')
            print('=' * 45)

    def print_user_user(userName):

        import json

        with open('crudCadastros.json') as database:

            dicCrud = json.load(database)

            try:
                userProfile = dicCrud[userName]

                print('=' * 45)
                print(f'\nnome do usuário: {userName}\nclasse do usuário: {userProfile[0]}\ntipo de diabetes: {userProfile[1]}\nsenha: {userProfile[2]}\n')
                print('=' * 45)

            except:
                print('\nnome de usuário alterado, faça lpgin novamente para resalisar novas alterações')

    def print_users():

        contador = 0

        with open('crudCadastros.json') as database:

            dicCrud = json.load(database)

            keysList = list(dicCrud.keys())

            print('=' * 4, 'usuários cadastrados', '=' * 4)

            for key in dicCrud:

                print(f'usuário nº{contador + 1}: {keysList[contador]}')

                contador += 1

            print('=' * 29)

class Inputs:
                
    def input_string(complemento):  # retorna uma string

        while True:

            string = str(input(f'\ndigite {complemento}: ')).strip().upper()

            if string != '':
                break

            print('\nfrase inválida, tente novamente')
        return string
    
    def input_float(complemento):

        while True:

            userNumber = str(input(f'\ndigite {complemento}: ')).strip()

            try:
                userNumber = float(userNumber)
                break

            except:
                print('\nvalor inválido, tente novamente')

        return userNumber

    def input_classe_usuario_comum():  # retorna um inteiro

        while True:

            classe_usuário = str(input('\ndigite o seu tipo de usuário\n\n[1] paciente\n[2] profissional de saúde\n\n')).strip()

            try:
                classe_usuário = int(classe_usuário)

                if classe_usuário in (1, 2):
                    break

                else:
                    print('\nvalor inválido, tente novamente')

            except:
                print('\nresposta inválida, tente novamente')
                    
        match classe_usuário:

            case 1:
                return 'paciente'
            
            case 2:
                return 'profissional de saúde'
            
    def input_tipo_diabetes():  # retorna um inteiro

        while True:

            tipo = str(input("\nInsira seu tipo de diabetes: \n \n[1] diabetes tipo 1\n[2] diabetes tipo 2\n[3] diabetes gestacional\n[4] pré diabetes\n\n")).strip()

            try:
                tipo = int(tipo)

            except:
                print('\nresposta inválida, tente novamente')

            if tipo in (1, 2, 3, 4):
                break

        match tipo:

            case 1:
                return 'diabetes tipo 1'
            
            case 2:
                return 'diabetes tipo 2'
            
            case 3:
                return 'diabetes gestacional'
            
            case 4:
                return 'pré diabetes'
            
class Funcionalidades:
    def main_remedinhos():
        import json, time, os

        def limpar_tela():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        def carregar_json():
            global medicamentos  # Permite que a variável medicamentos seja usada globalmente
            try:
                with open('dados.json', 'r') as file:
                    medicamentos = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                medicamentos = []

        def salvar_json():
            objeto_json = json.dumps(medicamentos, indent=4)
            with open('dados.json', 'w') as file:
                file.write(objeto_json)

        def adicionar_medicamentos():
            nome = input("Informe o nome do medicamento >>>> ")
            horario = input("Informe o horario que você irá tomar esse medicamento (HH:MM) >>>> ")
            dosagem = input("Informe a dosagem do medicamento >>>> ")
            medicamento = {
                'Nome': nome,
                'Horario': horario,
                'Dosagem': dosagem        
            }
            medicamentos.append(medicamento)
            salvar_json()

        def visualizar_medicamentos_menu():
            if not medicamentos:
                print("\nNenhum medicamento cadastrado!! (PRECIONE [ENTER] PARA CONTINUAR)")
            for num, medicamento in enumerate(medicamentos, start=1):
                print(f"\n{num}. Nome: {medicamento['Nome']}, Horario: {medicamento['Horario']}, Dosagem: {medicamento['Dosagem']}\n")
            print("Digite [sair] para parar de visualizar")
            opcao = input(">>> ")
            if opcao.lower() == 'sair':
                return

        def visualizar_medicamentos():
            if not medicamentos:
                print("\nNenhum medicamento cadastrado!! (PRECIONE [ENTER] PARA CONTINUAR)")
            for num, medicamento in enumerate(medicamentos, start=1):
                print(f"\n{num}. Nome: {medicamento['Nome']}, Horario: {medicamento['Horario']}, Dosagem: {medicamento['Dosagem']}\n")

        def atualizar_medicamento():
            visualizar_medicamentos()
            indice = int(input("\nInforme o indice do medicamento que voce deseja atualizar [0] PARA VOLTAR AO MENU >>>> ")) - 1
            if 0 <= indice < len(medicamentos):
                nome = input("\nInforme o novo nome do medicamento >>>> ")
                horario = input("\nInforme o novo horario que você irá tomar esse medicamento (HH:MM) >>>> ")
                dosagem = input("\nInforme a nova dosagem do medicamento >>>> ")
                medicamentos[indice]['Nome'] = nome
                medicamentos[indice]['Horario'] = horario
                medicamentos[indice]['Dosagem'] = dosagem
                salvar_json()
                print("Atualizado...")
                time.sleep(3)
                limpar_tela()
            elif indice == -1:
                print("Voltando ao menu principal...")
                time.sleep(2)
                limpar_tela()
                return
            else:
                print("Indice Invalido!")
                time.sleep(3)
                limpar_tela()

        def deletar_medicamento():
            visualizar_medicamentos()
            indice = int(input("Informe o numero do medicamento que voce deseja excluir >>>> ")) - 1
            if 0 <= indice < len(medicamentos):
                medicamentos.pop(indice)
                salvar_json()
                print("Excluido...")
                time.sleep(2)
                print("Excluido com sucesso!")
            else:
                print("Indice invalido...")

        def main_remedios():
            carregar_json()
            while True:
                limpar_tela()
                print("\n\n[1] Adicionar Medicamento")
                print("[2] Visualizar Medicamento")
                print("[3] Atualizar Medicamento")
                print("[4] Remover Medicamento")
                print("[5] Sair")
                try:
                    opcao = int(input("\nescolha uma opcao>>>> "))
                    match opcao:
                        case 1:
                            limpar_tela()
                            adicionar_medicamentos()
                        case 2:
                            limpar_tela()
                            visualizar_medicamentos_menu()
                        case 3:
                            limpar_tela()
                            atualizar_medicamento()
                        case 4:
                            limpar_tela()
                            deletar_medicamento()
                        case 5:
                            limpar_tela()
                            print("Voltando ao menu Principal")
                            time.sleep(3)
                            break
                        case _:
                            print("\nOpcao Invalidada, tente novamente...")
                except ValueError:
                    limpar_tela()
                    print("Opcao invalida! Informe outra opcao...")
                    time.sleep(3)

        main_remedios()


    def verificacao_nivel_glicose(glicose):

        if glicose <= 70:
            print("\nvocê está em estado de Hipoglicemia, procure ajuda assim que possível")

        elif 70 < glicose <= 150:
            print("\nGlicose dentro do intervalo ideal")

        elif 150 < glicose <= 300:
            print("\nGlicose acima do intervalo ideal, recomenda-se a adoção de uma medida preventiva assim que possível")

        else:
            print("\n você está em estado de Hiperglicemia, faça uso da dose adequada de insulina asim que possível")

    def calculador_quant_insulina(glicose, qtd_carbo):  # retorna um valor numérico

        fator_correcao = 50
        glicemia_alvo = 100
        razao_carbo = 15

        unidades_insulina = (((glicose - glicemia_alvo) / fator_correcao) + (qtd_carbo / razao_carbo))

        return unidades_insulina

    def formatacao_unidades_de_isulina(unidades_insulina):  # formata o valor retornado na função anterior

        import math

        insulina_inteiro = math.trunc(unidades_insulina)

        if (unidades_insulina - insulina_inteiro) == 0:
            insulina_print = unidades_insulina

        elif (unidades_insulina - insulina_inteiro) > 0 and (unidades_insulina - insulina_inteiro) < 0.5:
            insulina_print = math.floor(unidades_insulina)

        elif (unidades_insulina - insulina_inteiro) > 0.5:
            insulina_print = math.ceil(unidades_insulina)

        return insulina_print

    def monitoramento_consulta():  # calcula o intervalo entre a última consulta e a "data atual", retornando um veedback via print
        data_ultima_consulta = str(input('\ndigite a data da sua última consulta médica (ex: 01/01/2001): ')).strip()

        dia_ultima_consulta = int(data_ultima_consulta[:2])
        mes_ultima_consulta = int(data_ultima_consulta[3:5])
        ano_ultima_consulta = int(data_ultima_consulta[6:10])

        data_atual = '21/05/2024'

        dia_atual = int(data_atual[:2])
        mes_atual = int(data_atual[3:5])
        ano_atual = int(data_atual[6:10])

        if ((dia_ultima_consulta - dia_atual)**2 + ((mes_ultima_consulta - mes_atual) * 30)**2 + ((ano_ultima_consulta - ano_atual) * 365)**2) > 180 ** 2:
            print('\nparece que faz muito tempo desde a sua última consulta, vá imadiatamente consular o seu médico')

        elif ((dia_ultima_consulta - dia_atual)**2 + ((mes_ultima_consulta - mes_atual) * 30)**2 + ((ano_ultima_consulta - ano_atual) * 365)**2) > 90 ** 2:
            print('\nparece que faz um tempo desde a sua última consulta, é recomendado que você volte para uma nova conúlta com o seu médico responsável')

        else:
            print('\nparece que você ainda está dentro do prazo recomendado, continue com um bom acompanhamento')

    def calculadora_alimentos():  # mostra a quatidade de carboidratos em determinados alimentos

        while True:
            print("1 - Arroz\n" "2 - Macarrao\n" "3 - Feijão\n" "4 - Uva\n" "5 - Batata Inglesa\n" "6 - Tapioca\n" "7 - Cuscuz\n" "8 - Macaxeira\n" "9 - Chocolate\n" "10 - Batata Frita\n" "11 - Pão de Forma\n" "12 - Batata Doce\n" "13 - Banana\n" "14 - Maçã\n" "15 - Pão Francês")

            escolha = str(input("qual alimento você deseja? ")).strip()

            try:
                escolha = int(escolha)

            except:
                print('\nresposta inválida, tente novamente')

            if escolha in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
                break

        while True:

            qtd_alimento = str(input('\ninforme a quantidade, em gramas, deste alimento que será consumida: ')).strip()

            try:
                qtd_alimento = float(qtd_alimento)
                break

            except:
                print('\nresposta inválida, tente novamente')

        match(escolha):
            case 1:
                total_arroz = qtd_alimento * 0.28
                print(f"a quantidade de carboidratos é: {total_arroz}")

            case 2:
                total_macarrao = qtd_alimento * 0.31
                print(f"a quantidade de carboidratos é: {total_macarrao}")

            case 3:
                total_feijao = qtd_alimento * 0.14
                print(f"a quantidade de carboidratos é : {total_feijao}")

            case 4:
                total_uva = qtd_alimento * 0.14
                print(f"a quantidade de carboidratos é: {total_uva}")

            case 5:
                total_batata_inglesa = qtd_alimento * 0.19
                print(f"a quantidade de carboidratos é: {total_batata_inglesa}")

            case 6:
                total_tapioca = qtd_alimento * 0.93
                print(f"a quantidade de carboidratos é: {total_tapioca}")

            case 7:
                total_cuscuz = qtd_alimento * 0.77
                print(f"a quantidade de carboidratos é: {total_cuscuz}")

            case 8:
                total_macaxeira = qtd_alimento * 0.30
                print(f"a quantidade de carboidratos é: {total_macaxeira}")

            case 9:
                total_chocolate = qtd_alimento * 0.56
                print(f"a quantidade de carboidratos é: {total_chocolate}")

            case 10:
                total_batata_frita = qtd_alimento * 0.35
                print(f"a quantidade de carboidratos é: {total_batata_frita}")

            case 11:
                total_pao_forma = qtd_alimento * 25
                print(f"a quantidade de carboidratos é: {total_pao_forma}")

            case 12:
                total_batata_doce = qtd_alimento * 0.19
                print(f"a quantidade de carboidratos é: {total_batata_doce}")

            case 13:
                total_bananas = qtd_alimento * 26
                print(f"a quantide de carboidratos é: {total_bananas}")

            case 14:
                total_maca = qtd_alimento * 15
                print(f"a quantidade de carboiddratos é: {total_maca}")

            case 15:
                total_pao_frances = qtd_alimento * 28
                print(f"a quantidade de carboidratos é: {total_pao_frances}")
    
    
    def menu_funcionalidades_paciente():  # retorna uma string

        while True:
            user_choise = str(input('\nselecione a funcionalidade que você deseja utilisar\n\n[1] perfil\n[2] calculadora de carboidratos\n[3] calculadora de alimentos\n[4] situação da glicemia\n[5] monitoramento de  consultas\n[6] Calendario de remedios\n[7] voltar ao menu principal\n\n')).strip()
            
            try:
                user_choise = int(user_choise)

            except:
                print('\nfrase inválida, tente novamente')

            if user_choise in (1, 2, 3, 4, 5, 6, 7):
                break


        return user_choise

    def verificacao_de_prossegimento(complemento_pergunta, complemento_negacao):  # retorna um inteiro

        while True:

            verificacao = str(input(f'\ndeseja continuar {complemento_pergunta}?\n\n[1] sim\n[2] não, {complemento_negacao}\n\n')).strip()

            try:
                verificacao = int(verificacao)

            except:
                print('\nresposta inválida, tente novamente')

            if verificacao in (1, 2):
                break

            else:
                print('\nvalor inválido, tente novamente')


        return verificacao

    def match_funcionalidades_pacientes(user_choise, userName):

        from classesCrudCadastros import Inputs
        classeInputs = Inputs

        from classesCrudCadastros import crud_cadastro
        classeCrud = crud_cadastro

        from classesCrudCadastros import Funcionalidades
        classeFuncionalidades = Funcionalidades

        match user_choise:

            case 1:
                escolha = classeCrud.menuPerfilUsuário()

                classeCrud.matchPerfilUsuário(escolha, userName)

            case 2:

                glicose = classeInputs.input_float('sua glicemia')
                qtd_carbo = classeInputs.input_float('sua quantidade de carboidratos')

                unidades_insulina = classeFuncionalidades.calculador_quant_insulina(glicose, qtd_carbo)

                insulina_print = classeFuncionalidades.formatacao_unidades_de_isulina(unidades_insulina)

                print(f"A quantidade de insulina a ser tomada é: {insulina_print}ml")

            case 3:

                classeFuncionalidades.calculadora_alimentos()

            case 4:

                glicemia = classeInputs.input_float('sua glicemia')

                classeFuncionalidades.verificacao_nivel_glicose(glicemia)

            case 5:

                classeFuncionalidades.monitoramento_consulta()
            
            case 6:
                classeFuncionalidades.main_remedinhos()
