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
    try:

        if band in working_dict[place]:
            base = working_dict[place][band]
        else:
            base = 1
    except KeyError as e:
        raise KeyError('没有这个工作地点！请检查地点名称是否正确！') from e

    if rarity == 6:
        base *= 3
    elif rarity == 5:
        base *= 2
    elif rarity == 4:
        base *= 1.5

    
    end_time = current_time + hours*3600
    
    wage_per_hour = 2
    wage = ceil(wage_per_hour * base * min(hours, 3))+ ceil((wage_per_hour/2) * base * max(hours - 3, 0))

    return {'wage': wage, 'end_time': end_time}


    