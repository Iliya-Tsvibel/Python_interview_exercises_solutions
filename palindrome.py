# 1.
a = "Pop"
b = a.lower()
c = a[::-1]
if a == c:
    print("the word", a, "is palindrome")
else:
    print("the word", a, "is not palindrome")
####################
# 2. 
x = "maLayalam"
y = x.lower()
w = ""
for i in y:
    w = i + w
 
if (y == w):
    print("Yes")
else:
    print("No")
####################
# 3.
def checkPalindrome(s):
    return list(s) == list(reversed(s))

var = "Madam"
var_lower = var.lower()
a = checkPalindrome(var_lower)
if(a ==True):
    print (f"{var} is a palindrome")
else:
    print (f"{var} is not a palindrome")