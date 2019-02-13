import math

a = float(input('Please enter the a coordinate of vertex 1: '))
b = float(input('Please enter the b coordinate of vertex 1: '))

c = float(input('Please enter the c coordinate of vertex 2: '))
d = float(input('Please enter the d coordinate of vertex 2: '))

e = float(input('Please enter the e coordinate of vertex 3: '))
f = float(input('Please enter the f coordinate of vertex 3: '))

v1 = [a, b]
v2 = [c, d]
v3 = [e, f]

side1 = math.sqrt(((v1[0]-v2[0])**2)+((v1[1]-v2[1])**2))
side2 = math.sqrt(((v1[0]-v3[0])**2)+((v1[1]-v3[1])**2))
side3 = math.sqrt(((v2[0]-v3[0])**2)+((v2[1]-v3[1])**2))

C = side1 + side2 + side3
hc = C/2

triangle_area = math.sqrt(hc*(hc-side1)*(hc-side2)*(hc-side3))


print('Your triangle area is: ')
print(round(triangle_area, 2))