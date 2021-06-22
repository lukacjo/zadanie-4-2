def ispalindrome(word):
    return word == word[::-1]

word = "sos"
correct = ispalindrome(word)
 
if correct:
    print("True")
else:
    print("False")


"""
kiedy słowo jest palindromem?
porównanie ilości znaków żeby byla taka sama
odwrócenie słowa
iteracyjne porównanie kazdej litery, jeżeli inna =false
tez mozna powiedzieć że każde które ma mniej niż 2 znaki ale to takie meh
"""