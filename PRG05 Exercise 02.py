#two main variables
#1)Computer
#2)Human

#Actions:
# PC asking for imput
# Human:input a number
# Comparison by PC: 
# 3x output via Print: (too low/too high/equal)
#________________________________________________

number=99

while number != 100: #the while loop is endless, untill the boolean is False
  
  number=int(input("Please enter a number"))
  if number < 100:
    print("Sorry, your response is too low ")
    
  elif number >100:
    print("Sorry, your response is too high. ")

  else:
    print("You have found the right number!!! Well done!!")