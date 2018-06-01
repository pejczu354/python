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
from Login_module import LoginModule

def main():
    #try:
    login = LoginModule()
    login.logIn()
    #except:
        #print("Nie udało się zainicjowac zmiennej klasowej.")
if __name__ == '__main__':
    main()