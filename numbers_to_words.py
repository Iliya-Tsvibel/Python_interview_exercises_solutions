#1.
arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
def number_to_word(n):
    if(n==0):
        return ''
     
    else:
        words_from_arr = arr[n%10]
        res = number_to_word(int(n/10)) + words_from_arr + " "
        
    return res
 
n = int(input("Enter number in any range:"))
print("Entered number is : ", n)
print("Number in words: ",end="")
print(number_to_word(n))
###########################################
