from random import randint

def normal_lottery():
    rewards = {1: 200, 2: 100, 3: 50, 4: 20, 5: 0}
    number = randint(1, 100)
    if number == 100:   
        reward = rewards[1]
    elif number >= 95:
        reward = rewards[2]
    elif number >= 80:
        reward = rewards[3]
    elif number >= 30:
        reward = rewards[4]
    else:
        reward = rewards[5]
    return (number, reward)