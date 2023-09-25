import random
list_1 = ['красное', 'черное']

rand_list_1 = random.choice(list_1)
print(rand_list_1)
list_1.remove(rand_list_1)
losing = ' '.join(list_1)
print(losing)
