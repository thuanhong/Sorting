import math
z = 200
y = 500
while z <= 300:
    y += math.sin((z%(500/250))*math.pi)
    z += 1
    print(z, y)
