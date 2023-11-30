import sys
dados_pacientes = {}
def menu(): #Lari Aráujo
    """Função principal de menu que irá chamar as outras funções do código, variaveis para armazenar funções"""
    while True:
        print("\nOlá, Bem vindo ao FelizIdade!")
	dados = função_cadastro()
    #opção1 = perguntas_iniciais()
    #    se saude_mental < 3
    #        opção2 = avaliação_saudemental()
    #        retorna input saude_fisica
    #    se não 
    #        usuário escolhe responder
    #        retorna input_fisica
    #    se saude_fisica < 3
    #        opção3 = avaliação_saudefisica
    #    se não 
    #        usuário escolhe respoder 
    #media = mediadassaudes()
    #imc = calculo_imc()
    #recomendação = recomendar_especialista()

    #print finalizar
    #    input sim ou não
    pass



def função_cadastro(): #Lari Araújo    
    """Função responsavel por procurar se o usuário já esta cadastrado ou não no aplicativo, se cadastrado segue para as perguntas,
        se não, necessário fazer o cadastro"""
    print("\n_Primeiro iremos verificar seu cadastro!\n")
    cadastro = {}
    cadastro["nome"] = input("Por favor, digite seu nome: \n")  
    if continuar_cadastro(contato) == True:  
        cadastro["email"] = input("Informe seu e-mail corporativo: \n")
        cadastro["cargo"] = input("Agora, digite seu cargo: \n")
        cadastro["empresa"] = input("Informe o nome da empresa: \n")
        cadastro["telefone"] = input("Informe o telefone para contato: \n")
        cadastro["num_funcionarios"] = ""  
        while (cadastro["num_funcionarios"] not in ["1","2","3","4","5","6"]):
            cadastro["num_funcionarios"] = input("Informe a quantidade de funcionários: \n 1 - de 1 a 50 funcionários.\n 2 - de 51 a 300 funcionários.\n 3 - de 301 a 1000 funcionários.\n 4 - de 1001 a 2000 funcionários. \n 5 - acima de 2001 funcionários. \n 0 - Encerrar aplicação\n")
            if cadastro["num_funcionarios"] == "0":
                encerrar()
        return cadastro
    else: 
    return dados_pacientes[cadastro["nome"]]
        
	#input cpf
		#se cpf está em {cadastro}
			#retorna lista_usuario
		#se não
            #input dados 
		#lista_usuario

def continuar_cadastro(contato):
  if cadastro["nome"] in dados_pacientes:
    edit = input("Encontramos seu cadastro. \n Digite 1 para editá-lo ou 2 para prosseguir.\n")
    return (edit == "1")
  return True

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




