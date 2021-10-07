# We went full Jedi on this one! The result cabn be found underneath!
def average(age_vic,age_mar,age_fad,age_ahm):
      a = [age_vic,age_mar,age_fad,age_ahm]
      return (sum(a)/(len(a)))
#the array exist out of all the -agevic, agemar, etc- variables
#the values will be obtained at a later stage (via the user). 
age_vic=int(input("enter the age Victor :"))
age_mar=int(input("enter the age Mariek :"))
age_fad=int(input("enter the age Fadi :"))
age_ahm=int(input("enter the age Ahmed :"))
#instead of receiving the values, we have chosen to receive the values via the PC user. The code will ask for input. 

Leeftijd = average(age_vic,age_mar,age_fad,age_ahm)
print ("The average of",age_vic,"and", age_mar, "and", age_fad,"and",age_ahm,"is ",Leeftijd)