# Reading the input
num = int(input('Please enter test integer > 2: '))
nex=num
prev=num
# logic to find the next prime
def prev_prime(num1):
  for i in range(2,num1):
    if (num1 % i) == 0:
      return False
  return True

# logic to find the next prime number
prev = prev + 1
while prev_prime(prev) == False:
    prev = prev+ 1
print ('NEXT =',prev)

# logic to find the previous prime number
nex = nex - 1
while prev_prime(nex) == False:
    nex = nex - 1
print ('PREV =',nex)

#Difference between previous prime and next prime
print("Difference =",prev-nex)