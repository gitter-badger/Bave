#<startsettings>#

import bavem

#</startsettings>#

#<main>#

print ("")
print ("Bave")
print ("Type 'help' to view a list of commands.")
print ("")
cmd = raw_input("$>> ")

if cmd == "help":
    bavem.help()
    
elif cmd == "bave -h":
    bavem.help()

elif cmd == "bave -a":
    print("")
    a = raw_input("Type the first argument here: ")
    b = raw_input("Type the second argument here: ")
    c = bavem.addition(a,b)
    print (str(a) + " + " + str(b) + " = " + str(c))
elif cmd == "bave -s":
    print("")
    a = raw_input("Type the first argument here: ")
    b = raw_input("Type the second argument here: ")
    print("")
    c = bavem.subtraction(a,b)
    print (str(a) + " - " + str(b) + " = " + str(c))

elif cmd == "bave -m":
    print("")
    a = raw_input("Type the first argument here: ")
    b = raw_input("Type the second argument here: ")
    print("")
    c = bavem.multiplication(a,b)
    print (str(a) + " x " + str(b) + " = " + str(c))

elif cmd == "bave -d":
    print("")
    a = raw_input("Type the first argument here: ")
    b = raw_input("Type the second argument here: ")
    print("")
    c = bavem.division(a,b)
    print (str(a) + " / " + str(b) + " = " + str(c))

elif cmd == "bave -x":
    print("")
    a = raw_input("Type the expression here: ")
    print("")
    c = bavem.expro(a)
    print (str(a) + " = " + str(c))

elif cmd == "bave -l":
    print("")
    print ("This software is licensed under the GNU GPL v3.0.")

elif cmd =="bave -i":
    print ("")
    print ("BUILD INFO")
    print ("----------")
    print ("TYPE: ALPHA")
    print ("VERSION: 1")
    print ("API LEVEL: 5")
    print ("DEPENDENCIES: PYTHON")
    print ("MODULE(S): CWM")
    print ("COMPILATION DATE: 2016-04-02 GMT +1 19:10")
    print ("TOOLCHAIN(S): GCC 4.3; PY2EXE")

elif cmd =="bave -e":
    exit()

else:
    exit()

while cmd == "bave -a" or cmd == "bave -s" or cmd == "bave -m" or cmd == "bave -d" or cmd == "bave -x" or cmd == "bave -l" or cmd == "help" or cmd == "bave -h" or cmd == "bave -i":
    print ("")
    cmd = raw_input("$>> ")

    if cmd == "help":
        bavem.help()
        
    elif cmd == "bave -h":
        bavem.help()

    elif cmd == "bave -a":
       print("")
       a = raw_input("Type the first argument here: ")
       b = raw_input("Type the second argument here: ")
       print("")
       c = bavem.addition(a,b)
       print (str(a) + " + " + str(b) + " = " + str(c))
    elif cmd == "bave -s":
       print("")
       a = raw_input("Type the first argument here: ")
       b = raw_input("Type the second argument here: ")
       print("")
       c = bavem.subtraction(a,b)
       print (str(a) + " - " + str(b) + " = " + str(c))

    elif cmd == "bave -m":
       print("")
       a = raw_input("Type the first argument here: ")
       b = raw_input("Type the second argument here: ")
       print("")
       c = bavem.multiplication(a,b)
       print (str(a) + " x " + str(b) + " = " + str(c))

    elif cmd == "bave -d":
       print("")
       a = raw_input("Type the first argument here: ")
       b = raw_input("Type the second argument here: ")
       print("")
       c = bavem.division(a,b)
       print (str(a) + " / " + str(b) + " = " + str(c))

    elif cmd == "bave -x":
       print("")
       a = raw_input("Type the expression here: ")
       print("")
       c = bavem.expro(a)
       print (str(a) + " = " + str(c))

    elif cmd == "bave -l":
       print("")
       print ("This software is licensed under the GNU GPL v3.0.")

    elif cmd =="bave -i":
        print ("")
        print ("BUILD INFO")
        print ("----------")
        print ("TYPE: ALPHA")
        print ("VERSION: 1")
        print ("API LEVEL: 5")
        print ("DEPENDENCIES: PYTHON")
        print ("MODULE(S): CWM")
        print ("COMPILATION DATE: 2016-04-02 GMT +1 19:10")
        print ("TOOLCHAIN(S): GCC 4.3; PY2EXE")


    elif cmd =="bave -e":
        exit()

    else:
        exit()

#</main>#
