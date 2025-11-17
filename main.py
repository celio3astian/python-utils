# ---------------------------------------------------------
#   Python Utilities - Pequenos utilitários em Python
#   Autor: Célio Bastian
#   Funções: Calculadora, conversor e manipulação de dados
# ---------------------------------------------------------

def calculadora():
    print("\n--- Calculadora Simples ---")
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        print("\nOperações:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        op = input("\nEscolha a operação: ")

        if op == "1":
            resultado = n1 + n2
        elif op == "2":
            resultado = n1 - n2
        elif op == "3":
            resultado = n1 * n2
        elif op == "4":
            if n2 == 0:
                return print("\nErro: divisão por zero!")
            resultado = n1 / n2
        else:
            return print("\nOperação inválida!")

        print(f"\nResultado: {resultado}\n")

    except ValueError:
        print("\nErro: você deve digitar números válidos!\n")


def conversor_temperatura():
    print("\n--- Conversor de Temperatura ---")
    try:
        celsius = float(input("Digite a temperatura em °C: "))
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        print(f"\nFahrenheit: {fahrenheit:.2f} °F")
        print(f"Kelvin: {kelvin:.2f} K\n")

    except ValueError:
        print("\nErro: digite um valor numérico!\n")


def manipulacao_dados():
    print("\n--- Manipulação de Dados ---")
    print("Digite valores separados por vírgula (ex: 10, 20, 30):")

    try:
        entrada = input("Valores: ")
        lista = [float(x) for x in entrada.split(",")]

        media = sum(lista) / len(lista)
        maior = max(lista)
        menor = min(lista)

        print(f"\nQuantidade de itens: {len(lista)}")
        print(f"Média: {media:.2f}")
        print(f"Maior valor: {maior}")
        print(f"Menor valor: {menor}\n")

    except ValueError:
        print("\nErro: digite apenas números separados por vírgula!\n")


def menu():
    while True:
        print("\n=============== MENU ===============")
        print("1 - Calculadora")
        print("2 - Conversor de temperatura (°C → °F / K)")
        print("3 - Manipulação de dados (lista)")
        print("0 - Sair")
        print("====================================")

        escolha = input("Selecione uma opção: ")

        if escolha == "1":
            calculadora()
        elif escolha == "2":
            conversor_temperatura()
        elif escolha == "3":
            manipulacao_dados()
        elif escolha == "0":
            print("\nEncerrando o programa... Até a próxima!")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


# Executa o programa
if __name__ == "__main__":
    menu()
