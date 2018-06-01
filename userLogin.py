#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      172484
#
# Created:     01-06-2018
# Copyright:   (c) 172484 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Login_module
import csv

def userLogin(self):
    heads = ['Login', 'Pass', 'Function', 'Active']
    controlVar = True
    while controlVar:
        print(f"Jestes zalogowany jako uzytkownik: {self.userLogin}.")
        print("Funkcje uzytkownika:")
        print("1. Wyswietl moje dane")
        print("2. Zmien moje dane")
        print("3. Wyloguj")
        try:
            choice = int(input("Wybierz co chcesz zrobic: "))
        except ValueError:
            print("Nie podales cyfry/liczby. Prosze o podanie cyfry/liczby a nie litery/wyrazu.")
            userLogin(self)

        if choice == 3:
            controlVar = False
            self.logOut()

        if choice == 1:
            Login_module.LoginModule.printUserData(self)

        if choice == 2:
            try:
                whatYouWantChange = int(input("1. Zmiana loginu uzytkownika, 2. Zmiana hasla uzytkownika, 3. Wszystko."))
            except ValueError:
                print("Nie podales cyfry/liczby. Prosze o podanie cyfry/liczby a nie litery/wyrazu.")
                userLogin(self)

            if whatYouWantChange == 1:
                newLoginTmp = input('Podaj nowy login: ')
                for user in self.users:
                    if user['Login'] == self.userLogin:
                        user['Login'] = newLoginTmp

                with open("data.csv", "w", encoding="utf-8") as newUser:
                    data = csv.DictWriter(newUser, fieldnames=heads, delimiter=';')
                    data.writeheader()
                    for n in self.users:
                        data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})

            if whatYouWantChange == 2:
                newPasswordTmp = input('Podaj nowe haslo: ')
                for user in self.users:
                    if user['Login'] == self.userLogin:
                        user['Pass'] = newPasswordTmp

                with open("data.csv", "w", encoding="utf-8") as newUser:
                    data = csv.DictWriter(newUser, fieldnames=heads, delimiter=';')
                    data.writeheader()
                    for n in self.users:
                        data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})


            if whatYouWantChange == 3:
                newDataTmp = []
                dataUser = {}
                newDataTmp.append(input('Podaj nowy login uzytkownika do zmiany: '))
                newDataTmp.append(input('Podaj nowe haslo uzytkownika: '))
                for user in self.users:
                    if user['Login'] == self.userLogin:
                        user['Login'] = newDataTmp[0]
                        user['Pass'] = newDataTmp[1]
                        user['Function'] = user['Function']
                        user['Active'] = user['Active']

                with open("data.csv", "w", encoding="utf-8") as newUser:
                    data = csv.DictWriter(newUser, fieldnames=heads, delimiter=';')
                    data.writeheader()
                    for n in self.users:
                        data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})

            print("Zostales wylogowany po zmianie danych. Jezeli chcesz kontynuowac musisz sie zalogowac ponownie.")
            controlVar = False
            self.logOut()