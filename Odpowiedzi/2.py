# -*- coding: utf8 -*-

"""
kalkulator BMI 2
Zapisz kalkulator BMI, który wcześniej był w konsoli do pliku,
tak aby pytał użytkownika o potrzebne do obliczeń dane.
"""

print("Podaj wagę w kg: ")
weight = float(input())
print("Podaj wzrost w m: ")
height = float(input())
BMI = weight / (height ** 2)
print("Twoje bmi wynosi:", BMI)
