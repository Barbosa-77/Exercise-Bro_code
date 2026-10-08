import time


tempo = int(input("Digite quantos segundos quer de contagem "))

for i in (range (tempo, 1-1, -1)):
    seconds = i % 60
    minutes = (i//60) % 60
    hours = (i//3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Acabou o tempo!!")


"""
time.sleep(3)

print("Time's up")"""



86400