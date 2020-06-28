"""
Towobola
27 June 2020
UCLA EXTENSION
Python Programming 
Programming Exercise 1
This program provides user feedback on simple 
arithmetic and logical operations on 2 numbers
"""


#User instructions
print('Welcome. This is a simple program which helps understand numerical quantities')
print('Note that this program is limited to integer entries, other characters will be ignored')


#parse out non-integers
def number_extractor(order):

  s=input(order+' value: ')
  
  number=''
  for t in range(len(s)):
    try:
      number=number+str(int(s[t]))
    except ValueError:
      print("The character", s[t], "will be ignored")
  if number=='':
    return 0
  else:
    return int(number)

#collect numbers from user
first=number_extractor('First')
second=number_extractor('Second')

#User feedback on added number
print(first, ' + ', second,' = ',(first+second))

#User feedback on number subtraction
print(first, ' - ', second,' = ',(first-second))

#User feedback on number comparison
print(first, ' = ', second,' = ',(first==second))

print(first, ' is not equal to ', second,' ',(first==second))


#Some of the algorithm was adapted from https://www.w3schools.com/python/ref_string_split.asp