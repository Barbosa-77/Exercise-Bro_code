#Python quiz

perguntas = ("Qual é o Pokémon inicial do tipo Fogo na região de Kanto?",
             "Qual Pokémon é o mascote mais famoso da franquia?",
             "Em qual Pokémon o Magikarp evolui?",
             "Qual Pokémon é conhecido por dormir muito e ser bem grande e pesado?",
             "Qual é o nome do aparelho que os treinadores usam para capturar Pokémon?")

alternativas = (("A. Squirtle ","B. Bulbasaur ","C. Charmander ","D. Pikachu "),("A. Eevee ","B. Meowth ","C. Pikachu ","D. Jigglypuff "),("A. Blastoise ","B. Lapras ","C. Dragonite ","D. Gyarados "),("A. Snorlax ","B. Geodude ","C. Onix ", "D. Psyduck "),("A. Pokegear ","B. Pokebola ","C. Pokedex ","D. Pokefone "))

resp_correta = ("C", "C", "D", "A", "B")

resp_usuario = []

pontos = 0
numero_ques = 0

for pergunta in perguntas:
    print()
    print(40*"--")
    print(f"{pergunta}\n")
    for alternativa in alternativas[numero_ques]:
        print(alternativa)

    resposta = input("\nDigite (A, B, C, D): ").upper()
    resp_usuario.append(resposta)

    if resposta == resp_correta[numero_ques]:
        pontos = pontos + 1
        print("Correto!!")
    else:
        print("Resposta errada!")
        print(f"A resposta correta era {resp_correta[numero_ques]}")

    numero_ques += 1


print("----------------------")
print("      Resultado       ")
print("----------------------")

print("\nRespostas certas: ", end= "")
for r in resp_correta:
    print(r, end=" ")
print()

print("Suas respostas: ", end= "")
for c in resp_usuario:
    print(c, end=" ")
print()

pontos = int((pontos / len(perguntas)) * 100)

print(f"\nVoce acertou um total de {pontos}% das questoes")