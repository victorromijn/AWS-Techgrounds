"""a_dictiorary = {'First name ':'Coen' , 'Last name ' : 'Meulenkamp' , 'Job Title ' : ' Learning Coach' , 'Company ' : ' TechGrounds'}
for k,v in a_dictiorary.items():
    print(k,v)"""

h_a='First name:'
h_b='Last name:'
h_c='Job title:'
h_d='Company:'
h_totaal=(h_a,h_b,h_c,h_d)
print(h_totaal)
#writer.writerow(header)

dict = {}
a = input('first name: ')
b = input('last name: ')
c = input('job title: ')
d = input('company: ')
print({a, b, c, d})
#writer.writerow(data)

#import csv
#
#header = ['name', 'area', 'country_code2', 'country_code3']
#data = ['Afghanistan', 652090, 'AF', 'AFG']
#
#with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#    writer = csv.writer(f)
#
    # write the header
#    writer.writerow(header)
#
#    # write the data
#    writer.writerow(data)