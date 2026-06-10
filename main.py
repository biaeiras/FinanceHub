import os
import json
from entidades import gerenciadorDeUsuario

ARQUIVO_USUARIO = "usuarios.json"

def iniciar_buscando_usuarios_json(): 
    if os.path.exists(ARQUIVO_USUARIO): 
        try: 
            with open(ARQUIVO_USUARIO, "r", encoding= "utf-8") as arquivo: 
                dados = json.load(arquivo)

                gerenciadorDeUsuario.carregatTodosUsuarios(dados)
            
        except Exception:
            print("[AVISO] Arquivo corrompido. Iniciando sistema vazio")

def encerrar_e_salvar_usuarios_json(): 
    print("\n Salvando os dados...")

    dadosFinais = gerenciadorDeUsuario.obterTodosUsuarios()
    with open(ARQUIVO_USUARIO, "w", encoding= "utf-8") as arquivo: 
        json.dump(dadosFinais,arquivo, indent= 4, ensure_ascii= False )
        print("Dados salvos!")


def menuPrincipal(): 

    iniciar_buscando_usuarios_json()

    while True: 
        print("------ Bem-vindo ao Finance Hub! ------")
        print("1 - Cadastro")
        print("2 - Login")
        print("3 - Sair")
        

        try: 

            opcao =int(input("Insira sua opção: "))
        
        except ValueError: 
            print("Por favor, insira apenas as opções dadas")
            continue


        if opcao == 1: 
            cadastroUsuario()
        elif opcao == 3: 
            #login()
            pass
        
        elif opcao == 0: 
            encerrar_e_salvar_usuarios_json()
            print("Obrigada por usar o Finance Hub! Até logo.")


        else: 
            print("Opção inválida ! Tente novamente")

    
        

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
        print("Aporte deve ser um número decimal! ")
        return
    
    perfil = input("Digite seu perfil de risco (conservador, moderado ou arrojado): ").strip().lower()

    novoUsuario = {
        "email":email, 
        "nome": nome, 
        "idade" : idade, 
        "aporte": aporte, 
        "perfil": perfil
    }

    resultado = gerenciadorDeUsuario.CriaUsuario(u = novoUsuario,email = email)

    if resultado == 0: 
        print("Cadastro realizado com sucesso!")
   
    elif resultado == 1: 
        print("Este email já está cadastrado no sistema")
    
    elif resultado == 2: 
        print("Dados inválidos! Verifique se há campos vazios ou valores negativos ")



if __name__ == "__main__": 
    menuPrincipal()