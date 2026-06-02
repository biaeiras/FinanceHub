usuarios = []  

def CarregaArquivo():
    
def SalvaArquivo():
   

def ValidarDados(u):
    camposObrigatorios =["email", "nome", "idade",  "aporte", "perfil" ]
    # é um dict?
    if not isinstance(u, dict): 
        print("Formato inválido")
        return 1
    
    # tem todos os campos obrigatórios?
    if not camposObrigatorios.issubset(dados.keys()):
        print("Campos obrigatórios não preenchidos")
        return 1 
    
    # email tem '@'?

    email = u.get("email")
    if '@' not in email : 
        print("Email inválido")
    
    # nome não está vazio?
    #TEM NCESSIDADE DESSE SE  PRIMEIRO JÁ VERIFICA SE ESTÁ FLATANDO CAMPOS?
    nome = u.get("nome")
    if (nome is None or nome = "") : 
        print("Campo nome vazio")
        return 1
    
    # idade é número positivo?

    idade = u.get("idade")
    if (idade < 0) : 
        print("Idade inválida")
        return 1
    
    # aporte é número positivo?
    aporte = u.get("aporte")
    if (aporte < 0) : 
        print("Aporte inválido")
        return 1

    
    # perfil é conservador/moderado/arrojado?


def VerificaExistenciaEmail(email):
    

def CriaUsuario(u):
    

def CarregaPerfilDoArq(email):
   
def AtualizaUsuario(email, campo, valor):
    