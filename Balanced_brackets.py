#Using stack (the best solution)
class Solution:
   def isValid (self, sequence: str):
       stack = []
       opening = set('([{')
       closing = set(')]}')
       pair = {')' : '(' , ']' : '[' , '}' : '{'}
       for i in sequence :
           if i in opening :
               stack.append(i)
           if i in closing :
               if not stack :
                   return False
               elif stack.pop() != pair[i] :
                   return False
               else :
                   continue
       if not stack :
           return True
       else :
           return False

if __name__ == "__main__":
    sequence1 = input("Enter a string of brackets:")
    print(f"Is {sequence1} valid ? : {Solution().isValid(sequence1)}")
    sequence2 = input("Enter a string of brackets:")
    print(f"Is {sequence2} valid ? : {Solution().isValid (sequence2)}")
#####################################################################
#Time complexity is O(n^2) where the n is total number of characters
#Using while
class Solution:
   def isValid( self, sequence ):
       while True:
           if '()' in sequence :
               sequence = sequence.replace ( '()' , '' )
           elif '{}' in sequence :
               sequence = sequence.replace ( '{}' , '' )
           elif '[]' in sequence :
               sequence = sequence.replace ( '[]' , '' )
           else :
               return not sequence

if __name__ == '__main__':
   sequence1 = input("Enter a string of brackets:")
   print(f'Is {sequence1} valid ? : {Solution().isValid(sequence1)}')
   sequence2 = input("Enter a string of brackets:")
   print(f'Is {sequence2} valid ? : {Solution().isValid (sequence2)}')
