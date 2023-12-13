"""Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';"""
    
name = input("Type your name: ")
while len(name) <= 3:
    name = input("Name must be more than 3 characters! Type again: ")
    
age = int(input("Type your age: "))
while age < 0 or age > 150:
    age = int(input("Age must be more than 0 and less than 150 years! Type again: "))
    
wage = float(input("Type your wage: "))

while wage < 0:
    wage = float(input("Wage must be higher than 0! Type your wage again: "))
    
gender = input("(F) for Female or (M) for Male): ").upper().strip()
while gender != "F" and gender != "M":
    gender = input("Invalid character! Type (F) for Female or (M) for Male): ").upper().strip()
    
marital_status = input("Type (S) for single, (M) for married, (W) for widower or (D) for divorced: ").upper().strip()
while marital_status != "S" and marital_status != "M" and marital_status != "W" and marital_status != "D":
    marital_status = input("Invalid character! Type (S) for single, (M) for married, (W) for widower or (D) for divorced: ").upper().strip()