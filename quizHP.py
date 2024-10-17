import random

def fazer_pergunta(pergunta, resposta_correta):
    print(pergunta)
    resposta = input("\n\nResposta: ").upper()
    if resposta == resposta_correta:
        print("Acertou!\n")
        return 1
    else:
        print("Que pena, errou!\n")
        return 0


print("Seja bem vindo(a)!")
answer_user = input("Quer começar? (S/N) \n").upper()

if answer_user != "S":
    print("\nNos vemos em outro momento, até mais.")
    quit()

print("Então vamos lá!\n")

score = 0

perguntas = [
    ("Qual o nome do melhor amigo do Harry Potter? \n(A) Draco Malfoi \n(B) Ron Weasley \n(C) Dino Thomas \n(D) Cedrico Diggory", "B"),
    ("Qual a casa do Harry? \n(A) Grifinória \n(B) Lufa-Lufa \n(C) Corvinal \n(D) Sonserina", "A"),
    ("Qual o nome da coruja do Harry? \n(A) Hélio \n(B) Agoureiro \n(C) Edwiges \n(D) Dobby", "C"),
    ("Qual é o mascote da Sonserina? \n(A) Leão \n(B) Texugo \n(C) Águia \n(D) Serpente", "D"),
    ("Para enxergar um Testrálio, o que um bruxo precisa presenciar? \n(A) Primeiro feitiço de um bruxo \n(B) Uma morte \n(C) Um deslizamento de terra \n(D) Um parto", "B"),
    ("Onde Harry Potter nasceu? \n(A) Godric's Hollow \n(B) Little Whingeing \n(C) Universidade de Oxford \n(D) Londres", "A"),
    ("Qual o nome da poção responsável por trazer sorte a quem a bebe? \n(A) Veritaserum \n(B) Amortentia \n(C) Polissuco \n(D) Felix Felicis", "D"),
    ("Qual o nome da poção do 'amor'? \n(A) Veritaserum \n(B) Amortentia \n(C) Polissuco \n(D) Felix Felicis", "B")
]

# Embaralhar as perguntas
random.shuffle(perguntas)

# Apresentar as perguntas embaralhadas
for pergunta, resposta_correta in perguntas:
    score += fazer_pergunta(pergunta, resposta_correta)

# Resultado final
print(f"Você chegou até o fim, parabéns! Sua pontuação foi {score}/{len(perguntas)}.")
