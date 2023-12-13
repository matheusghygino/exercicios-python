"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

print("Vamos criar um usuario e senha para você!")
user = input("Digite seu usuário: ")
password = input("Digite sua senha: ")

while user == password:
    print("O usuário e a senha não podem ser iguais! Digite novament!")
    user = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

if user != password:
    print("Usuário criado com sucesso!")