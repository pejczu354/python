#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      172484
#
# Created:     24-05-2018
# Copyright:   (c) 172484 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv

class LoginModule:
    def __init__(self):
        self.users=[]
        with open('data.csv') as myData:
            csvreader = csv.DictReader(myData, delimiter=';')
            for row in csvreader:
                self.users.append(row)
                print(row)

    def logIn(self,userLogin,userPass):
        self.userLogin = userLogin
        self.userPass = userPass
        def userLogin(self):
            print(f"Jestes zalogowany jako uzytkownik: {self.userLogin}.")
            print("Funkcje uzytkownika:")
            print("1. Wyswietl moje dane")
            print("2. Zmien moje dane")
            print("3. Wyloguj")
            choice = int(input("Wybierz co chcesz zrobic: "))
            if choice == 3:
                self.logOut()

        def adminLogin(self):
            def addUser(self):
                try:
                    uLogin = input("Podaj login nowego uzytkownika: ")
                    uPass = input("Podaj haslo nowego uzytkownika: ")
                    uFunction = input("Podaj funkcję uzytkownika(user/admin): ")
                except KeyboardInterrupt:
                    print("Nieudane pobranie danych o uzytkowniku.")

                dataUser = {'Login':uLogin,'Pass':uPass,'Function':uFunction}
                userStruct = [dataUser]
                print(dataUser)
                with open("data.csv", "a", encoding="utf-8") as newUser:
                    fNames = ['Login', 'Pass', 'Function']
                    data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                    for n in userStruct:
                        data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function']})

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
                        fNames = ['Login', 'Pass', 'Function']
                        data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                        data.writeheader()
                        for n in self.users:
                            data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function']})

            def changeUserData(self):
                whatYouWantChange = int(input("1. Zmiana loginu uzytkownika, 2. Zmiana hasla uzytkownika, 3. Zmiana funkcji uzytkownika, 4. Wszystko."))

                if whatYouWantChange == 1:
                    loginTmp = input('Podaj login uzytkownika ktoremu chcesz zmienic dane: ')
                    newLoginTmp = input('Podaj nowy login uzytkownika do zmiany: ')
                    for user in self.users:
                        if user['Login'] == loginTmp:
                            user['Login'] = newLoginTmp

                    with open("data.csv", "w", encoding="utf-8") as newUser:
                        fNames = ['Login', 'Pass', 'Function']
                        data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                        data.writeheader()
                        for n in self.users:
                            data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function']})

                if whatYouWantChange == 2:
                    loginTmp = input('Podaj login uzytkownika ktoremu chcesz zmienic dane: ')
                    newPasswordTmp = input('Podaj nowe haslo uzytkownika: ')
                    for user in self.users:
                        if user['Login'] == loginTmp:
                            user['Pass'] = newPasswordTmp

                    with open("data.csv", "w", encoding="utf-8") as newUser:
                        fNames = ['Login', 'Pass', 'Function']
                        data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                        data.writeheader()
                        for n in self.users:
                            data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function']})

                if whatYouWantChange == 3:
                    loginTmp = input('Podaj login uzytkownika ktoremu chcesz zmienic dane: ')
                    newFunctionTmp = input('Podaj nowa funkcje uzytkownika: ')
                    for user in self.users:
                        if user['Login'] == loginTmp:
                            user['Function'] = newFunctionTmp

                    with open("data.csv", "w", encoding="utf-8") as newUser:
                        fNames = ['Login', 'Pass', 'Function']
                        data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                        data.writeheader()
                        for n in self.users:
                            data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function']})

                if whatYouWantChange == 4:
                    loginTmp = input('Podaj login uzytkownika ktoremu chcesz zmienic dane: ')
                    newDataTmp = []
                    newDataTmp.append(input('Podaj nowy login uzytkownika do zmiany: '))
                    newDataTmp.append(input('Podaj nowe haslo uzytkownika: '))
                    newDataTmp.append(input('Podaj nowa funkcje uzytkownika: '))
                    for user in self.users:
                        if user['Login'] == loginTmp:
                            user['Login'] = newDataTmp[0]
                            user['Pass'] = newDataTmp[1]
                            user['Function'] = newDataTmp[2]

                    dataUser = {'Login':uLogin,'Pass':uPass,'Function':uFunction}
                    userStruct = [dataUser]
                    with open("data.csv", "w", encoding="utf-8") as newUser:
                        fNames = ['Login', 'Pass', 'Function']
                        data = csv.DictWriter(newUser, fieldnames=fNames, delimiter=';')
                        data.writeheader()
                        for n in userStruct:
                            data.writerow({'Login': n['Login'],'Pass': n['Pass'], 'Function': n['Function']})

                print(self.users)

            print(f"Jestes zalogowany jako administrator: {self.userLogin}.")
            print("Funkcje admina: ")
            print("1. Dodanie uzytkownika")
            print("2. Usuniecie uzytkownika")
            print("3. Zablokowanie/Odblokowanie uzytkownika")
            print("4. Zmiana danych uzytkownika")
            print("5. Wyloguj")
            choice = int(input("Wybierz co chcesz zrobic: "))
            if choice == 5:
                self.logOut()
            if choice == 1:
                addUser(self)
            if choice == 4:
                changeUserData(self)
            if choice == 2:
                deleteUser(self)


        for user in self.users:
            if user['Login']==self.userLogin and user['Pass']==self.userPass:
                if(user['Function']=='user'):
                    userLogin(self)
                if(user['Function']=='admin'):
                    adminLogin(self)

        print('Logowanie nieudane.')


    def logOut(self):
        print("Zostales wylogowany.")
        print("Jezeli chcesz ponownie sie zalogowac wybierz 1. Jeżeli chcesz wyjsc wybierz 2.")

        choice = int(input("Dokonaj wyboru: "))
        if choice == 1:
            try:
                login = input("Podaj login: ")
                haslo = input("Podaj haslo: ")
                self.logIn(login,haslo)
            except KeyboardInterrupt:
                print("Logowanie niepowiodło się.")
        if choice == 2:
            exit()

c=LoginModule()
try:
    login = input("Podaj login: ")
    haslo = input("Podaj haslo: ")
    c.logIn(login,haslo)
except KeyboardInterrupt:
    print("Logowanie nieudane.")