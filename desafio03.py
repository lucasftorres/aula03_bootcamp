### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

#1 Solicita ao usuario que digite seu nome
# Usuario pode inserir o nomer não válido utilizando numeros ou simbolos ou vazio

nome_valido = False
salario_valido = False
bonus_valido = False


while not nome_valido:
    try:
        nome = input("Digite seu nome aqui: ") 

        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio!")
            exit()
        elif not all(char.isalpha() for char in nome):
            raise ValueError('Você digitou um valor inválido, por favor informe um nome alfabetico!')
            exit()
        else:
            print(f'Nome valido: {nome}')
            nome_valido = True

    except ValueError as e:
        print(e)
        exit()


#2 Solicita ao usuario que digite o valor do seu salario
# Converte o valor para float
# O usuario pode inserir um valor não numérico ou negativo, em ultimo caso zero, mas há a possibilidade de não ter salario fixo e sim remnuneração por comissão que seria o bônus.

while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salario: "))

        if salario <= 0:
            raise ValueError('Voce digitou um valor menor ou igual a zero para salario!')
            exit()
        else:
            salario_valido = True
    except ValueError as e:
        print(e)
        exit()



#3 Solicita ao usuario que digite o valor do bonus recebido
# O usuario inserir um valor não numérico ou negativo ou zero, que por ultimo iria zerar toda a remuneração se o usuario também receber salario fixo

while not bonus_valido:
    try:

        bonus = float(input("Digite o valor do seu bônus: "))
        if bonus <= 0:
            raise ValueError('Voce digitou um valor menor ou igual a zero para bonus!')
            exit()
        else:
            bonus_valido = True
    except ValueError as e:
        print(e)
        exit()

#4 Calcule o valor do bonus final
# O valor do Bonus zerar a remuneração, ou o usuario inserir um salario com valor <= -1000
bonus_final = (1000 + salario) * bonus

#5 Imprima o calculo de KPI do usuario
# O Resultado dos itens anteriores podem zerar a remuneração ou gerar um soma de tipos de dados errados.
print(f"O calculo de KPI eh: ({float(1000)} + {salario}) * {bonus}")

#6 Imprima o nome do usuario e o valor do bonus final
# O resultado dos itens anteriores gerar um impressão incorreta
print(f"Nome: {nome}, Bônus Final: {bonus_final:.2f}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?