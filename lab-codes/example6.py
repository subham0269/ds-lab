count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("=======================================")


for letter in 'Python':     # First Example
   print ('Current Letter :', letter)
   
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print ('Current fruit :', fruit)

print ("-----------------------------------------")


i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) :
       print (i, " is prime")
       i = i + 1

print ("Good bye!")
