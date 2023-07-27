import random

seed = 42
simulations = 1000
n_tries = 50
n_prisoners = 100

outcome = []
random.seed(seed)
for x in range(simulations):
    a = [x for x in range(1,n_prisoners+1)]
    b = random.sample(a, len(a))
    def find_number(number, real_number):
        global count
        count +=1
        number = b[number-1]
        if number == real_number:
            return number
        return find_number(number, real_number)

    new = []
    cont = 0
    for i in range(1,n_prisoners+1):
        count = 0
        find_number(i, i)
        if count <= n_tries:
            new.append(i)
    if len(new)==n_prisoners:
        outcome.append(1)
    else:
        outcome.append(0)

surviving_prisoners = outcome.count(1)
print("The number of times prisoners got away is %d in over %s iterations." %(surviving_prisoners, simulations))
print("The probability of surviving is %s" %(surviving_prisoners/simulations))

