from app.working import working_func

def test_wage_calc():

    place = "SPACE"
    band = "popipa" 
    hours = 2
    now = 1000
    
    # rarity 6 test
    result1 = working_func(band, 6, place, hours, current_time=now)
    assert result1['wage'] == 90
    assert result1['end_time'] == now + 2 * 3600

    # rarity 5 test
    result2 = working_func(band, 5, place, hours, current_time=now)
    assert result2['wage'] == 60

    # rarity 3 test
    result3 = working_func(band, 3, place, hours, current_time=now)
    assert result3['wage'] == 42

    # no buff
    result4 = working_func("toge", 1, place, hours, current_time=now)
    assert result4['wage'] == 20

    result5 = working_func(band, 1, place, 4, current_time=now)
    assert result5['wage'] == 53