"""#cadastro_usuario:
nome = input ("Digite  Usuario: ")
cpf= int(input("Digite  CPF: "))
senha = int(input("Digite Senha: "))

def senha_nome():
  senha = 1234
  if senha == """
"""while True:
    palavra_chave = input("DIgite sua senha")
    if senha == 1234:
        print ("Parabens senha correta")
    else:
      return("Senha Incorreta")"""
 
"""cadastro_usuario = input("Usuário: ") 
def registrar_senha(): 
  cadastro_senha = input("senha: ") 
print("Cadatro realizado com sucesso!") 
print("Entre com seu usuário e senha!") 
usuario = input("Usuário: ") 
senha = input("Senha: ")"""

def cadastrar_usuario():
  nome = input(" Digite seu Nome: ")
  cpf = input(" Digite seu CPF:")
  senha = input(" DIgite sua senha:")
  return nome, cpf, senha
  
def login(usuarios):
  cpf = int(input(" Digite seu CPF:"))
  senha = int(input(" Digite sua Senha:"))
  
  for usuario in usuarios:
    if cpf == usuario[1] and senha == usuario[2]:
      print("login feito com sucesso!")
      return True
  print("CPF ou senha incorretos. Tente novamente.")
  return False

def main():
  usuarios = []
  while True:
    print("1. Cadastrar Usuário")
    print("2. Fazer Login")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
      novo_usuario = cadastrar_usuario
      if len(novo_usuario[1]) == 11 and novo_usuario[1].isdigit():
        usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso!")
      else:
        print("CPF inválido. O CPF tem que ser apenas números e 11 digitos!")
    
    elif opcao == "2":
      if login(usuarios):
         break
      
    elif opcao == "3":
      print("Saindo...") 
      break
    
    else:
      print("Opçaõ Inválida!")

main()