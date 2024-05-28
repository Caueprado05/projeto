from classesCrudCadastros import crud_cadastro

classeGlicode = crud_cadastro

from classesCrudCadastros import Funcionalidades
classeGlicode2 = Funcionalidades



while True:

    login = 'defoult'
    continuos = 1
    userClass = ''

    while True:
        userFirstAction = str(input('\no que você deseja fazer?\n\n[1] fazer login\n[2] criar usuário\n[3] sair do sistema\n\n')).strip()

        try:
            userFirstAction = int(userFirstAction)

        except:
            print('\nresposta inválida, tente novamente')

        if userFirstAction in (1, 2, 3):
            break

    while True:

        while True:
            match userFirstAction:

                case 1:
                        login = classeGlicode.login()

                        if login == 'defoult':

                            print('\nusuário ou senha incorretos')
                            continuos = classeGlicode.verificacao_de_prossegimento('continuar tentando', 'retornar ao menu anterior')
                            break

                        else:

                            userClass = classeGlicode.verificação_classe_usuário(login)
                            break

                case 2:
                    classeGlicode.CreateOrdinaryUser()
                    break

                case 3:
                    break

        if continuos == 2 or userFirstAction == 3 or login == 'defoult' or userClass != '':
            break

    if continuos == 2 or userFirstAction == 3:
            break

    if userClass == 'adiministrador':

        while True:
        
            userChoise = classeGlicode.menuFuncionalidadesAdm()

            match userChoise:

                case 1:

                    classeGlicode.CreateAdmUser()

                case 2:

                    verify = classeGlicode.Read()

                    if verify == 2:
                        break

                case 3:

                    classeGlicode.edição_usuário(login)

                case 4:

                    verify = classeGlicode.Delete()

                    if verify == 2:
                        break

            userProceed = classeGlicode2.verificacao_de_prossegimento('a utilisar alguma outra funcionalidade', 'voltar para menu principal')

            if userProceed == 2:
                break

    elif userClass == 'paciente':

        while True:

            user_choise = classeGlicode2.menu_funcionalidades_paciente()

            if user_choise == 7:
                break

            classeGlicode2.match_funcionalidades_pacientes(user_choise, login)

    elif userClass == 'profissional de saúde':

        while True:

            user_choise = classeGlicode.menuFuncionalidadesProfissionalDeSaúde()

            if user_choise == 3:
                break

            match user_choise:

                case 1:

                    menuChoise = classeGlicode.menuPerfilUsuário()

                    classeGlicode.matchPerfilUsuário(menuChoise, login)

                case 2:

                    print('\natualizações virão em breve :)')

                case 3:
                    
                    break

    else:
        pass
