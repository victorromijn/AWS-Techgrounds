#Write custom function called average()

def average(x,y):
      a = x,y
      return (sum(a)/(len(a)))#with return the value/result of the calculation is stored in the function
 
x = 128
y = 255
z = average(x,y) #now we call/activate the function 'average(x,y)'
print ("The average of",x,"and", y, "is", z)