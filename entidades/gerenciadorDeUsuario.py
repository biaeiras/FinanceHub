#Apresenta a lista de funções a serem disponibilizadas pelo módulo
__all__ = ["ValidarDados", "VerificaExistenciaEmail", "CriaUsuario", "ConsultaUsuario", "AtualizaUsuario", "obterTodosUsuarios", "carregarTodosUsuarios" ] 

usuarios = {}

def obterTodosUsuarios() -> dict:
    return usuarios
    
def carregarTodosUsuarios(dadosCarregados: dict):
    global usuarios
    usuarios.clear()
    usuarios.update(dadosCarregados)
  

def ValidarDados(u: dict) -> int:

    """
    Retorno 0 -> Dados inválidos
    Retorno 2 -> Parâmetros inválidos, tipos errados ou campos ausentes

    """
    if not isinstance(u, dict): 
        return 2
    
    try: 

        email = u.get("email")
        nome = u.get("nome")
        idade = u.get("idade")
        aporte = u.get("aporte")
        perfil = u.get("perfil")

        # 2 - Validação se campo for ausente(None) ou vazio ("")

        if email is None or str(email).strip() == "": 
            return 2
        
        if nome is None or str(nome).strip() == "": 
            return 2

        if idade is None: 
            return 2
        
        if aporte is None: 
            return 2
        
        if perfil is None: 
            return 2

        #3 - Validação de Email ( Possui @?)
        email = str(u.get("email")).strip()
        if '@' not in email : 
            return 2 
    
    
        # 4 -Validação de Nome (nome não está vazio?)
        nome = str(u.get("nome")).strip()
        if nome is None or nome == "" : 
            return 2
    
        #5 - Validação da Idade (idade é número positivo?)

        idade =int(u.get("idade"))
        if (idade < 0) : 
            return 2
    
        #6- aporte é número positivo?
        aporte = float(u.get("aporte"))
        if (aporte <= 0) : 
            return 2

    
        #7- Validação de perfil (perfil é conservador/moderado/arrojado?)
        perfil = str(u.get("perfil")).strip().lower()
        tipos_validos = {"conservador", "moderado", "arrojado"}

        if perfil not in tipos_validos: 
            return 2
        

        #se não entrou em nenhum if(passou por tudo)

        return 0
    
    except(ValueError, TypeError):
        return 2
    


def VerificaExistenciaEmail(email:str) -> int:
    """
    Retorno 0 -> Usuário encontrado
    Retorno 1 -> Usuário não encontrado

    """
     
    if email in usuarios: 
        return 0
     
    return 1 

    

def CriaUsuario(u: dict, email: str):
    """
    Retorno 0 -> Usuário Inserido com sucesso
    Retorno 1 -> Email já cadastrado
    Retorno 2 -> Dados inválidos

    """

    #1 - Valida os dados antes 
    if ValidarDados(u) == 2: 
        return 2
    
    #2 - Checa se o email existe 
    if VerificaExistenciaEmail(email) == 0:
        return 1
    
    #3 - Se o email passou, guarda no dicionário 
    usuarios[email] = {
        "email": str(u.get("email")).strip(), 
        "nome": str(u.get("nome")).strip(), 
        "idade": int(u.get("idade")), 
        "aporte": float(u.get("aporte")),
        "perfil": str(u.get("perfil")).strip().lower()
    }
    
    return 0 
    

def ConsultaUsuario(email: str):
    """
    Retorna  o  dicionário do usuário se o email for encontrado 
    Retorna 1 se o email não existir 
    """
    email = str(email).strip()
    if email in usuarios: 
        return usuarios[email]

    return 1
   
def AtualizaUsuario(email: str, campo: str, valor) -> int:
    """
    Retorna 0 -> Atualizado com sucesso
    Retorna 1 -> Email não encontrado 
    Retorna 2 -> Campo inválido ou Valor Inválido

    """
    if VerificaExistenciaEmail(email) == 1: 
        return 1 
    
    #isso é validação, ataualizar tá fazendo mais do que devia?
    camposValidos = {"nome", "idade", "aporte", "perfil"}
    if campo not in camposValidos: 
        return 2
    
    usuario_temp = usuarios[email].copy() 
    usuario_temp[campo] = valor

    if ValidarDados(usuario_temp) == 2: 
        return 2
    
    elif campo == "idade": 
       usuarios[email][campo] = int(valor) 
    
    elif campo == "aporte": 
       usuarios[email][campo] = float(valor)
    
    elif campo == "perfil": 
       usuarios[email][campo] = str(valor).strip().lower()
    
    else: 
        usuarios[email][campo] = str(valor).strip()
        

    return 0 
    