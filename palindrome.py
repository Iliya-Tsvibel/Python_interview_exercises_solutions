# 1.
#Read about Big O notation: https://en.wikipedia.org/wiki/Big_O_notation
#Good article: https://javascript.plainenglish.io/the-best-and-worst-way-of-solving-the-palindrome-question-4b7d2f9ada06
#Additional explanation: https://stackoverflow.com/questions/24153433/complexity-of-palindrome-test
#Examples on JS: https://learnersbucket.com/examples/algorithms/palindrome-string/
#IA normal list :

# Append : O(1)
# Extend : O(k) - k is the length of the extension
# Index : O(1)
# Slice : O(k)
# Sort : O(n log n) - n is the length of the list
# Len : O(1)
# Pop : O(1) - pop from end
# Insert : O(n) - n is the length of the list
# Del : O(n) - n is the length of the list
# In : O(n) - n is the length of the list
# + : O(m + n) - m & n are the length of the lists - this creates a new list object
# += : O(n) - n is the length of the list being added - list is extended.


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
