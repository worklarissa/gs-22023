def menu(): #Lari Aráujo
    """Função principal de menu que irá chamar as outras funções do código, variaveis para armazenar funções"""
	dados = função_cadastro()
    opção1 = perguntas_iniciais()
        se saude_mental < 3
            opção2 = avaliação_saudemental()
            retorna input saude_fisica
        se não 
            usuário escolhe responder
            retorna input_fisica
        se saude_fisica < 3
            opção3 = avaliação_saudefisica
        se não 
            usuário escolhe respoder 
    media = mediadassaudes()
    imc = calculo_imc()
    recomendação = recomendar_especialista()

    print finalizar
        input sim ou não
    pass



def função_cadastro(): #Lari Araújo
    """Função responsavel por procurar se o usuário já esta cadastrado ou não no aplicativo, se cadastrado segue para as perguntas,
        se não, necessário fazer o cadastro"""
	input cpf
		se cpf está em {cadastro}
			retorna lista_usuario
		se não
            input dados 
			return lista_usuario
    pass


def perguntas_iniciais():#Lari Araújo
    """Função responsavel por fazer as perguntas de check-in e retornar uma lista que armazena as respostas"""
	input saude_mental
    input saude_fisica
    retorna lista_saudefisicamental #as informações das perguntas iniciais devem estar associadas ao repectivo usuário que respondeu
    pass    


def avaliacao_saudemental():#Luna
    """Função responsavel por fazer perguntas voltadas a saúde mental e se necessário retorna a função de recomendar especialista"""
    per1 = input("Em um nível de 0 a 5, sendo 0 muito baixo e 5 muito alto, como está seu nível de estresse ultimamente?")
    while per1 != int:
         return("Por favor, dê uma nota de 0 a 5")
    per2 = input("Baseado nessa resposta, tem mais de uma semana que você está se sentindo assim? Responda 'sim' ou 'não'")
    while per2 != "sim" or "não":
         return("Por favor, digite 'sim' ou 'não'")
    per3 = input("Você já faz terapia? Responda 'sim' ou 'não'")
    while per3 != "sim" or "não":
         return("Por favor, responda 'sim' ou 'não'")
    
    if per1 <= 3 and per2 == "sim":
         return recomendar_especialista
    else:
         return "Muito obrigada por preencher a avaliação de saúde mental!"
    

    pass


def avaliacao_saudefisica():#Luna
    """Função responsavel por fazer perguntas voltadas a saúde mental e se necessário retorna a função de recomendar especialista"""
    per1 = input("Você está sentindo dor atualmente? Responda 'sim' ou 'não'")
    while per1 != "sim" or "não":
         return("Por favor, digite 'sim' ou 'não'")
    if per1 == "sim":
        per2 = input("Em um nível de 0 a 5, sendo 0 muito baixo e 5 muito alto, como está o nível dessa dor?")
        while per2 != int:
             return("Por favor, dê uma nota de 0 a 5")
        per3 = input("Baseado nessa resposta, tem mais de uma semana que você está se sentindo assim? Responda 'sim' ou 'não'")
        while per3 != "sim" or "não":
             return("Por favor, responda 'sim' ou 'não'")
    per4 = input("Você prática algum tipo de atividade física? Responda 'sim' ou 'não'")
    while per4 != "sim" or "não":
         return("Por favor, digite 'sim' ou 'não'")
    
    if per1 == "sim" and per3 == "sim":
         return recomendar_especialista
    else:
         return "Muito obrigada por preencher a avaliação de saúde física!"
    
    pass


def mediadassaudes():#Lari Lopes
    """Função armazena os conteúdos da avaliação da saúde mental e saúde fisica, calcula uma média entre os dois e printa
     o resultado com uma mensagem"""
    pass


def recomendar_especialista():#Lari Lopes
    """A Função recomenda um especialista a partir do resultado das avaliações de saúde mental e física (separadas), """
    pass




