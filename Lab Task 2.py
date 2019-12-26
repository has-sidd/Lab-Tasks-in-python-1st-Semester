#Q1
radius = [0.5, 1, 2]
speed = 10
for i in range(3):
    velocity = speed * radius[i]
    print("Linear Velocity is ", velocity, " meter/second at radius ", radius[i], "m")

print()
#Q2
radius = [0.05, 0.1]
av = 523.3
for i in range(2):
    lv = radius[i] * av
    print("Linear velocity at radius ", radius[i], "m is :", lv, "m/s")

print()
#Q3
radius = 0.3
velocity = 10
speed = velocity / radius
print("Angular Velocity is : ", speed, "radians/second")

