'''
n = int(input("write your int number: "))
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 
      
print ("The factorial of",n,"is : ",end="") 
print (fact) 
'''
x = lambda num : 1 if num <= 1 else num*x(num-1)
number = int(input('Enter number: '))
print(x(number))
