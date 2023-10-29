from colorama import Style, Fore, init
import os
import random


def initialize_colorama():
    init()
    os.system('cls' if os.name == 'nt' else 'clear')


def read():
    f = open("cuvinte.txt", "r")
    cuvinteq = f.readlines()
    f.close()
    for jj in range(len(cuvinteq)):
        cuvinteq[jj] = cuvinteq[jj].replace("\n", "")
    return cuvinteq


def update_list(cuvinte_vechi, greenl, yllwl, redl):
    ls = []
    for x in cuvinte_vechi:
        ok = 1
        for i in range(5):
            if x[i] != greenl[i] and greenl[i] != '':
                ok = 0
        for i in yllwl:
            if not x.__contains__(i):
                ok = 0
            for jjj in range(5):
                if yllwl[jjj] == x[jjj]:
                    ok = 0
        for i in redl:
            if x.__contains__(i):
                ok = 0
        if ok:
            ls.append(x)
    return ls


initialize_colorama()

print(f"{Fore.LIGHTGREEN_EX}{'Introduceti numarul de guess-uri wordle: '}{Style.RESET_ALL}")
n = int(input())

suma = 0
copiecuvinte = read()
for zz in range(n):
    green = ['', '', '', '', '']

    cuvinte = list(copiecuvinte)
    __choice__ = random.choice(cuvinte)

    print(f"{Fore.LIGHTMAGENTA_EX}{'-' * 69}")
    # print(f"{Fore.LIGHTMAGENTA_EX}{'Cuvantul care trebuie ghicit este'}", end=': ')
    # print(__choice__, end='\n')

    tries = 0
    while True:
        yllw = ['', '', '', '', '']
        red = []
        cuv = random.choice(cuvinte)
        if cuvinte.__contains__(cuv):
            contor = 0
            for j in range(len(cuv)):
                if cuv[j] == __choice__[j]:
                    print(f"{Fore.GREEN}{cuv[j]}{Style.RESET_ALL}", end="")
                    green[j] = cuv[j]
                    contor += 1
                elif __choice__.find(cuv[j]) != -1:
                    print(f"{Fore.YELLOW}{cuv[j]}{Style.RESET_ALL}", end="")
                    yllw[j] = cuv[j]
                else:
                    print(f"{Fore.RED}{cuv[j]}{Style.RESET_ALL}", end="")
                    red.append(cuv[j])

            tries += 1
            if contor == 5:
                print('\n'f"{Fore.LIGHTMAGENTA_EX}{zz+1}. Cuvantul {__choice__} a fost gasit din {tries} incercari.")
                suma += tries
                break
        print()
        cuvinte = update_list(cuvinte, green, yllw, red)
        # print(f"{Fore.LIGHTBLACK_EX}{cuvinte}")
        # print(yllw)

print("Numărul mediu de încercări pentru ghicirea tuturor cuvintelor este", end=" ")
print(suma / n)
