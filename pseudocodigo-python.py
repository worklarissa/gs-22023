função menu():
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



função função_cadastro:
	input cpf
		se cpf está em {cadastro}
			retorna lista_usuario
		se não
            input dados 
			return lista_usuario

função perguntas_iniciais():
	input saude_mental
    input saude_fisica
    retorna lista_saudefisicamental #as informações das perguntas iniciais devem estar associadas ao repectivo usuário que respondeu
        

função avaliação_saudemental():
        input 

função avaliação_saudefísica():

função mediadassaudes():

função calculo_imc():

função recomendar_especialista():




