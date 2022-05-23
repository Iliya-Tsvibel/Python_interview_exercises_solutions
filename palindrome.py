# 1.
#Read about Big O notation: https://en.wikipedia.org/wiki/Big_O_notation
#This first solution optimized for CPU, unlike subsequent additional solutions.
def is_pal(a):
    for n in range(len(a) // 2):
        if a[n] != a[len(a) - n - 1]:
            return False
    return True

res = is_pal("abcba")
print (res)
####################
# 2.
def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
####################
# 3.
a = "abcba"
b = a[::-1]
if a == b:
    print("the word", a, "is palindrome")
else:
    print("the word", a, "is not palindrome")
####################
# 4. 
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
# 5.
def checkPalindrome(s):
    return list(s) == list(reversed(s))

var = "Madam"
var_lower = var.lower()
a = checkPalindrome(var_lower)
if(a ==True):
    print (f"{var} is a palindrome")
else:
    print (f"{var} is not a palindrome")
