import requests

# URL do servidor
BASE_URL = "https://calculadora-fxpc.onrender.com"

# Função para listar todas as operações disponíveis no servidor
def listar_operacoes():
    response = requests.get(f"{BASE_URL}/operations")
    print(f"Request Status Code (listar_operacoes): {response.status_code}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Erro ao listar operações")

# Função para realizar uma operação ( que pode ser soma, subtração, multiplicação e divisão)
def realizar_operacao(operacao, param1, param2):
    path = f"/operation/{operacao}/{param1}/{param2}"
    response = requests.post(f"{BASE_URL}{path}")
    print(f"Request Status Code (realizar_operacao): {response.status_code}")
    print(f"Response Content: {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao realizar operação {operacao}: {response.text}")

# Função principal para execução do código
def main():
    try:
        operacoes = listar_operacoes()
        print("Operações disponíveis:", operacoes)

        resultado = realizar_operacao("soma", 5, 3)
        print("Resultado da soma:", resultado)

        resultado = realizar_operacao("subtracao", 10, 4)
        print("Resultado da subtração:", resultado)

        resultado = realizar_operacao("multiplicacao", 6, 7)
        print("Resultado da multiplicação:", resultado)

        resultado = realizar_operacao("divisao", 20, 4)
        print("Resultado da divisão:", resultado)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
