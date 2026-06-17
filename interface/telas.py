from entidades import gerenciadorDeUsuario

from servicos.simuladores import (
    simulador_aposentadoria,
    simulador_investimento
)

__all__ = ["menuPrincipal"]


def menuPrincipal():

    while True:

        print("------ Bem-vindo ao Finance Hub! ------")
        print("1 - Cadastro")
        print("2 - Login")
        print("3 - Sair")

        try:
            opcao = int(input("Insira sua opção: "))

        except ValueError:
            print("Por favor, insira apenas as opções dadas")
            continue

        if opcao == 1:
            cadastroUsuario()

        elif opcao == 2:
            login()

        elif opcao == 3:
            print("Obrigada por usar o Finance Hub! Até logo.")
            break

        else:
            print("Opção inválida ! Tente novamente")


def menuSistemaLogado(nomeUsuario: str, email: str):

    while True:

        print(f"------ Olá, {nomeUsuario} ------")
        print("1 - Atualizar dados")
        print("2 - Simulador de Aposentadoria")
        print("3 - Simulador de Investimentos")
        print("4 - Sair")

        try:
            opcao = int(input("Insira sua opção: "))

        except ValueError:
            print("Por favor, insira apenas as opções dadas")
            continue

        if opcao == 1:

            email = AtualizarDadosUsuario(email)

            dados_atualizados = gerenciadorDeUsuario.ConsultaUsuario(email)

            if dados_atualizados != 1:
                nomeUsuario = dados_atualizados["nome"]

        elif opcao == 2:

            usuario = gerenciadorDeUsuario.ConsultaUsuario(email)

            simulador_aposentadoria(
                usuario["aporte"]
            )

        elif opcao == 3:

            simulador_investimento()

        elif opcao == 4:

            print("Obrigada por usar o Finance Hub! Até logo.")
            break

        else:
            print("Opção inválida ! Tente novamente")


def AtualizarDadosUsuario(email: str):

    while True:

        print("------ATUALIZA USUÁRIO------")
        print("1 - Atualizar email")
        print("2 - Atualizar nome")
        print("3 - Atualizar idade")
        print("4 - Atualizar aporte")
        print("5 - Atualizar perfil")
        print("6 - Sair")

        try:
            opcao = int(input("Insira sua opção: "))

        except ValueError:
            print("Por favor, insira apenas as opções dadas")
            continue

        if opcao == 1:

            campo = "email"
            dado = input("Digite novo email: ").strip()

        elif opcao == 2:

            campo = "nome"
            dado = input("Digite novo nome: ").strip()

        elif opcao == 3:

            campo = "idade"

            try:
                dado = int(input("Digite sua nova idade: "))

            except ValueError:
                print("Idade deve ser um número inteiro!")
                continue

        elif opcao == 4:

            campo = "aporte"

            try:
                dado = float(input("Digite seu novo aporte mensal (R$): "))

            except ValueError:
                print("Aporte deve ser um número decimal!")
                continue

        elif opcao == 5:

            campo = "perfil"

            dado = input(
                "Digite seu novo perfil de risco (conservador, moderado ou arrojado): "
            ).strip().lower()

        elif opcao == 6:

            return email

        else:

            print("Opção Inválida!")
            continue

        resultado = gerenciadorDeUsuario.AtualizaUsuario(
            email=email,
            campo=campo,
            valor=dado
        )

        if resultado == 0:

            print("Perfil atualizado com sucesso!")

            if campo == "email":
                email = dado

        elif resultado == 1:

            print("Este email não foi encontrado no sistema")

        elif resultado == 2:

            print(
                "Dados inválidos! Verifique se há campos vazios ou valores negativos"
            )


def cadastroUsuario():

    print("------CADASTRO USUÁRIO------")

    email = input("Digite seu email: ").strip()
    nome = input("Digite seu nome: ").strip()

    try:
        idade = int(input("Digite sua idade: "))

    except ValueError:
        print("Idade deve ser um número inteiro!")
        return

    try:
        aporte = float(input("Digite seu aporte mensal (R$): "))

    except ValueError:
        print("Aporte deve ser um número decimal!")
        return

    perfil = input(
        "Digite seu perfil de risco (conservador, moderado ou arrojado): "
    ).strip().lower()

    novoUsuario = {
        "email": email,
        "nome": nome,
        "idade": idade,
        "aporte": aporte,
        "perfil": perfil
    }

    resultado = gerenciadorDeUsuario.CriaUsuario(
        u=novoUsuario,
        email=email
    )

    if resultado == 0:

        print("Cadastro realizado com sucesso!")

    elif resultado == 1:

        print("Este email já está cadastrado no sistema")

    elif resultado == 2:

        print(
            "Dados inválidos! Verifique se há campos vazios ou valores negativos"
        )


def login():

    print("------ LOGIN ------")

    email = input("Digite seu email: ").strip()

    usuario = gerenciadorDeUsuario.ConsultaUsuario(email)

    if usuario == 1:

        print("Email não cadastrado! Cadastre-se primeiro")
        return

    nome_usuario = usuario["nome"]

    menuSistemaLogado(
        nomeUsuario=nome_usuario,
        email=email
    )
