import math

# array = [0,0,0,1,1,1,2,2,3,4,5,6,2,12,2,3,4,1,1,1,0,0,0]

# line1 = []
# line2 = []
# line3 = []

# for i in range(len(array)):
#     line3.append(".")
#     line2.append("." if array[i] > 0 else " ")
#     line1.append("." if array[i] > 2 else " ")

# print(''.join(line1))
# print(''.join(line2))
# print(''.join(line3))
# print(''.join(line2))
# print(''.join(line1))


radius = 10
diameter = radius * 2

for i in range(diameter + 1):
    for j in range(diameter + 1):
        # Multiply the horizontal difference by 2 to compensate for character aspect ratio
        dx = (j - radius) 
        dy = (i - radius)
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance < radius + 0.5:
            print(".", end="")
        else:
            print(" ", end="")
    print()