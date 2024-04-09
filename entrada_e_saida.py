#1 - Crie uma função que pede o nome do usuário e o imprime com uma saudação. Ao final desta tarefa faça um commit “Resolve questão 1”no repositório remoto.
#Exemplo de resultado: "Olá, [nome do usuário]! Seja bem-vindo(a)!"


def saudacao_usuario():
    nome = input("Digite o seu nome: ")
    print(f"Olá, {nome}! Seja bem-vindo(a)!")
saudacao_usuario()


#2 - Crie uma função que pede dois números, faz a soma deles e imprime o resultado. 
#Exemplo de saída: "A soma dos números é: [resultado] "


def somar_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"A soma dos números é: {resultado}")
somar_numeros()


#3 - Crie uma função que pede dois números, faz a multiplicação deles e imprime o resultado.
#Exemplo de saída: "O produto dos números é: [resultado] "


def multiplicacao_de_numeros():
    try:
        # Solicita os números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Calcula o produto dos números
        produto = num1 * num2
        
        # Imprime o resultado
        print(f"O produto dos números é: {produto}")
    except ValueError:
        print("Por favor, insira números válidos.")

# Chama a função
multiplicacao_de_numeros()


#4 - Crie uma função que pede um número, divide por 2 e imprime o resultado. 
#Exemplo de saída: "A divisão do número [numero] por dois é: [resultado] "


def divisao_por_dois():
    try:
        # Solicita um número ao usuário
        numero = float(input("Digite um número: "))
        
        # Realiza a divisão por 2
        resultado = numero / 2
        
        # Imprime o resultado
        print(f"A divisão do número {numero} por dois é: {resultado}")
    except ValueError:
        print("Por favor, insira um número válido.")

# Chama a função
divisao_por_dois()
