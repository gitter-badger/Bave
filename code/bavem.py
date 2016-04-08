#<startsettings>#

#none

#</startsettings>#

#<calculatorfunctions>#

def addition(b,c):
    addition = (float(b)+float(c))
    return addition
def subtraction(b,c):
    subtraction = (float(b)-float(c))
    return subtraction
def multiplication(b,c):
    multiplication = (float(b)*float(c))
    return multiplication
def division(b,c):
    division = (float(b)/float(c))
    return division

#</calculatorfunctions>#

#<converterfunctions>#

def celsius(f):
    celsius = (float((float(5)/float(9)) * float(float(f) - 32)))
    return celsius
def fahrenheit(g):
    fahrenheit = (float(float(g)/float(float(5)/float(9))) + float(32))
    return fahrenheit

#</converterfunction>#

#<velocityfunction>#

def velocity(i,j):
    velocity = (float(i)/float(j))
    return velocity
def distance(k,l):
    distance = (float(k) * float(l))
    return distance
def time(m,n):
    time = (float(m)/float(n))
    return time

#</velocityfunction>#

#<loopmultiplier>#

def loopmultiplier(o,q):
     w = 1 + int(q)
     j = 0
     for j in range(1,int(w)):
         value = (str(float(o)) + (" x ") + str(float(j)) + (" = ") + str(float(o)*float(j)))
         print(str(value))
     return value

#</loopmultiplier>#

#<CalculusWizardfunction>#

def degree(y,r):
    degrees = (float((float(float(y) * float(180)))/(float(r))))
    return degrees
def radians(z,r):
    radians = (float(float(float(z) * float(r))/float(180)))
    return radians

#</CalculusWizardfunctions>#

#<expro>#

def expro(a):
    exval = eval(str(a))
    fval = float(exval)
    return fval

#</expro>#

#<help function>#

def help():
    print ("")
    print (" bave <command>")
    print ("")
    print (" -h  displays this help message")
    print ("")
    print (" -a  adds two numbers")
    print ("")
    print (" -s  subtracts two numbers")
    print ("")
    print (" -m  multiplies two numbers")
    print ("")
    print (" -d  dividess two numbers")
    print ("")
    print (" -x  evaluates a full expression")
    print ("")
    print (" -l  dsiplays the license agreement")
    print ("")
    print (" -e  exits the console")
    print ("")
    print (" -i  displays information about this build of bave")
    print ("")

#</help function>#
