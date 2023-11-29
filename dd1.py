# fahrenheit

f = float(input("give f:"))

c = (f - 32) * 5 / 9

print("celsius: {:.2f}".format(c))


# euro

amount_foreign = float(input("give foreign amount:"))
rate_per_euro = float(input("give exchange rate (per euro):"))

amount_euro = amount_foreign / rate_per_euro

print("euros:{0:10.2f}".format(amount_euro))

#

amount_foreign = float(input("give foreign amount:"))
currency = input("give foreign amount:")

rates = { "USD" : 0.887, "GBP" : 1.33, "AUD" : 0.99 }

rate = rates[currency]


# fase overgangen

temp = int(input("give temp:"))

if temp < 0:
    print("vast")
elif temp == 0:
    print("smeltend")
elif temp < 100:
    print("vloeibaar")
elif temp == 100:
    print("kokend")
else:
    print("gas")


# gestructureerd

woord = "pindakaas"
for letter in woord:
    if letter == "k":
        break
    print(letter)
print("Einde programma")

woord = "pindakaas"
i = 0
while i < len(woord) and woord[i] != "k":
    print(woord[i])
    i += 1
print("Einde programma")


#min-max

import sys

values = []
for i in range(1, 6):
    values.append(float(input("enter value {}: ".format(i))))
sum = 0
min = sys.float_info.max
max = sys.float_info.min
for v in values:
    sum += v 	# gelijk aan sum = sum + v
    if v < min:
        min = v
    if v > max:
        max = v
print("min =", min)
print("max =", max)
print("sum =", sum)
print("avg =", sum / len(values))


# fibonacci

import sys

n = int(input("enter n:"))

if n < 1:
    print("n moet groter dan 0 zijn")
    sys.exit(1)
    
prev1 = 0
prev2 = 1
print(prev1, end=",")
print(prev2, end="")
for i in range(n - 2):
    print(",", end="")
    sum = prev1 + prev2    
    print(sum, end="")
    prev1, prev2 = prev2, sum

