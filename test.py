
import random

def generate_prisoner(number_prisoners):
    list = []
    cont = 0
    while cont < (number_prisoners):
        cont +=1
        list.append(cont)
    return list

#Generated prisoners
a = generate_prisoner(100)
print(a)

#Hidden prisoners name
import random
b = random.sample(a, len(a))
print(b)
#count = 0

#real_number = a[prisoner_tag-1]
def find_number(number, real_number):
    global count
    count +=1
    number = b[number-1]
    #print(number)

    if number == real_number:
        return number
    return find_number(number, real_number)

#Prisoner uses the algorithm and tries to find his box
#Random prisoner enters the cage

#prisoner_tag = 1

#prisoner_1 = find_number(prisoner_tag, prisoner_tag)
#print('Prisoner %d found his name after opening %d boxes'%(prisoner_tag,count))
new = []
cont = 0
for i in range(1,101):
    count = 0
    find_number(i, i)
    print('Prisoner %d found his name after opening %d boxes' % (i, count))
    if count <= 50:
        new.append(i)
        #50 % chance to find his name
        print('Prisoner %d managed to pass'%i)

#print(len(new))

if len(new)==100:
    print("Prisoners survived!")
else:
    print("Prisoners are all executed")

