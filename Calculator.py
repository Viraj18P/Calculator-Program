'''Calculator Program by Viraj Samir Patel-EE240002079'''

def addition(a,b):
    print(a+b)
def multiplication(a,b):
    print(a*b)
def addition(a,b):
    print(a+b)
def division(a,b):
    print(a/b)
def subtraction(a,b):
    print(a-b)

def fact(n):
    result=1
    for i in range (1,n+1):
        result*=i
    return result

def log(x):

    
    m=1
    loge=0

    while x>2:
        x=x/2
        loge=loge+0.69315


    for i in range (1,10000,1):
        loge=loge+(pow((x-1),i)/i)*m
        m=m*(-1)
        
    print(loge)



ask=input("Which operation do you want to perform from: addition/subtraction/multiplication/division/sine/cos/tan/log/quadratic/LinearEqnVar2? (Enter exact operation name as above)")


if ask=="addition" :
    enter1=int(input("Enter your first number:"))
    enter2=int(input("Enter your second number:"))
    print(addition(enter1,enter2))

if ask=="multiplication" :
    enter1=int(input("Enter your first number:"))
    enter2=int(input("Enter your second number:"))
    print(multiplication(enter1,enter2))

if ask=="division" :
    enter1=int(input("Enter your first number:"))
    enter2=int(input("Enter your second number:"))
    if enter2==0:
        print("Can't divide by 0")
    else:   
        print(division(enter1,enter2))
    

if ask=="subtraction" :
    enter1=int(input("Enter your first number:"))
    enter2=int(input("Enter your second number:"))
    print(subtraction(enter1,enter2))



if ask=="sine":
    a=int(input("Enter number (in radians):"))
    sin=a
    m=-1
    for i in range(3,1000,2):
        sin=sin+(pow(a,i)/fact(i)*m)
        m=m*(-1)
    print(sin)

if ask=="log":
    x=int(input("Enter value:x (for log(x))"))
    print(log(x))



if ask=="quadratic":
    
    a=int(input("Enter quadratic eqn x^2 coeff:"))
    b=int(input("Enter quadratic eqn x coeff:"))
    c=int(input("Enter quadratic eqn constant:"))
    root1= (-b/(2*a))+(((b*b-4*a*c))**0.5)/(2*a)
    root2= (-b/(2*a))-(((b*b-4*a*c))**0.5)/(2*a)
    print("The solutions of the quadratic eqn are:",root1,root2)

if ask==("cos"):

    a=int(input("Enter value(in radians):"))
    cos=1
    m=-1
    for i in range(2,1000,2):
        cos=cos+(pow(a,i)/fact(i))*m
        m=m*(-1)
    print(cos)

if ask==("tan"):

    a=int(input("Enter value:(in radians)"))
    cos=1
    m=-1
    for i in range(2,1000,2):
        cos=cos+(pow(a,i)/fact(i))*m
        m=m*(-1)
    
    sin=a
    m=-1
    for i in range(3,1000,2):
        sin=sin+(pow(a,i)/fact(i)*m)
        m=m*(-1)
    print(sin/cos)
    
if ask==("LinearEqnVar2"):
    print("For eqn of form ax+by+c=0 and dx+ey+f=0")
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    c=int(input("Enter value of c:"))
    d=int(input("Enter value of d:"))
    e=int(input("Enter value of e:"))
    f=int(input("Enter value of f:"))
    x=(b*f-c*e)/(a*e-b*d)
    y=(c*d-a*f)/(a*e-b*d)
    print("The value of x=",x)
    print("The value of y=",y)


    

    







