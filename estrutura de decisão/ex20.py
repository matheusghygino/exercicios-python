"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10."""
    
print("Iremos analisar suas três notas e lhe informar se você foi aprovado ou não!")
n1 = float(input("Digite o valor da primeira nota: "))
n2 = float(input("Digite o valor da segunda nota: "))
n3 = float(input("Digite o valor da terceira nota: "))

media = (n1 + n2 + n3) / 3

if media == 10:
    print(f"Sua média foi {media:.2f}! Parabéns você foi aprovado com distinção!")
elif media >= 7 and media < 10:
    print(f"Sua média foi {media:.2f}! Parabéns você foi aprovado!")
elif media < 7:
    print(f"Sua média foi {media:.2f}! Você foi reprovado!")
elif media > 10 or media < 0:
    print("Digite um valor válido para as notas, o valor mínimo é 0 e o máximo 10")