import unittest 
from entidades.gerenciadorDeUsuario import *
# Importamos o módulo como objeto para conseguir manipular a memória global dele
import entidades.gerenciadorDeUsuario

class TestGerenciadorUsuario(unittest.TestCase):

    def setUp(self):
        #IA recomendou para testar cada teste de forma separada - 10/06/2026
        """Garante que a memória encapsulada comece 100% limpa antes de CADA teste."""
        entidades.gerenciadorDeUsuario.usuarios = {}

   
    def test_01_validar_usuario_ok_condicao_retorno(self):
        print("Caso de Teste 01 - Validação dados válidos")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }
        retorno = ValidarDados(usuario)
        self.assertEqual(retorno, 0)

    def test_02_validar_usuario_falta_campos_obrigatórios(self):
        print("Caso de Teste 02 - Validação dados faltando campos obrigatórios")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "perfil": "moderado"
        }
        retorno = ValidarDados(usuario)
        self.assertEqual(retorno, 2)

    def test_03_validar_usuario_tipo_parâmetro_errado(self):
        print("Caso de Teste 03 - Validação passando parâmetro errado")
        
        usuario = "ana@gmail.com, Ana, 30, 500.0, moderado"
        retorno = ValidarDados(usuario)
        self.assertEqual(retorno, 2)

    def test_04_validar_usuario_email_formato_errado(self):
        print("Caso de Teste 04 - Validação passando parâmetro errado")
        
        usuario = {
        "email": "anagmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }

        retorno = ValidarDados(usuario)
        self.assertEqual(retorno, 2)

    def test_05_validar_email_existe_ok(self):
        print("Caso de Teste 05 - Verificação se email que existe no sistema")

        #cria usuário 

        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }

        #insere primeiro para o email existir nos dados

        CriaUsuario(usuario, "ana@gmail.com")
        
        retorno =  VerificaExistenciaEmail("ana@gmail.com")
        self.assertEqual(retorno, 0)
    
    def test_06_validar_nao_email_existe_ok(self):
        print("Caso de Teste 06 - Verificação se email não existe no sistema")

        retorno =  VerificaExistenciaEmail("carlos@gmail.com")
        self.assertEqual(retorno, 1)
    
    
    def test_07_validar_email_arq_nao_existente(self):
        print("Caso de Teste 07 - Verificação quando a estrutura de dados está vazia")
        retorno = VerificaExistenciaEmail("ana@gmail.com")
        self.assertEqual(retorno, 1)

    def test_08_criar_usuario_novo_ok(self):
        print("Caso de Teste 08 - Cria novo usuário")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }
        retorno =  CriaUsuario(usuario, "ana@gmail.com")
        self.assertEqual(retorno, 0)
    
    def test_09_criar_usuario_campos_obrigatórios_vazios(self):
        print("Caso de Teste 09 - Tenta criar usuário com campos obrigatórios vazios")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "perfil": "moderado"
        }
        retorno =  CriaUsuario(usuario, "ana@gmail.com" )
        self.assertEqual(retorno, 2)
    
    def test_10_criar_usuario_já_existente(self):
        print("Caso de Teste 10 - Tenta criar usuário já existente no sistema")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }
        #chama a primeira vez pra salvar
        CriaUsuario(usuario, "ana@gmail.com")

        retorno =  CriaUsuario(usuario, "ana@gmail.com")
        self.assertEqual(retorno, 1)
    
    def test_11_busca_usuario_existente(self):
        print("Caso de Teste 11 - Busca Usuário já cadastrado no sistema")

        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }

        CriaUsuario(usuario, "ana@gmail.com")

        resultado = ConsultaUsuario("ana@gmail.com")


        self.assertEqual(resultado, usuario)
    
    def test_12_busca_usuario_nao_existente(self):
        print("Caso de Teste 12 - Busca usuário não cadastrado no sistema")
        resultado = ConsultaUsuario("carlos@gmail.com")

        self.assertEqual(resultado, 1)
    
    def test_13_atualiza_usuario_existente(self):

        print("Caso de Teste 13 - Atualiza usuário existente")

        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }

        CriaUsuario(usuario, "ana@gmail.com")

        retorno = AtualizaUsuario(
                            "ana@gmail.com",
                            "aporte",
                            800.0
                            )


        self.assertEqual(retorno, 0)
    
    def test_14_atualiza_usuario_nao_existente(self):
        print("Caso de Teste 14 - Atualiza usuário não existente")
        retorno = AtualizaUsuario(
                            "carlos@gmail.com",
                            "aporte",
                            800.0
                            )


        self.assertEqual(retorno, 1)
    
    def test_15_atualiza_usuario_campo_inválido(self):
        print("Caso de Teste 15 - Atualiza campo inválido")

        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }

        CriaUsuario(usuario, "ana@gmail.com")
        
        retorno =  AtualizaUsuario(
                            "ana@gmail.com",
                            "cpf",
                            "123.456.789-00"
                            )


        self.assertEqual(retorno, 2)
    
    def test_16_atualiza_usuario_valor_inválido(self):
        print("Caso de Teste 16 - Atualiza dado com valor inválido")

        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }

        CriaUsuario(usuario, "ana@gmail.com")
        retorno =  AtualizaUsuario(
                            "ana@gmail.com",
                            "aporte",
                            "oitocentos"
                            )


        self.assertEqual(retorno, 2)


if __name__ == '__main__':
    unittest.main()