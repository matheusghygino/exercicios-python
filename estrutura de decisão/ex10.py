"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno = input("Qual turno você estuda?\n Digite (M) para matutino, (V) para vespertino ou (N) para noturno: ").upper().strip()

while turno != "M" and turno != "V" and turno != "N":
    turno = input("Valor inválido! Digite (M) para matutino, (V) para vespertino ou (N) para noturno:  ").upper().strip()
    
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")

