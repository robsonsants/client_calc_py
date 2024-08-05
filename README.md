# client_calc_py
The goal of this project is to implement a REST client in Python to consume a calculator API as specified by OpenAPI. The REST client interacts with the server to list available operations and perform basic calculations such as addition, subtraction, multiplication, and division. This activity helps you understand the communication between clients and servers in a RESTful architecture.

The Python client is designed to perform the following tasks:

List Available Operations:

Makes a GET request to https://calculadora-fxpc.onrender.com/operations.

Returns a list of operations supported by the API.

Perform Mathematical Operations:

Makes POST requests to perform operations such as addition, subtraction, multiplication, and division.

Example endpoint for sum: https://calculadora-fxpc.onrender.com/operation/sum/5/3.
