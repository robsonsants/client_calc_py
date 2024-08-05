# Cliente REST para API de Calculadora

Este é um cliente REST escrito em Python para interagir com uma API de calculadora. Ele lista as operações disponíveis no servidor e realiza operações aritméticas básicas como soma, subtração, multiplicação e divisão.

## Visão Geral

O cliente se comunica com o servidor de calculadora hospedado em [calculadora-fxpc.onrender.com](https://calculadora-fxpc.onrender.com). As operações disponíveis são:

- Soma
- Subtração
- Multiplicação
- Divisão

## Requisitos

- Python 3.x
- Biblioteca `requests`

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/robsonsants/client_calc_py.git
   cd client_calc_py

2. Instale as dependências necessárias:

     ```bash
    pip install requests

## Uso
O script cliente_calculadora.py pode ser executado diretamente para listar operações e realizar cálculos.

##Listar Operações
A função listar_operacoes() envia uma requisição GET para o servidor e imprime as operações disponíveis.

##Realizar Operação
A função realizar_operacao(operacao, param1, param2) envia uma requisição POST para realizar a operação especificada. Os parâmetros param1 e param2 são os números nos quais a operação será realizada.

## Executar o Script
Para executar o script, basta rodar o seguinte comando no terminal:

    python cliente_calculadora.py

## Exemplo de Saída

```bash

Request Status Code (realizar_operacao): 200
Response Content: {"result":8.0}

Resultado da soma: {'result': 8.0}
Request Status Code (realizar_operacao): 200
Response Content: {"result":6.0}

Resultado da subtração: {'result': 6.0}
Request Status Code (realizar_operacao): 200
Response Content: {"result":42.0}

Resultado da multiplicação: {'result': 42.0}
Request Status Code (realizar_operacao): 200
Response Content: {"result":5.0}

Resultado da divisão: {'result': 5.0}

## Estrutura do Código
- listar_operacoes: Envia uma requisição GET para obter as operações disponíveis.
- realizar_operacao: Envia uma requisição POST para realizar uma operação específica (soma, subtração, multiplicação ou divisão).
- main: Função principal que executa o fluxo de listagem de operações e realiza algumas operações de exemplo.

