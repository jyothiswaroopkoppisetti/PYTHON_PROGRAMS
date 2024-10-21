# simple interest
def simpleinterest(p,r,t):
    si = (p * r * t) / 100
    print("Simple Interest", si)

p = 100000
r = 5
t = 5

simpleinterest(p,r,t)

# area and perimeter of rectangle



def areaofrectangle(l,w):
    area = l * w
    print("area", area)

def perimeterofrectangle(l,w):
    perimeter = 2 * (l + w)
    print("Perimeter", perimeter)

l = 2.4
w = 5

areaofrectangle(l,w)
perimeterofrectangle(l,w)




# temperature c to f

def convert_c_to_f(c):
    f = (c * 1.8) + 32
    print(f)

c = 36.8

convert_c_to_f(c)

#write a python to compute spead using s=ut+1/2at2 using functions
def compute_speed(u,t,a):
    s = (u * t) +(0.5 * a * (t**2))
    print("speed:",s)
initial_velocity = 100
acceleration = 40
time = 20

compute_speed(initial_velocity, time, acceleration)


#write a python program to calculate BMI (body mass index) using functions concept
#formula BMI=weight in kgs/(height in meters)2

def bodymassindex(weight, height):
    BMI = weight / height**2
    print("body mass index of given height:", height,"weight:", weight, "is", BMI)

weight = 65
height = 1.6
bodymassindex(weight, height)
