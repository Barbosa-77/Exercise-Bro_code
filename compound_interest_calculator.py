# Python compound interest calculator

#principle, float
# rate, float
# time, years

principle = 0
rate = 0
time = 0 

while principle <= 0:
    principle = float(input("Type the value of Principle: "))
    if principle<= 0:
     print("Principle cannot be equals or lower than 0")
    
while rate <= 0:
    rate = float(input("Type the value of Rate: "))
    if rate<= 0:
     print("Rate cannot be equals or lower than 0")

while time <= 0:
    time = int(input("How many years? "))
    if principle<= 0:
     print("Time cannot be equals or lower than 0")

final = principle * pow((1 + rate/100), time)

print(f"The final amount will be {final:.2f} after {time} year/s")