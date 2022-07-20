# Take in 3 parameter s as input

#gives three and compares for the largest
#Thought Process: If num 1 is larger than num 2 then move to compare it to num 3 and if it is greater than num 3 compare num 2 and num 3 and so on...
#actual execution
def max_num(num1, num2, num3):
   if num1 >= num2 and num1 >= num3: #its either true or false, using comparison operators
         return num1
   elif num2 >= num1 and num2 >= num3:
       return num2
   else:
       return num3


# #use function
# #print the function for the max numbers including the parameters used
#
print(max_num(5,25,8))

#can also use other parmameters to compare
