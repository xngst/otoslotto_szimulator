#!/usr/bin/env python3

"""
Ötöslottó szimulátor.
Addíg húzunk amíg ötösünk nem lesz!
"""

import itertools
import random
from collections import Counter

import click

@click.command()
@click.option('--megjatszott_szamok', 
    help='5darab ismétlés nélküli szám 1 és 90 között, Pl.: "5,23,45,75,36"')

def sorsolas(megjatszott_szamok: str):
    """
    """
    print("Kis türelmet, hamarosan sorsolunk..")
    n = range(1, 91)
    k = 5
    combinations = itertools.combinations(n, k)
    combination_list = [c for c in combinations]
    megjatszott_szamok = Counter([int(i) for i in megjatszott_szamok.split(",")])

    print("<<<<< ÖTÖS LOTTÓ >>>>>")
    print("^"*79)
    print("Minden egyes sorsoláson ugyanazokat a számokat játszuk meg.")
    print("Minden sorsolás új húzásnak felel meg.")
    print("Minden húzásnál 1 : 43 949 268 nyerési esélyünk van az ötös találatra.")
    print("Minden sorsolás alkalmával hozzáadunk a költségekhez 300 Forintot.")
    print("A sorsolásokat addig ismételjük, amíg a megjátszott számokkal ötös találatunk nem lesz.")
    print("A sorsolás elkezdődött!")
    print(f"Megjátszott számok: {list(megjatszott_szamok)}")

    print("^"*79)

    huzas_szamlalo = 0
    millio_szamlalo = 0
    koltseg = 300
    szerencse = False

    while not szerencse:
        nyero_szamok = Counter(random.choice(combination_list))
        if nyero_szamok == megjatszott_szamok:
            szerencse = True
            print("#"*79)
            print(list(nyero_szamok))
            print("Gratulálunk!")
            print(f"Telitalálat a {huzas_szamlalo:,d}. sorsoláson!")
            print(f"Összesen {koltseg:,d} Forintot költöttünk.")
            print("#"*79)
            break
        else:
            huzas_szamlalo += 1
            koltseg += 300
            print(f"Eddig {koltseg:,d} Forintot költöttünk",end="\r")
        if huzas_szamlalo % 1000000 == 0:
            millio_szamlalo += 1
            print()
            print(f"{millio_szamlalo} milliomodik sorsolás...")


if __name__ == '__main__':
    sorsolas()