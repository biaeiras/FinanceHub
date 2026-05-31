import unittest 
from gerenciador_usuario import *

class TestGerenciadorUsuario(unittest.TestCase):

    def test_01_validar_usuario_ok_condicao_retorno(self):
        print("Caso de Teste 01 - Validação dados válidos")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }
        retorno_esperado = ValidarDados(usuario)
        self.assertEqual(retorno_esperado, 0)

    def test_02_validar_usuario_falta_campos_obrigatórios(self):
        print("Caso de Teste 02 - Validação dados faltando campos obrigatórios")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "perfil": "moderado"
        }
        retorno_esperado = ValidarDados(usuario)
        self.assertEqual(retorno_esperado, 2)

    def test_03_validar_usuario_tipo_parâmetro_errado(self):
        print("Caso de Teste 03 - Validação passando parâmetro errado")
        
        usuario = "ana@gmail.com, Ana, 30, 500.0, moderado"
        retorno_esperado = ValidarDados(usuario)
        self.assertEqual(retorno_esperado, 2)

    def test_04_validar_usuario_email_formato_errado(self):
        print("Caso de Teste 04 - Validação passando parâmetro errado")
        
        usuario = {
        "email": "anagmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }

        retorno_esperado = ValidarDados(usuario)
        self.assertEqual(retorno_esperado, 2)

    def test_05_validar_email_existe_ok(self):
        print("Caso de Teste 05 - Verificação se email que existe no sistema")

        retorno_esperado =  VerificaExistenciaEmail("ana@gmail.com")
        self.assertEqual(retorno_esperado, 0)
    
    def test_06_validar_nao_email_existe_ok(self):
        print("Caso de Teste 06 - Verificação se email não existe no sistema")

        retorno_esperado =  VerificaExistenciaEmail("carlos@gmail.com")
        self.assertEqual(retorno_esperado, 1)
    
    #COMO FAZER ESSE??
    #def test_07_validar_email_arq_nao_existente(self):

    def test_08_criar_usuario_novo_ok(self):
        print("Caso de Teste 08 - Cria novo usuário")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }
        retorno_esperado =  CriaUsuario("ana@gmail.com", usuario)
        self.assertEqual(retorno_esperado, 0)
    
    def test_09_criar_usuario_campos_obrigatórios_vazios(self):
        print("Caso de Teste 09 - Tenta criar usuário com campos obrigatórios vazios")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "perfil": "moderado"
        }
        retorno_esperado =  CriaUsuario("ana@gmail.com", usuario)
        self.assertEqual(retorno_esperado, 1)
    
    def test_10_criar_usuario_já_existente(self):
        print("Caso de Teste 10 - Tenta criar usuário já existente no sistema")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }
        retorno_esperado =  CriaUsuario("ana@gmail.com", usuario)
        self.assertEqual(retorno_esperado, 1)
    
    def test_11_busca_usuario_existente(self):
        print("Caso de Teste 11 - Busca Usuário já cadastrado no sistema")
        resultado = CarregaPerfilNoArq("ana@gmail.com")

        retorno_esperado == {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "perfil": "moderado"
        }
        self.assertEqual(resultado, retorno_esperado)
    
    def test_12_busca_usuario_nao_existente(self):
        print("Caso de Teste 12 - Busca usuário não cadastrado no sistema")
        resultado = CarregaPerfilNoArq("carlos@gmail.com")

        self.assertEqual(resultado, {})
    
    def test_13_atualiza_usuario_existente(self):
        print("Caso de Teste 13 - Atualiza usuário existente")
        retorno_esperado = AtualizaUsuario(
                            "ana@gmail.com",
                            "aporte",
                            800.0
                            )


        self.assertEqual(retorno_esperado, 0)
    
    def test_14_atualiza_usuario_nao_existente(self):
        print("Caso de Teste 14 - Atualiza usuário não existente")
        retorno_esperado = AtualizaUsuario(
                            "carlos@gmail.com",
                            "aporte",
                            800.0
                            )


        self.assertEqual(retorno_esperado, 1)
    
    def test_15_atualiza_usuario_campo_inválido(self):
        print("Caso de Teste 15 - Atualiza campo inválido")
        retorno_esperado =  AtualizaUsuario(
                            "ana@gmail.com",
                            "cpf",
                            "123.456.789-00"
                            )


        self.assertEqual(retorno_esperado, 1)
    
    def test_16_atualiza_usuario_valor_inválido(self):
        print("Caso de Teste 16 - Atualiza dado com valor inválido")
        retorno_esperado =  AtualizaUsuario(
                            "ana@gmail.com",
                            "aporte",
                            "oitocentos"
                            )


        self.assertEqual(retorno_esperado, 1)


if __name__ == '__main__':
    unittest.main()