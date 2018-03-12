# -*- coding: utf8 -*-

"""
Skrypt:
- zapyta o Twoje imię
- powita Cię po imieniu
- zapyta o Twój wiek
- zapyta o peron z Harrego Potter’a
- odpowie (dowolnie łącząc wiek i peron), np. czy jest sens jechać do Hogwartu
"""
print("Jak masz na imię?")
name = input()
print("Cześć", name, "miło Cię poznać")
print("Ile masz lat?")
age = input()
print("Z jakiego peronu dostaniesz się do Hogwartu?")
platform = input()
print("W wieku", age, "lat chyba już nie ma sensu jechać na peron", platform)
