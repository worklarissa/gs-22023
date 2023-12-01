from pseudocodigo_python import*

def menu(): #Lari Aráujo
    """Função principal de menu que irá chamar as outras funções do código, variaveis para armazenar funções"""
    while True:
      print("\nOlá, Bem vindo ao FelizIdade!")
      dados = função_cadastro()
      print(f"Os dados de seu cadastro são: {dados}")
      perguntas_iniciais(dados["cpf"])
      mediadassaudes(dados["cpf"])
      
      #media = mediadassaudes()
      #imc = calculo_imc()
      #recomendação = recomendar_especialista()

      #print finalizar
      #    input sim ou não

if __name__ == "__main__":
  menu()

