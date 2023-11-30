from pseudocodigo_python import*

def menu(): #Lari Aráujo
    """Função principal de menu que irá chamar as outras funções do código, variaveis para armazenar funções"""
    while True:
      print("\nOlá, Bem vindo ao FelizIdade!")
      dados = função_cadastro()
      print(f"Os dados de seu cadastro são: {dados}")
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

if __name__ == "__main__":
  menu()

