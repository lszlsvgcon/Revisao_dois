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
