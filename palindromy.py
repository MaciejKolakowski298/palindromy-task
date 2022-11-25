"""
To krótka funkcja do sprawdzenia czy podany wyraz jest palindromem.
Wynik podawany jest jako True/False 
"""
def pali_check(word):
    if str(word)==str(word)[::-1]:
        print("True")
    else:
        print("False")