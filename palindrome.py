def is_pal(a)
    for n in range(len(a) // 2):
        if a[n] != a[len(a) - n - 1]:
            return False
    return True

is_pal("abcba")


# 1.
a = "abcba"
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
