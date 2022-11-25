"""
To krótka funkcja do sprawdzenia czy podany wyraz jest palindromem.
Wynik podawany jest jako True/False 
"""
def pali_check(word):
    if str(word.lower())==str(word.lower())[::-1]:
        print("True")
    else:
        print("False")
pali_check("kAJaK")