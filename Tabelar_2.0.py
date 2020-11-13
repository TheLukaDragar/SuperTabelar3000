import re
from functools import partial
import sys
import Kmap
import itertools

save = True
translator = {

    "∧": " and ",
    "&&": " and ",
    "||": " or ",
    "∨": " or ",
    "+": " or ",
    "¬": " not ",
    "!": " not ",
    ">>": " ^1 or ",
    "⇒": " ^1 or ",
    "⇔": " == ",
    "==": " == ",
    "*": " and "}

# realizacija da je (a xor 1)  enak kot (not a)
translatorforwords = {
    "xor": " ^ ",  # add xnor
    "nor": " ^1 and 1^ ",
    "nand": " ^1 or 1^ ",
    "and": " and ",
    "or": " or ",
    "not": " not ",
    "imply": " ^1 or ",
    "equal": " == "

}


def replacewords(input):
    for wordkey in translatorforwords.keys():
        input = input.replace(wordkey, translatorforwords[wordkey])

    return input


def replacesigns(input):
    for key in translator.keys():
        input = input.replace(key, translator[key])

    return input


def findvariables(exp):
    for wordkey in translatorforwords.keys():
        exp = exp.replace(wordkey, " ")

    for key in translator.keys():
        exp = exp.replace(key, " ")

    exp = exp.replace("(", " ").replace(")", " ")

    listofvar = exp.split()
    listofvar.sort()

    mylist = list(dict.fromkeys(listofvar))

    return mylist


def calculate(expression_list, variable_list):
    result_dict = {}

    for expression in expression_list:

        print("-" * 30)
        print(expression)
        print("-" * 30)

        expression_results = []
        for input_vector in range(0, 2 ** len(variable_list)):

            exp = expression

            minterm = list("{0:b}".format(input_vector).zfill(len(variable_list)))

            cnt = 0
            for var in variable_list:
                # replacing variables names with minterm values
                exp = re.sub(r'\b{}\b'.format(var), minterm[cnt], exp)  # replacing only whole words MATCHING
                cnt = cnt + 1

            result = int(eval(exp))

            print(exp + " ~ " + str(result))

            expression_results.append(result)

        result_dict[str(expression)] = (expression_results)

    return result_dict


def printresults(variables_list, expression_list, results):
    print("--------------------Results------------------------------")
    tosave = []
    tosave.append(str(expression_list))
    tosave.append("".join(variables_list))
    for variable in variables_list:
        print(variable, end="")
    print()

    for k in range(0, 2 ** len(variables_list)):

        input_vector = list("{0:b}".format(k).zfill(len(variables_list)))

        outzeros = ""
        for exp in expression_list:
            minterm = str(results[str(exp)][k]).replace(
                "True", "1").replace("False", "0")

            outzeros = outzeros + minterm

        print("".join(input_vector) + " " + outzeros)

        tosave.append("".join(input_vector) + " " + outzeros)

    print("-------------------------------------------------------")
    if save:
        print("\n".join(tosave), file=open('save.txt', 'w'))


def get_minterms(variables_list, expression_list, results):
    expressions_minterms_list = {}

    for expression in expression_list:

        minterms = []

        for k in range(0, 2 ** len(variables_list)):
            minterm = str(results[str(expression)][k]).replace("True", "1").replace("False", "0")

            if minterm == "1":
                input_vector = list("{0:b}".format(k).zfill(len(variables_list)))
                minterms.append(input_vector)

        expressions_minterms_list[str(expression)] = minterms

    return expressions_minterms_list


def printPDNO(minterms, variables_list):
    for expression, minterm_list in minterms.items():

        pdno = []
        for minterm in minterm_list:

            one_minterm = ""
            for i in range(0, len(variables_list)):
                if minterm[i] == "1":
                    one_minterm += variables_list[i]

                if minterm[i] == "0":
                    one_minterm += variables_list[i] + "'"  # negation sign

            pdno.append(one_minterm)

        print("PDNO: " + expression + " \n " + " + ".join(pdno))


def getDNO(minterms):
    DNO = {}
    for expression, minermlist in minterms.items():
        mintermss = []
        for minterms in minermlist:
            mintermss.append("".join(minterms))

        simplified = Kmap.simplifyyy(mintermss)

        DNO[expression] = simplified

    return DNO


def printDNO(dno_list, variables_list):
    for expression, dnos in dno_list.items():

        res = []
        for dno in dnos:
            dno=str(dno)
            one_minterm = ""
            for i in range(0, len(variables_list)):
                if dno[i] == "1":
                    one_minterm += variables_list[i]

                if dno[i] == "0":
                    one_minterm += variables_list[i] + "'"  # negation sign

            res.append(one_minterm)

        res.sort()

        print("DNO: " + expression + " \n " + " + ".join(res))


if __name__ == '__main__':

    expression_list = []
    variables_list = []

    while True:

        exprs = input("enter expression" + "\n")

        if exprs == "exit" or exprs == "":
            print("ok bye!")
            sys.exit()

        if exprs == "clear":
            print("ok clearing")
            expression_list.clear()
            variables_list.clear()
            continue

        variables_list.extend(findvariables(exprs))
        variables_list = list(dict.fromkeys(variables_list))
        variables_list.sort()

        expression = replacesigns(replacewords(exprs))
        expression_list.append(expression)

        print(expression)
        print(variables_list)

        results = {}
        results = calculate(expression_list, variables_list)

        print("-" * 30)
        print(expression_list)

        printresults(variables_list, expression_list, results)

        minterms = get_minterms(variables_list, expression_list, results)

        printPDNO(minterms, variables_list)
        printDNO(getDNO(minterms), variables_list)
