# # # FizzBuzz
# # # Jei skaicius dalinasi is 3:
# # # grazinti Fizz
# # # Jei dalinasi is 5:
# # # grazinti Buzz
# # # # Jei dalinasi is 3 ir is 5:
# # # # # grazinti 'FizzBuzz'
# # # # # has context menu
# # # # #
# # # #
# # # # number = 30
# # #
# # # # if number == 5:
# # # #     print(f'number is {number}')
# # # # elif 7 > number > 5:
# # # #     print(f'{number} is larger than 5')
# # # # elif number * 2 > 14:
# # # #     print(f'{number} daugyba')
# # # # else:
# # # #     print('Bet ka')
# # #
# # # # if number / 3:
# # # #     print('fizz')
# # # # elif number / 5:
# # # #     print('buzz')
# # # # else:
# # # #     print('fizzbuzz')
# # #
# # #
# # #
# # #
# # # a = input('Iveskite skaiciu A')
# # # b = input('Iveskite sakiciu B')
# # #
# # # if a > b:
# # #     print(input())
# # # elif a < b:
# # #     print(input())
# # # elif a == b:
# # #     print(input())
# # # else:
# # #     print('beleka senelyzai')
# #
# #
# # zen_of_python = """﻿The Zen of Python, by Tim Peters
# #
# # Beautiful is better than ugly.
# # Explicit is better than implicit.
# # Simple is better than complex.
# # Complex is better than complicated.
# # Flat is better than nested.
# # Sparse is better than dense.
# # Readability counts.
# # Special cases aren't special enough to break the rules.
# # Although practicality beats purity.
# # Errors should never pass silently.
# # Unless explicitly silenced.
# # In the face of ambiguity, refuse the temptation to guess.
# # There should be one-- and preferably only one --obvious way to do it.
# # Although that way may not be obvious at first unless you're Dutch.
# # Now is better than never.
# # Although never is often better than *right* now.
# # If the implementation is hard to explain, it's a bad idea.
# # If the implementation is easy to explain, it may be a good idea.
# # Namespaces are one honking great idea -- let's do more of those!
# # """
# #
# # # Atspausdinti paskutinį antro žodžio simbolį
# # second_word = zen_of_python.split()[1]
# # print(second_word[-1])
# #
# # # Atspausdinti pirma trecio zodzio simboli
# # third_word = zen_of_python.split()[2]
# # print(third_word[0])
# # #
# # # # Atspausdinti tik pirma zodi
# # # first_word = zen_of_python.split()[0]
# # # print(first_word)
# # #
# # # # Atspausdinti tik paskutini zodi
# # # last_word = zen_of_python.split()[-1]
# # # print(last_word)
# # #
# # # # Atspausdinti visą frazę atbulai
# # # print(zen_of_python[::-1])
# # #
# # # # Atskirti žodžius ir juos atspausdinti
# # # words = zen_of_python.split()
# # # for word in words:
# # #     print(word)
# # #
# # # # Pakeisti žodį "Python" į "Programming" ir atspausdinti naują sakinį
# # # new_sentence = zen_of_python.replace("Python", "Programming")
# # # print(new_sentence)
# # #
# # #
# # # third_word = (zen_of_python) upper()
# # # print(zen_of_python[::1])
# #
# # # input(number = "")
# # # input(numer2 = "")
# #
# #
# #
# # def add(x, y):
# #     return x + y
# #
# # def subtract(x, y):
# #     return x - y
# #
# # def multiply(x, y):
# #     return x * y
# #
# # def divide(x, y):
# #     return x / y
# #
# # def exponentiate(x, y):
# #     return x ** y
# #
# # def modulo(x, y):
# #     return x % y
# #
# # def perform_operation():
# #     num1 = float(input("Enter the first number: "))
# #     num2 = float(input("Enter the second number: "))
# #
# #     operation = input("Enter the operation (+, -, *, /, **, %): ")
# #
# #     if operation == '+':
# #         print("Result:", add(num1, num2)
# #     elif operation == '-':
# #         print("Result:", subtract(num1, num2)
# # import random
#
#
# # numbers = [1, 2, 3, 4, 5, 6, 7]
# #
# # for num in numbers:
# #     if num % 2 == 0:
# #         print(num)
#
#
#
#
#
#
#
# # # Parašyti programą, kuri:
# # #
# # # Leistų vartotojui įvesti skaičių.
# # # Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# # # Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# # # Patarimas: Naudoti ciklą while, sąlygą if, break
# #
# # #
# # teigiamas_skaičius = 0
# #
# # while True:
# #     skaicius = float(input("Įveskite skaičių: "))
# #     if skaicius > 0:
# #         teigiamas_skaičius += skaicius
# #         skaicius = float(input("Įveskite dar vieną skaičių: "))
# #     else:
# #         break
# # print("Visų įvestų teigiamų skaičių suma yra:", suma_teig)
# #
# #
# #
#
#
#
#
#
#
# #
# # Sukurti programą, kuri:
# #
# # Leistų vartotojui įvesti metus
# # # Atspausdintų „Keliamieji metai“, jei taip yra
# # # Atspausdintų „Nekeliamieji metai“, jei taip yra
# #
# #
# #
# # def ar_keliamieji_metai(metai):
# #     if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
# #         return True
# #     else:
# #         return False
# #
# # metai = int(input("Įveskite metus: "))
# # if ar_keliamieji_metai(metai):
# #     print(metai, "yra keliamieji metai.")
# # else:
# #     print(metai, "yra nekeliamieji metai.")
# #
# #
# #
# # def ar_keliamieji_metai(metai):
# #     if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
# #         return True
# #     else:
# #         return False
# #
# # for metai in range(1900, 2101):
# #     if ar_keliamieji_metai(metai):
# #         print(metai, "yra keliamieji metai.")
# #     elif ar_keliamieji_metai(metai):
# #         print(metai, "Yra nekeliamieji metai")
# #     else:
# #         break
# #
# #
# #
# # def ar_keliamieji_metai(metai):
# #     if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
# #         return True
# #     else:
# #         return False
# #
# # for metai in range(1900, 2101):
# #     if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
# #         print(metai, "yra keliamieji metai.")
#
#
# # Kauliukų žaidimas
# #
# # Sukurti programą, kuri:
# #
# # Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# # Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# # Kitu atveju atspausdinti „Laimėjai!“
# # Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break
# #
# # Random skaičiaus generavimo pavyzdys:
#
# # def Skaičiu_Generatorius():
# #     return random.randint(1, 6)
# #
# # def Metimas():
# #     while True:
# #         skaiciai = [Skaičiu_Generatorius() for _ in range(3)]
# #         print("Tavo skaičiai:", skaiciai)
# #         if 5 in skaiciai:
# #             print("Pralaimėjai...")
# #         else:
# #             print("Laimėjai!")
# #             break
# #
#
# #
# #  Yra duotas listas, jame yra žodžiai. Parašyti algortimą, kuris atrinktų patį ilgiausią besikartojančių žodžių fragmenta. Pvz, jei listas:
# # [‚namas‘, ‚namelis‘, ‚nameliukas‘] -> „nam“
# # [morkytė, molas, morka] - > mo
# # [namas, balkonas, mama] - > „“ tuscias stringas.
#
#
# #
# # def ilgiausias_besikartojantis_fragmentas(sarasas):
# #     zodziu_sarasas = list(set(sarasas))
# #     ilgiausias_fragmentas = ''
# #
# #     for i in range(len(zodziu_sarasas)):
# #         zodis1 = zodziu_sarasas[i]
# #         for j in range(i + 1, len(zodziu_sarasas)):
# #             zodis2 = zodziu_sarasas[j]
# #             fragmentas = ''
# #             for k in range(min(len(zodis1), len(zodis2))):
# #                 if zodis1[k] == zodis2[k]:
# #                     fragmentas += zodis1[k]
# #                 else:
# #                     break
# #             if len(fragmentas) > len(ilgiausias_fragmentas):
# #                 ilgiausias_fragmentas = fragmentas
# #
# #     return ilgiausias_fragmentas
# #
# #
# # # Pavyzdžiai:
# # sarasas1 = ['namas', 'namelis', 'nameliukas']
# # sarasas2 = ['morkyte', 'molas', 'morka']
# # sarasas3 = ['namas', 'balkonas', 'mama']
# #
# # print(ilgiausias_besikartojantis_fragmentas(sarasas1))  # Rezultatas: "nam"
# # print(ilgiausias_besikartojantis_fragmentas(sarasas2))  # Rezultatas: "mo"
# # print(ilgiausias_besikartojantis_fragmentas(sarasas3))  # Rezultatas: ""
# #
# #
#
#
#
#
# #
# # Sukurkite ir išsibandykite funkcijas, kurios:
# #
# # 1. Gražinti trijų paduotų skaičių sumą
#
# #
# # def suma_triju_skaiciu(a, b, c):
# #     return a + b + c
# #
# # # Išbandykime funkciją su kai kuriomis reikšmėmis
# # print(suma_triju_skaiciu(1, 2, 3))  # Turėtų grąžinti 6
# # print(suma_triju_skaiciu(10, 20, 30))  # Turėtų grąžinti 60
# # print(suma_triju_skaiciu(-5, 5, 0))  # Turėtų grąžinti 0
# #
# #
# # # 2. Gražintų paduoto sąrašo iš skaičių, sumą.
# #
# # def suma_liste(numbers):
# #     return sum(numbers)
# #
# # sarasas = [1, 2, 3, 4, 5]
# #
# # print("Suma:", suma_liste(sarasas))
# #
# # # 3.Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
# #
# # def didziausias(*args):
# #     if len(args) == 0:
# #         print("Nėra pateiktų skaičių")
# #     else:
# #         didziausias_sk = max(args)
# #         print("Didžiausias skaičius:", didziausias_sk)
# #
# # # Pavyzdiniai skaičiai
# # didziausias(1, 5, 3, 8, 2)
# # didziausias(10, 20, 30)
# # didziausias(-5, -10, -3, -2)
#
# # # 4.Gražintų paduotą stringą atbulai.
# #
# # def atbulai(stringas):
# #     return stringas[::-1]
# #
# # tekstas = "Sula Alus"
# #
# # print("Atbulai:", atbulai(tekstas))
#
#
# # 5.Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
# #
# # def stringo_raidžių_kiekiai(stringas):
# #     zodziu_skaicius = 0
# #     didziuju_raziu_skaicius = 0
# #     mazuju_raziu_skaicius = 0
# #     skaiciu_skaicius = 0
# #
# #     for char in stringas:
# #         if char.islower():
# #             mazuju_raziu_skaicius += 1
# #         elif char.isupper():
# #             didziuju_raziu_skaicius += 1
# #         elif char.isdigit():
# #             skaiciu_skaicius += 1
# #
# #     zodziu_skaicius = len(stringas.split())
# #
# #     print("Žodžių skaičius:", zodziu_skaicius)
# #     print("Didžiųjų raidžių skaičius:", didziuju_raziu_skaicius)
# #     print("Mažųjų raidžių skaičius:", mazuju_raziu_skaicius)
# #     print("Skaičių skaičius:", skaiciu_skaicius)
# #
# # tekstas = "Mano vardas Laurynas pavardė Bulavinas mano mašinos numeriai 445 "
# #
# # stringo_raidžių_kiekiai(tekstas)
#
# # # 6.Gražintų sąrašą tik su nepasikartojančiais paduoto sąrašo elementais.
# #
# # def Nepasikartojanciu_skaiciu_sarasas(sarasas):
# #     nepasikrtojantis = list(set(sarasas))
# #     return nepasikrtojantis
# #
# # sarasas = [1, 2, 3, 4, 2, 3, 5]
# #
# # print("Sąrašas su unikaliais elementais:", Nepasikartojanciu_skaiciu_sarasas(sarasas))
# #
# # # 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
# #
# #
# # def rikiuoti_zodzius_atvirksciai(tekstas):
# #     zodziai = tekstas.split()
# #     zodziai_atvirksciai = ' '.join(reversed(zodziai))
# #     return zodziai_atvirksciai
# #
# # # Pavyzdinis string'as
# # tekstas = "Labas, pasauli! Kaip gyveni?"
# #
# # # Iškvietimas ir spausdinimas
# # print("Išrikiuoti žodžiai atvirkščiai:", rikiuoti_zodzius_atvirksciai(tekstas))
#
#
# # 1.Yra duotas listas, jame yra žodžiai. Parašyti algortimą, kuris atrinktų patį ilgiausią besikartojančių žodžių fragmenta. Pvz, jei listas:
# #
# # [‚namas‘, ‚namelis‘, ‚nameliukas‘] -> „nam“
# #
# # [morkytė, molas, morka] - > mo
# #
# # # [namas, balkonas, mama] - > „“ tuscias stringas.
#
#
# # from collections import Counter
# #
# # def ilgiausias_fragmentas(sarasas):
# #     if not sarasas:
# #         return ""
# #
# #     zodziu_skaiciai = Counter()
# #     for zodis in sarasas:
# #         for i in range(len(zodis)):
# #             for j in range(i+1, len(zodis)+1):
# #              fragmentas = zodis[i:j]
# #              zodziu_skaiciai[fragmentas] += 1
# #
# #     ilgiausias_fragmentas = ""
# #     ilgiausias_fragmento_ilgis = 0
# #     for fragmentas, skaicius in zodziu_skaiciai.items():
# #         if skaicius > 1 and len(fragmentas) > ilgiausias_fragmento_ilgis:
# #             ilgiausias_fragmentas = fragmentas
# #             ilgiausias_fragmento_ilgis = len(fragmentas)
# #
# #     return ilgiausias_fragmentas
#
#
# # 2.Duotas listas skaiciu – [1, 2, 3, 4, 5, 6, 18, 90, 118, 991,  196151]. Grazinti dicta, kuris butu suskaiciuota kiek is siu skaiciu yra lyginiu, kiek nelyginiu:
# #
# # {
# #
# # ‚lyginiu_skaiciu_suma‘: suskaiciuotas kiekis‘,
# #
# # ‚nelyginiu_skaiciu_suma‘: suskaiciuotas kiekis‘
# #
# # }
# # #
# # #
# #
# #
# # def skaiciuoti_lyginius_nelyginius(skaiciai):
# #     lyginiai = 0
# #     nelyginiai = 0
# #
# #     for skaicius in skaiciai:
# #         if skaicius % 2 == 0:
# #             lyginiai += 1
# #         else:
# #             nelyginiai += 1
# #
# #     rezultatai = {
# #         'lyginiu_skaiciu_suma': lyginiai,
# #         'nelyginiu_skaiciu_suma': nelyginiai
# #     }
# #
# #     return rezultatai
# #
# # skaiciai = [1, 2, 3, 4, 5, 6, 18, 90, 118, 991, 196151]
# # rezultatai = skaiciuoti_lyginius_nelyginius(skaiciai)
# # print(rezultatai)
# #
# #
# # # 3. Yra stringas; ‚1asdg16asdg1wg16ewrg1er6gw1‘. Suskaiciuoti ir grazinti dicte kiek yra skaiciu ir kiek yra raidziu.
# #
# #
# # def skaiciu_ir_raziu_skaiciavimas(stringas):
# #     skaiciai = 0
# #     raidzes = 0
# #     for simbolis in stringas:
# #         if simbolis.isdigit():
# #             skaiciai += 1
# #         elif simbolis.isalpha():
# #             raidzes += 1
# #     rezultatai = {'skaičiai': skaiciai, 'raidės': raidzes}
# #     return rezultatai
# #
# # stringas = '1asdg16asdg1wg16ewrg1er6gw1'
# # rezultatai = skaiciu_ir_raziu_skaiciavimas(stringas)
# # print("Skaičių kiekis:", rezultatai['skaičiai'])
# # print("Raidžių kiekis:", rezultatai['raidės'])
# #
# #
# # 4.
# #
# #
# #
# # input_list = [3, 2, 'm', 'lele', (1, 2, 3), [1, 2, 3], {'vienas': 1, 'du': 2}]
# #
# # result_dict = {}
# #
# # for item in input_list:
# #     if isinstance(item, str):  # Tikrinama, ar elementas yra stringas
# #         result_dict[item] = len(item)  # Simbolių skaičius
# #     elif isinstance(item, int):  # Tikrinama, ar elementas yra sveikasis skaičius
# #         result_dict[item] = item ** 2  # Kvadratas
# #     elif isinstance(item, list):  # Tikrinama, ar elementas yra sąrašas
# #         result_dict[item] = sum(item)  # Sąrašo suma
# #     elif isinstance(item, dict):  # Tikrinama, ar elementas yra žodynas
# #         result_dict[item] = sum(item.values())  # Žodyno reikšmių suma
# #     elif isinstance(item, tuple):  # Tikrinama, ar elementas yra tuple
# #         result_dict[item] = 1  # Pradinė reikšmė, kuri bus padauginta
# #         for num in item:
# #             result_dict[item] *= num  # Visų tuple elementų daugyba
# #
# # print(result_dict)
#
#
#
#
#
# # class Tankas:
# #     def __init__(self):
# #         self.x = 0
# #         self.y = 0
# #         self.kryptis = 'pirmyn'
# #         self.suvis = {'pirmyn': 0, 'atgal': 0, 'kairėn': 0, 'dešinėn': 0}
# #
# #     def tanko_judejimas(self, kryptis):
# #         if kryptis == 'pirmyn':
# #             self.y += 1
# #         elif kryptis == 'atgal':
# #             self.y -= 1
# #         elif kryptis == 'kairėn':
# #             self.x -= 1
# #         elif kryptis == 'dešinėn':
# #             self.x += 1
# #
# #     def sauti(self):
# #         self.suvis[self.kryptis] += 1
# #
# #     def info(self):
# #         print("Tanko kryptis:", self.kryptis)
# #         print("Tanko koordinatės: ({}, {})".format(self.x, self.y))
# #         print("Iš viso atliko šūvių:", sum(self.suvis.values()))
# #         print("Šūviai į kiekvieną kryptį:")
# #         for direction, shots in self.suvis.items():
# #             print("- {}: {}".format(direction, shots))
# #
# #
# class Tankas:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.kryptis = 'pirmyn'
#         self.suvis = {'pirmyn': 0, 'atgal': 0, 'kairėn': 0, 'dešinėn': 0}
#
#     def tanko_judejimas(self, kryptis):
#         if kryptis == 'pirmyn':
#             self.y += 1
#         elif kryptis == 'atgal':
#             self.y -= 1
#         elif kryptis == 'kairėn':
#             self.x -= 1
#         elif kryptis == 'dešinėn':
#             self.x += 1
#
#     def sauti(self):
#         self.suvis[self.kryptis] += 1
#
#     def info(self):
#         print("Tanko kryptis:", self.kryptis)
#         print("Tanko koordinatės: ({}, {})".format(self.x, self.y))
#         print("Iš viso atliko šūvių:", sum(self.suvis.values()))
#         print("Šūviai į kiekvieną kryptį:")
#         for direction, shots in self.suvis.items():
#             print("- {}: {}".format(direction, shots))
#
# tank = Tankas()
#
# while True:
#     print("\nPasirinkite veiksmą:")
#     print("1. Judėti")
#     print("2. Šaudyti")
#     print("3. Informacija")
#     print("4. Baigti programą")
#
#     choice = input("Įveskite pasirinkimą: ")
#
#     if choice == '1':
#         direction = input("Įveskite judėjimo kryptį (pirmyn, atgal, kairėn, dešinėn): ")
#         tank.tanko_judejimas(direction)
#     elif choice == '2':
#         tank.sauti()
#     elif choice == '3':
#         tank.info()
#     elif choice == '4':
#         print("Programa baigia darbą.")
#         break
#     else:
#         print("Neteisingas pasirinkimas. Bandykite dar kartą.")

# import random
#
# class Taikinys:
#     def __init__(self):
#         self.x = random.randint(-10, 10)
#         self.y = random.randint(-10, 10)
#
#     def ar_pataike(self, x, y):
#         return self.x == x and self.y == y
#
# class Tankas:
#     def __init__(self):
#         self.x = random.randint(-10, 10)
#         self.y = random.randint(-10, 10)
#         self.kryptis = random.choice(['primyn', 'atgal', 'kairėn', 'dešinėn'])
#
#     def tanko_judėjimas(self, kryptis):
#         if kryptis == 'pirmyn':
#             self.y += 1
#         elif kryptis == 'atgal':
#             self.y -= 1
#         elif kryptis == 'kairėn':
#             self.x -= 1
#         elif kryptis == 'dešinėn':
#             self.x += 1
#
#     def sauti(self, taikinys):
#         if taikinys.ar_pataike(self.x, self.y):  # Corrected method call to ar_pataike
#             print('Pataikei')
#             taikinys = Taikinys()
#         else:
#             print('Nepataikei')
#
#     def informacija(self):
#         print('Tanko kryptis:', self.kryptis)
#         print('Tanko kordinatės: ({}, {})'.format(self.x, self.y))
#
# taikinys = Taikinys()
# tank = Tankas()
#
# while True:
#     print('\nPasirinkite veiksmą:')
#     print('1. Judėti')
#     print('2. Šaudyti')
#     print('3. Informacija')
#     print('4. Baigti programą')
#
#     pasirinkimas = input('Įveskite pasirinkimą: ')
#
#     if pasirinkimas == '1':
#         tanko_kryptis = input('Įveskite judėjimo kryptį (pirmyn, atgal, kairėn, dešinėn): ')
#         tank.tanko_judėjimas(tanko_kryptis)
#     elif pasirinkimas == '2':
#         tank.sauti(taikinys)
#     elif pasirinkimas == '3':
#         tank.informacija()
#     elif pasirinkimas == '4':
#         print('Programa užbaigs darbą')
#         break  # Exiting the loop if user chooses to end the program
#     else:
#         print('Neteisingai pasirinkote, bandykite iš naujo')