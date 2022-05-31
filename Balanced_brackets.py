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
