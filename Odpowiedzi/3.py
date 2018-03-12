# -*- coding: utf8 -*-

"""
kalkulator zapotrzebowania kalorycznego 2
Zapisz kalkulator BMR, który wcześniej był w konsoli do pliku,
tak aby pytał użytkownika o potrzebne do obliczeń dane.
"""

#wzór dla kobiet
weight = float(input("Twoja waga [kg]: "))
height = float(input("Twój wzrost [cm]: "))
age = int(input("Twój wiek: "))
S = -161
PPM = 10 * weight + 6.25 * height + 5 * age + S

print("Dzienne zapotrzebowanie kaloryczne wynosi:", PPM * 1.6, "kcal")
