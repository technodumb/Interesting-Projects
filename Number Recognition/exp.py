import math


series = 0

x = int(input())
for i in range(x):
    series += (-1)**i*(1/(i+1)) 

print(series, math.log(2))
