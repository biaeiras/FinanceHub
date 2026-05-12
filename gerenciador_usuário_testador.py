#IMPORTAR MÓDULOS


#ValidarDados

# TESTE C1

usuario = {
    "email": "ana@gmail.com",
    "nome": "Ana",
    "idade": 30,
    "aporte": 500.0,
    "perfil": "moderado"
}

resultado = ValidarDados(usuario)

assert resultado == True

print("C1 PASSOU")


# TESTE C2

usuario = {
    "email": "ana@gmail.com",
    "nome": "Ana",
    "idade": 30,
    "perfil": "moderado"
}

resultado = ValidarDados(usuario)

assert resultado == False

print("C2 PASSOU")


# TESTE C3

usuario = "ana@gmail.com, Ana, 30, 500.0, moderado"

resultado = ValidarDados(usuario)

assert resultado == False

print("C3 PASSOU")


# TESTE C4

usuario = {
    "email": "anagmail.com",
    "nome": "Ana",
    "idade": 30,
    "aporte": 500.0,
    "perfil": "moderado"
}

resultado = ValidarDados(usuario)

assert resultado == False

print("C4 PASSOU")



# VerificaExistenciaEmail

# TESTE C1

resultado = VerificaExistenciaEmail("ana@gmail.com")

assert resultado == True

print("C1 PASSOU")


# TESTE C2

resultado = VerificaExistenciaEmail("carlos@gmail.com")

assert resultado == False

print("C2 PASSOU")


# TESTE C3

resultado = VerificaExistenciaEmail("ana@gmail.com")

assert resultado == False

print("C3 PASSOU")


# CriaUsuario


# TESTE C1

usuario = {
    "email": "ana@gmail.com",
    "nome": "Ana",
    "idade": 30,
    "aporte": 500.0,
    "perfil": "moderado"
}

resultado = CriaUsuario("ana@gmail.com", usuario)

assert resultado == True

print("C1 PASSOU")


# TESTE C2

usuario = {
    "email": "ana@gmail.com",
    "nome": "Ana",
    "idade": 30,
    "perfil": "moderado"
}

resultado = CriaUsuario("ana@gmail.com", usuario)

assert resultado == False

print("C2 PASSOU")


# TESTE C3

usuario = {
    "email": "ana@gmail.com",
    "nome": "Ana",
    "idade": 30,
    "aporte": 500.0,
    "perfil": "moderado"
}

resultado = CriaUsuario("ana@gmail.com", usuario)

assert resultado == False

print("C3 PASSOU")


# CarregaPerfilNoArq

# TESTE C1

resultado = CarregaPerfilNoArq("ana@gmail.com")

assert resultado == {
    "email": "ana@gmail.com",
    "nome": "Ana",
    "idade": 30,
    "aporte": 500.0,
    "perfil": "moderado"
}

print("C1 PASSOU")


# TESTE C2

resultado = CarregaPerfilNoArq("ana@gmail.com")

assert resultado == {}

print("C2 PASSOU")


# TESTE C3

resultado = CarregaPerfilNoArq("carlos@gmail.com")

assert resultado == {}

print("C3 PASSOU")


# AtualizaUsuario


# TESTE C1

resultado = AtualizaUsuario(
    "ana@gmail.com",
    "aporte",
    800.0
)

assert resultado == True

print("C1 PASSOU")


# TESTE C2

resultado = AtualizaUsuario(
    "carlos@gmail.com",
    "aporte",
    800.0
)

assert resultado == False

print("C2 PASSOU")


# TESTE C3

resultado = AtualizaUsuario(
    "ana@gmail.com",
    "cpf",
    "123.456.789-00"
)

assert resultado == False

print("C3 PASSOU")


# TESTE C4

resultado = AtualizaUsuario(
    "ana@gmail.com",
    "aporte",
    "oitocentos"
)

assert resultado == False

print("C4 PASSOU")


print("Todos os testes passaram!")