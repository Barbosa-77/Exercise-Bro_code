username = input("Digite seu nome \n")
length = len(username)

if len(username) > 12:
    print ("Mais que 12")
elif not username.find (" ") == -1:
    print("Seu nome de usuario nao pode conter espaco")
elif not username.isalpha():
    print ("Nao pode conter digitos")
else:
    print (f"Bem vindo {username}")



#if length >= 12:
    #print("Tem mais de 12 caracteres")