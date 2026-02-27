from time import time
from math import ceil

from app.working.up_for_band import working_dict



def working_func(band:str, 
            rarity:int, 
            place:str, 
            hours:int, 
            *, 
            current_time = None)->dict:

    if current_time is None:
        current_time = int(time())

    #calculate the wage and the end time of working

    if band in working_dict[place]:
        base = working_dict[place][band]
    else:
        base = 1

    if rarity == 6:
        base *= 3
    elif rarity == 5:
        base *= 2
    else:
        base *= 1 + 0.2*(rarity - 1)

    
    end_time = current_time + hours*3600
    
    wage = ceil(10 * base * hours)

    return {'wage': wage, 'end_time': end_time}


    