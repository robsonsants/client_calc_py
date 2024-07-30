import requests

# URL do servidor
BASE_URL = "https://calculadora-fxpc.onrender.com"

# Função para listar operações disponíveis
def listar_operacoes():
    response = requests.get(f"{BASE_URL}/operations")
    print(f"Request Status Code (listar_operacoes): {response.status_code}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Erro ao listar operações")

# Função para realizar uma operação
def realizar_operacao(operacao, param1, param2):
    path = f"/operation/{operacao}/{param1}/{param2}"
    response = requests.post(f"{BASE_URL}{path}")
    print(f"Request Status Code (realizar_operacao): {response.status_code}")
    print(f"Response Content: {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao realizar operação {operacao}: {response.text}")

# Função principal para executar o código
def main():
    try:
        # Listar operações disponíveis
        operacoes = listar_operacoes()
        print("Operações disponíveis:", operacoes)

        # Realizar uma operação (exemplo: soma de 5 + 3)
        resultado = realizar_operacao("soma", 5, 3)
        print("Resultado da soma:", resultado)

        # Realizar uma operação (exemplo: subtração de 10 - 4)
        resultado = realizar_operacao("subtracao", 10, 4)
        print("Resultado da subtração:", resultado)

        # Realizar uma operação (exemplo: multiplicação de 6 * 7)
        resultado = realizar_operacao("multiplicacao", 6, 7)
        print("Resultado da multiplicação:", resultado)

        # Realizar uma operação (exemplo: divisão de 20 / 4)
        resultado = realizar_operacao("divisao", 20, 4)
        print("Resultado da divisão:", resultado)
    except Exception as e:
        print(e)

# Executa a função main
if __name__ == "__main__":
    main()
