x = int(input("Insert number of elements in the series: "))


y = 1
z = 0
sum1 = 0

while z < x:
    sum1 += y
    y = y/-2
    z += y
print(sum1)
