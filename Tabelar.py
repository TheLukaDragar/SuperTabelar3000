import re
from functools import partial
import sys

listizrazi=[]
listofvar = []

save=True
translator = {"∧": " and ",
              "&&": " and ",
              "||": " or ",
              "∨": " or ",
              "+": " or ",
              "¬": " not ",
              "!": " not ",
              ">>": " implc ",
              "⇒": " implc ",
              "⇔": " == ",
              "*": " and "}


def getinput(x):
    if x == 0:
        #a="t->(p∨u),u∧(¬t∨s),¬s∨¬u∨r⊨p∧r∨¬p∧¬r".upper()
        #a = "s∧q⇒r,s,p⇒¬(q⇒r)⊨¬p".upper()
        #q⇒(¬r∧t),r⇒(¬p∨¬u),¬t⇔p∨s⊨(q∨t)∧(¬q∨¬t) ROBLEMATICNA

        a = input("vnesi izraz\n").upper()

        if a=="EXIT" or a=="":
            print("ok bye!")
            sys.exit()

        if a=="CLEAR":
            print("ok clearing")
            listizrazi.clear()
            listofvar.clear()
            nums=[]
            return nums

        num = getnumofvariables(a)

        listizrazi.append(a)

        return num


def getnumofvariables(text):
    word1 = " ".join(re.findall("[a-zA-Z]+", text))
    
    for letter in word1:
        if not listofvar.__contains__(letter) and letter != " ":
            listofvar.append(letter)
    return listofvar


def racunaj(izraziall):

    resulttable = {}

    for zraz in izraziall:

        print("-------------------------")
        print(zraz)
        print("-------------------------")

        listofoneszeros = []

        for i in range(0, 2 ** len(numofvar)):
            lst = list("{0:b}".format(i).zfill(len(numofvar)))

            iz = zraz



           # if "implc" in iz:

            #    iz = implicationsorter(iz)

                # izz=iz.split("implc",1)
                # print(iz)
                # iz="spr("+izz[0]+","+izz[1]+")"

            cnt = 0
            for var in numofvar:
                iz = iz.replace(var, lst[cnt])
                cnt = cnt + 1

            # print(iz)

            print(iz+" ~ "+str(int(eval(iz))))

            listofoneszeros.append(eval(iz))

        resulttable[zraz] = listofoneszeros

    return resulttable

def printresults(numofvar,izraziall,resulttable):
    print("--------------------Results------------------------------")
    tosave=[]
    tosave.append(str(izraziall))
    tosave.append("".join(numofvar))
    for num in numofvar:
        print(num,end="")
    print()
    
    for k in range(0, 2 ** len(numofvar)):

        bin0 = list("{0:b}".format(k).zfill(len(numofvar)))

        outzeros = ""
        for izzzz in izraziall:
            e = str(resulttable[izzzz][k]).replace("True", "1").replace("False", "0")

            outzeros = outzeros + e

        print("".join(bin0) + " " + outzeros)
        tosave.append("".join(bin0) + " " + outzeros)


    print("-------------------------------------------------------")
    if save:
        print("\n".join(tosave),  file=open('save.txt', 'w'))

def imply(x, y):
    if x == 1 and y == 0:
        return 0
    else:
        return 1


def implicationsorter(izraz):
    stimplikacij = len(izraz.split("implc")) - 1
    # print(stimplikacij)

    lst = []

    for i in range(0, stimplikacij):
        endel = izraz.split("implc")[i]
        #print(endel)

        # sprehajanjelevo
        if "(" in endel:
            rev = str(endel[::-1])

            o = rev.split("(", 1)

            endel = " not "+" ( " + o[1][::-1] + o[0][::-1]

        elif ")" in endel:
            endel= endel
          #  print("LST"+str(lst))
            dd=lst[i-1]

            new=dd.split("(",1)
            lst[i-1]= new[0]+" ( " + " not "+new[1]
            #print(dd)



        else:

            endel = " not " + " ( "+ endel+" ) "

        #print(str(endel))

        lst.append(endel)

    toret = " or ".join(lst)
    toret = toret + " or " + izraz.split("implc")[-1]
  
    return toret
#print(toret)

if __name__ == "__main__":

    while True:
        numofvar = getinput(0)
        print(numofvar)
        print("------------")

        izrazi2 = []

        c = 0
        for izraz in listizrazi:
            print(izraz)
            for key in translator.keys():
                izraz = izraz.replace(key, translator[key])

            if "implc" in izraz:
                izraz = implicationsorter(izraz)

            izrazi2.append(izraz)

            c = c + 1

        print("------------")

        izraziall = []

        izraziall.extend(izrazi2)
        resulttable = {}
        resulttable =racunaj(izraziall)
        print("------------")
        print(izraziall)
        printresults(numofvar,izraziall,resulttable)







