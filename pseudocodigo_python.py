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
          criar_novo_cadastro(cadastro)
          return cadastro
     else:
          return lista_usuarios[cadastro["cpf"]]
 
def continuar_cadastro(cadastro):
     if cadastro["cpf"] in lista_usuarios:
          edit = input("Você já está cadastrado. \n Digite 1 para editar o cadastro ou 2 para prosseguir.\n")
          return (edit == "1")
     return True

def criar_novo_cadastro(cadastro):
     lista_usuarios[cadastro["cpf"]] = cadastro

def perguntas_iniciais():#Lari Araújo
    """Função responsavel por fazer as perguntas de check-in e retornar uma lista que armazena as respostas"""
	#input saude_mental
    #input saude_fisica
    #retorna lista_saudefisicamental #as informações das perguntas iniciais devem estar associadas ao repectivo usuário que respondeu
    pass    

def avaliacao_saudemental():#Luna
    """Função responsavel por fazer perguntas voltadas a saúde mental e se necessário retorna a função de recomendar especialista"""
    per1 = input("Em um nível de 0 a 5, sendo 0 muito baixo e 5 muito alto, como está seu nível de estresse ultimamente?")
    # per1.append(LISTA DE SAUDE MENTAL)
    while per1 not in ["0","1","2","3","4","5"]:
         return("Por favor, dê uma nota de 0 a 5")
    per2 = input("Baseado nessa resposta, tem mais de uma semana que você está se sentindo assim? Responda 'sim' ou 'não'")
    while per2 not in ["sim","Sim","SIM","não","nao","NÃO","NAO","Não","Nao"]:
         return("Por favor, digite 'sim' ou 'não'")
    per3 = input("Você já faz terapia? Responda 'sim' ou 'não'")
    while per3 not in ["sim","Sim","SIM","não","nao","NÃO","NAO","Não","Nao"]:
         return("Por favor, responda 'sim' ou 'não'")
    
    if per1 <= 3 and per2 == "sim" or "Sim" or "SIM":
         return recomendar_especialista
    else:
         return "Muito obrigada por preencher a avaliação de saúde mental!"
    
    return


def avaliacao_saudefisica():#Luna
    """Função responsavel por fazer perguntas voltadas a saúde mental e se necessário retorna a função de recomendar especialista"""
    per1 = input("Você está sentindo dor atualmente? Responda 'sim' ou 'não'")
    while per1 not in ["sim","Sim","SIM","não","nao","NÃO","NAO","Não","Nao"]:
         return("Por favor, digite 'sim' ou 'não'")
    if per1 == "sim":
        per2 = input("Em um nível de 0 a 5, sendo 0 muito baixo e 5 muito alto, como está o nível dessa dor?")
        #per2.append(LISTA DE SAUDE FISICA)
        while per2 not in ["0","1","2","3","4","5"]:
             return("Por favor, dê uma nota de 0 a 5")
        per3 = input("Baseado nessa resposta, tem mais de uma semana que você está se sentindo assim? Responda 'sim' ou 'não'")
        while per3 not in ["sim","Sim","SIM","não","nao","NÃO","NAO","Não","Nao"]:
             return("Por favor, responda 'sim' ou 'não'")
    per4 = input("Você prática algum tipo de atividade física? Responda 'sim' ou 'não'")
    while per4 not in ["sim","Sim","SIM","não","nao","NÃO","NAO","Não","Nao"]:
         return("Por favor, digite 'sim' ou 'não'")
    
    if per1 == "sim" or "Sim" or "SIM" and per3 == "sim" or "Sim" or "SIM":
         return recomendar_especialista
    else:
         return "Muito obrigada por preencher a avaliação de saúde física!"
    
    return


def mediadassaudes():#Lari Lopes
    """Função armazena os conteúdos da avaliação da saúde mental e saúde fisica, calcula uma média entre os dois e printa
     o resultado com uma mensagem"""
    pass


def recomendar_especialista():#Lari Lopes
    """A Função recomenda um especialista a partir do resultado das avaliações de saúde mental e física (separadas), """
    pass




