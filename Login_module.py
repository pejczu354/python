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
import adminLogin
import userLogin as uL

class LoginModule:
    def __init__(self):
        self.users=[]
        with open('data.csv') as myData:
            csvreader = csv.DictReader(myData, delimiter=';')
            for row in csvreader:
                self.users.append(row)
                print(row)

    def logIn(self):
        numbersOfAttempt = 3
        attempt = True
        helpingVar = 0
        while attempt:
            self.userLogin = input("Podaj login: ")
            userPass = input("Podaj haslo: ")
            i=0
            for user in self.users:
                i+=1
                if user['Login']==self.userLogin and user['Pass']==userPass:
                    if user['Function']=='admin':
                        if user['Active'] == 'y':
                            adminLogin.adminLogin(self)
                            attempt = False
                            break
                        else:
                            print('Twoje konto zostalo zablokowane.')
                    elif user['Function']=='user':
                        if user['Active'] == 'y':
                            uL.userLogin(self)
                            attempt = False
                            break
                        else:
                            print('Twoje konto zostalo zablokowane.')
                elif i>=len(self.users):
                    helpingVar += 1
                    print('Logowanie nieudane.')
                    print('Sprobuj ponownie. Pozostały Ci ',numbersOfAttempt-helpingVar,' proby.')
                    if helpingVar >= 3:
                        print("Niestety wykorzystales wszystkie proby.")
                        attempt = False

    def logOut(self):
        print("Zostales wylogowany.")
        print("Jezeli chcesz ponownie sie zalogowac wybierz 1. Jeżeli chcesz wyjsc wpisz jakakolwiek liczbe naturalna rozna od 1.")

        try:
            choice = int(input("Dokonaj wyboru: "))
        except ValueError:
            print("Nie podales cyfry/liczby. Prosze o podanie cyfry/liczby a nie litery/wyrazu.")
            self.logOut()

        if choice == 1:
            try:
                self.logIn()
            except KeyboardInterrupt:
                print("Logowanie niepowiodło się.")
        if choice != 1:
            exit()

    def printUserData(self):
        for user in self.users:
            if user['Login'] == self.userLogin:
                print('Twoj login: ',user['Login'])
                print('Twoje haslo: ',user['Pass'])
                print('Twoja funkcja: ',user['Function'])