'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''
medias = []
n = 0
media = 0
soma = 0
alunos = 0
for i in range(4):
    for  i in  range(4):
        nota = float(input(f"Digite a {i+1} nota: "))
        while nota > 10 or nota < 0:
            nota = float(input("Digite um valor entre 0 e 10: "))
        soma += nota
    media = soma / 4
    
    soma = 0
    
    if media >= 7:
        medias.append(media)
        alunos += 1
print(f'O número de alunos que tirou média acima d 7 foi: {alunos}')