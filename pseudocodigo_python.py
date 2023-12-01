import sys
lista_usuarios = {}

def função_cadastro(): #Lari Araújo
     """Função responsavel por procurar se o usuário já esta cadastrado ou não no aplicativo, se cadastrado segue para as perguntas,
        se não, necessário fazer o cadastro"""
     print("\n_Primeiro iremos verificar seu cadastro!\n")
     cadastro = {}
     cadastro["cpf"] = input("Por favor, digite seu CPF: \n")  
     if continuar_cadastro(cadastro) == True:
          cadastro["nome"] = input("Informe seu nome: \n")
          cadastro["email"] = input("Agora, digite seu email: \n")
          cadastro["telefone"] = input("Informe o telefone para contato: \n")
          cadastro["respostas"] = []
          criar_novo_cadastro(cadastro)
     return lista_usuarios[cadastro["cpf"]]
     
 
def continuar_cadastro(cadastro):
     if cadastro["cpf"] in lista_usuarios:
          edit = input("Você já está cadastrado. \n Digite 1 para editar o cadastro ou 2 para prosseguir.\n")
          return (edit == "1")
     return True

def criar_novo_cadastro(cadastro):
     lista_usuarios[cadastro["cpf"]] = cadastro

def perguntas_iniciais(cpf):#Lari Araújo
     """Função responsavel por fazer as perguntas de check-in e retornar uma lista que armazena as respostas"""
     print("\nPor favor, responda algumas perguntas para avaliarmos seu estado de saude.\n")

     per1 = int(input("De 0 a 5, sendo 0 muito baixo e 5 muito alto, como está sua saúde mental ultimamente? "))
     while per1 not in range(0,6):
          per1 = int(input("\nPor favor, dê uma nota de 0 a 5.\nComo está sua saúde mental ultimamente? "))
     if per1 <= 3:
          avaliacao_saudemental(cpf)

     per2 = int(input("De 0 a 5, sendo 0 muito baixo e 5 muito alto, como está sua saúde física ultimamente? "))
     while per2 not in range(0,6):
          per2 = int(input("Por favor, dê uma nota de 0 a 5.\nComo está sua saúde física ultimamente? "))
     if per2 <= 3:
          avaliacao_saudefisica(cpf)
     lista_usuarios[cpf]["perguntas"].extend(per1, per2)
     print(lista_usuarios)


def avaliacao_saudemental(cpf):#Luna
     """Função responsavel por fazer perguntas voltadas a saúde mental e se necessário retorna a função de recomendar especialista"""

     per1 = input("Em um nível de 0 a 5, sendo 0 muito baixo e 5 muito alto, como está seu nível de estresse ultimamente?")
     # per1.append(LISTA DE SAUDE MENTAL)
     while per1 not in ["0","1","2","3","4","5"]:
          per1 = input("Por favor, dê uma nota de 0 a 5")

     per2 = input("Baseado nessa resposta, tem mais de uma semana que você está se sentindo assim? Responda 'sim' ou 'não'")
     while per2.lower() not in ["sim","não","nao"]:
          per2 = input("Por favor, digite 'sim' ou 'não'")

     per3 = input("Você já faz terapia? Responda 'sim' ou 'não'")
     while per3.lower() not in ["sim","não","nao"]:
          per3 = input("Por favor, responda 'sim' ou 'não'")
     
     lista_usuarios[cpf]["perguntas"].append(int(per1))
     print(lista_usuarios)

     if (int(per1) >= 3) and (per2.lower() == "sim"):
          return recomendar_especialista
     else:
          return "Muito obrigada por preencher a avaliação de saúde mental!"


def avaliacao_saudefisica(cpf):#Luna
     """Função responsavel por fazer perguntas voltadas a saúde mental e se necessário retorna a função de recomendar especialista"""
     per3 = ""

     per1 = input("Você está sentindo dor atualmente? Responda 'sim' ou 'não'")
     while per1.lower() not in ["sim","não","nao"]:
          per1 = input("Por favor, digite 'sim' ou 'não'")

     if per1.lower() == "sim":
          per2 = input("Em um nível de 0 a 5, sendo 0 muito baixo e 5 muito alto, como está o nível dessa dor?")
          while per2 not in ["0","1","2","3","4","5"]:
               per2 = input("Por favor, dê uma nota de 0 a 5")
          
          lista_usuarios[cpf]["perguntas"].append(per2)
          print(lista_usuarios)
          
          per3 = input("Baseado nessa resposta, tem mais de uma semana que você está se sentindo assim? Responda 'sim' ou 'não'")
          while per3.lower() not in ["sim","não","nao"]:
               per3 = input("Por favor, responda 'sim' ou 'não'")
          
     per4 = input("Você prática algum tipo de atividade física? Responda 'sim' ou 'não'")
     while per4.lower() not in ["sim","não","nao"]:
          per4 = input("Por favor, digite 'sim' ou 'não'")
     
     if (per1.lower() == "sim") and (per3.lower() == "sim"):
          return recomendar_especialista()
     else:
          return "Muito obrigada por preencher a avaliação de saúde física!"




def mediadassaudes():#Lari Lopes
    """Função armazena os conteúdos da avaliação da saúde mental e saúde fisica, calcula uma média entre os dois e printa
     o resultado com uma mensagem"""
    pass


def recomendar_especialista():#Lari Lopes
    """A Função recomenda um especialista a partir do resultado das avaliações de saúde mental e física (separadas), """
    print("batata")




