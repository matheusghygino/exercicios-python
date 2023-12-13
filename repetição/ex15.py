"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo."""

"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo."""

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1
if (n==1) or (n==2):
    print("1")
    print("1")
else:
    print("1")
    print("1")
    for i in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        i += 1
        print(termo)
