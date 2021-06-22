def ispalindrome(word):
    return word == word[::-1]

word = "sos"
correct = ispalindrome(word)
 
if correct:
    print("True")
else:
    print("False")


