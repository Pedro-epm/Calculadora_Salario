def calcular_imc():
    #ler dados
    peso = float(input("Informe o peso do usuário: ").replace(",", "."))
    altura = float(input("Informe a altura do usuário").replace(",", "."))
    #calcular imc
    imc = peso / (altura ** 2)
    #classificação imc
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5<= imc <= 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc <= 34.9:
        classificacao = "Obesidade Grau 1"
    elif 35 <= imc <= 39.9:
        classificacao = "Obesidade Grau 2"
    else:
        classificacao = "Obesidade Grau 3"
    return round(imc, 2), classificacao

def calcular_juros_compostos():
    #ler os dados
    capital_inicial = float(input("Informe o capital inicial da operação: "))
    juros = float(input("informe quantos % de juros: ").replace(",", ".")) / 100
    tempo = int(input("Informe quantos meses ").replace(",", "."))
    #calculo montante
    montante = capital_inicial *(( 1 + juros)**tempo)
    valor_juros = montante - capital_inicial
    return montante, valor_juros

def calcular_salario_liquido():
    bruto = float(input("Salário bruto R$: ").replace(",", "."))
    #calculo do valor inss
    if bruto < 1518:
      desconto_INSS = bruto * 0.075
    elif bruto <= 2793.88:
      desconto_INSS = bruto * 0.09
    elif bruto <= 4190.83:
      desconto_INSS = bruto * 0.12
    else:
      desconto_INSS = bruto * 0.14
    #calculo base irrf
    base_irrf = bruto - desconto_INSS
    if base_irrf <= 2428.80:
      desconto_irrf = 0
    elif base_irrf <= 2826.65:
      desconto_irrf = base_irrf * 0.075 - 182.16
    elif base_irrf <= 3751.05:
      desconto_irrf = base_irrf * 0.15 - 394.16
    elif base_irrf <= 4664.68:
      desconto_irrf = base_irrf * 0.225 - 675.49
    else:
      desconto_irrf = base_irrf * 0.275 - 908.73
    #calculo salario liquido
    plano_saude = float(input("Informe o valor do plano de saúde: ").replace(",", "."))
    salario_liquido = bruto - desconto_INSS - desconto_irrf - plano_saude
    return salario_liquido

def menu():
  print('''
  [1]Calcular IMC
  [2]Calcular juros
  [3]Calcular salario liquido
  [4]Sair
  ''')

#programa principal
while True:
  opcao = input(menu())
  if opcao == "1":
    imc, classificacao = calcular_imc()
    print(f"O seu IMC é {imc:.2f} {classificacao}")
  elif opcao == "2":
    montante, juros = calcular_juros_compostos()
    print(f"Seu montante é de {montante:.2f}")
    print(f"O juros foi de {juros:.2f}")
  elif opcao == "3":
    liquido = calcular_salario_liquido()
    print(f"O salario liquido foi de R$ {liquido:.2f}")
  elif opcao == "4":
    print("Encerrando o programa. Ate logo")
    break
  else:
    print("Opcao invalida! Tente novamente")



    

