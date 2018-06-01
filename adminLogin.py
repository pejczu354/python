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

def adminLogin(self):
    def addUser(self):
        try:
            uLogin = input("Podaj login nowego uzytkownika: ")
            uPass = input("Podaj haslo nowego uzytkownika: ")
            uFunction = input("Podaj funkcję uzytkownika(user/admin): ")
            uActive = input("Czy konto ma byc aktywne(y/n): ")
        except KeyboardInterrupt:
            print("Nieudane pobranie danych o uzytkowniku.")

        dataUser = {'Login':uLogin,'Pass':uPass,'Function':uFunction, 'Active': uActive}
        userStruct = [dataUser]
        print(dataUser)
        with open("data.csv", "a", encoding="utf-8") as newUser:
            fNames = ['Login', 'Pass', 'Function', 'Active']
            data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
            for n in userStruct:
                data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})
        adminLogin(self)

    def deleteUser(self):
        try:
            uLogin = input("Podaj login uzytkownika do usunięcia: ")
        except KeyboardInterrupt:
            print("Nieudane pobranie danych o uzytkowniku.")
        i=0
        for user in self.users:
            if uLogin == user['Login']:
                del self.users[i]
            i+=1

        with open("data.csv", "w", encoding="utf-8") as newUser:
                fNames = ['Login', 'Pass', 'Function', 'Active']
                data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                data.writeheader()
                for n in self.users:
                    data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})
        adminLogin(self)

    def changeUserData(self):
        try:
            whatYouWantChange = int(input("1. Zmiana loginu uzytkownika, 2. Zmiana hasla uzytkownika, 3. Zmiana funkcji uzytkownika, 4. Wszystko."))
        except ValueError:
            print("Nie podales cyfry/liczby. Prosze o podanie cyfry/liczby a nie litery/wyrazu.")
            changeUserData(self)

        if whatYouWantChange == 1:
            loginTmp = input('Podaj login uzytkownika ktoremu chcesz zmienic dane: ')
            newLoginTmp = input('Podaj nowy login uzytkownika do zmiany: ')
            for user in self.users:
                if user['Login'] == loginTmp:
                    user['Login'] = newLoginTmp

            with open("data.csv", "w", encoding="utf-8") as newUser:
                fNames = ['Login', 'Pass', 'Function', 'Active']
                data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                data.writeheader()
                for n in self.users:
                    data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})

        if whatYouWantChange == 2:
            loginTmp = input('Podaj login uzytkownika ktoremu chcesz zmienic dane: ')
            newPasswordTmp = input('Podaj nowe haslo uzytkownika: ')
            for user in self.users:
                if user['Login'] == loginTmp:
                    user['Pass'] = newPasswordTmp

            with open("data.csv", "w", encoding="utf-8") as newUser:
                fNames = ['Login', 'Pass', 'Function', 'Active']
                data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                data.writeheader()
                for n in self.users:
                    data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})

        if whatYouWantChange == 3:
            loginTmp = input('Podaj login uzytkownika ktoremu chcesz zmienic dane: ')
            newFunctionTmp = input('Podaj nowa funkcje uzytkownika: ')
            for user in self.users:
                if user['Login'] == loginTmp:
                    user['Function'] = newFunctionTmp

            with open("data.csv", "w", encoding="utf-8") as newUser:
                fNames = ['Login', 'Pass', 'Function', 'Active']
                data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                data.writeheader()
                for n in self.users:
                    data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})

        if whatYouWantChange == 4:
            loginTmp = input('Podaj login uzytkownika ktoremu chcesz zmienic dane: ')
            newDataTmp = []
            seq = ('Login', 'Pass', 'Function', 'Active')
            dataUser = {}
            newDataTmp.append(input('Podaj nowy login uzytkownika do zmiany: '))
            newDataTmp.append(input('Podaj nowe haslo uzytkownika: '))
            newDataTmp.append(input('Podaj nowa funkcje uzytkownika: '))
            newDataTmp.append(input('Podaj czy uzytkownik ma byc aktywny(y/n): '))
            for user in self.users:
                if user['Login'] == loginTmp:
                    user['Login'] = newDataTmp[0]
                    user['Pass'] = newDataTmp[1]
                    user['Function'] = newDataTmp[2]
                    user['Active'] = newDataTmp[3]
            print(self.users)
            with open("data.csv", "w", encoding="utf-8") as newUser:
                fNames = ['Login', 'Pass', 'Function', 'Active']
                data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                data.writeheader()
                for n in self.users:
                    data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})

        if whatYouWantChange > 4:
            print("Nie podales zadnej z podanych mozliwosc. Podaj jeszcze raz.")
            changeUserData(self)

        adminLogin(self)

        print(self.users)

    def banUnban(self):
        loginTmp = input('Podaj login uzytkownika ktorego chcesz zbanowac/odblokowac: ')
        newActiveTmp = input('Ban - y, Odblokowanie - n: ')
        for user in self.users:
            if user['Login'] == loginTmp:
                user['Active'] = newActiveTmp

        with open("data.csv", "w", encoding="utf-8") as newUser:
            fNames = ['Login', 'Pass', 'Function', 'Active']
            data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
            data.writeheader()
            for n in self.users:
                data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function'], 'Active': n['Active']})

        adminLogin(self)

    print(f"Jestes zalogowany jako administrator: {self.userLogin}.")
    print("Funkcje admina: ")
    print("1. Dodanie uzytkownika")
    print("2. Usuniecie uzytkownika")
    print("3. Zablokowanie/Odblokowanie uzytkownika")
    print("4. Zmiana danych uzytkownika")
    print("5. Wyloguj")

    try:
        choice = int(input("Wybierz co chcesz zrobic: "))
    except ValueError:
        print("Nie podales cyfry/liczby. Prosze o podanie cyfry/liczby a nie litery/wyrazu.")
        adminLogin(self)

    if choice == 5:
        Login_module.LoginModule.logOut(self)
    if choice == 1:
        addUser(self)
    if choice == 4:
        changeUserData(self)
    if choice == 2:
        deleteUser(self)
    if choice == 3:
        banUnban(self)
    if choice > 5:
        print("Nie podales zadnej z podanych mozliwosc. Podaj jeszcze raz.")
        adminLogin(self)