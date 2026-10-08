temperature = float(input("Digite uma temperatura:"))

unit = input("A temperatura esta em Celcius ou em Farenheit (C/F):\n")

if unit == "C" :
    temperature = (temperature* 9/5 + 32)
    unit = "Farenheit"
    unit2 = "F" 
elif unit == "F" or "f":
    temperature = (temperature - 32) / (9/5)
    unit = "Celsius"
    unit2 = "C"

print(f"Convertida em {unit} sera {round(temperature, 1)} {unit2}.")