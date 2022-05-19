#1.
arr = [1, 2, 3, 4, 5];     
print("Original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" "),     
print("Array in reverse order: ");    
for i in range(len(arr)-1, -1, -1):     
    print(arr[i], end=" "), 
    ##As well the loop can be:
    #for x in arr:
    #print(x, end="")
##################################
#2.
arr = [1, 2, 3, 4, 5]
i = len(arr) -1 
while i >= 0 :
    print(arr[i] , end=" ") 
    i -= 1
##################################
# 3.
arr = [1, 2, 3, 4, 5]
for i in reversed(arr) :
    print(i, end= " ")
##################################
# 4.
arr = [1, 2, 3, 4, 5]
[print (i, end =" ") for i in arr[::-1]]
##################################
# 5. 
arr = [1, 2, 3, 4, 5]
[print (i, end=" ") for i in reversed(arr)]
##################################
# 6.
arr = [11, 22, 33, 44, 55]
print("Before reversal Array is :",arr)
 
arr.reverse() #reversing using reverse()
print("After reversing Array:",arr)
####################
# 7.
arr = [12, 34, 56, 78]
print("Original Array is :",arr)
#reversing using reversed()
result=list(reversed(arr))
print("Resultant new reversed Array:",result)

++++++++++++++++++++++++++++++++++

Reverse string:
# 1.
string = "Perdoyawer"
rev = string[::-1]
print(rev)
####################
# 2.
string = "Terdoyawer"
rev = string[slice(None, None, -1)]
print(rev)
####################
# 3.
def reversed_string(text):
     result = ""
     for char in text:
         result = char + result
     return result

out = reversed_string("Hello, World!")
print("the reverse is:", out)
####################
# 4.
def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt )
####################
# 5.
s = "Python" # initial string
reversedString=[]
index = len(s) # calculate length of string and save in index
while index > 0: 
    reversedString += s[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString) # reversed string
####################
# 6.
s = 'Python' #initial string
reversed=''.join(reversed(s)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed) #print the reversed string
####################
# 7.
def reverse_string(string):
	if len(string) == 0:
		return string
	else:
		return reverse_string(string[1:]) + string[0]

rev = reverse_string("Python")
print(rev)
