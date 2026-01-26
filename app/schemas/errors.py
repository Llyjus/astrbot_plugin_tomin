ERROR_MESSAGES = {
      
    'int_type': '请输入一个整数；',
    'string_type': '请输入文本；',
    'float_type': '请输入一个浮点数；'

}

def error_message(e):
        result = ''
        errors = e.errors()
        for error in errors:
            loc = error['loc']
            type = error['type']
            if type in ERROR_MESSAGES:
                result += str(loc) + '：' + ERROR_MESSAGES[type] + '；'
            else:
                result += error['msg']


class App_error(Exception):
    
    #error caused in app
    pass



class Not_enough_fund(App_error):
     pass

class Request_repeat(App_error):
     pass

class Card_already_exists(App_error):
     pass

class Card_not_found(App_error):
     pass

class User_already_exists(App_error):
     pass

class User_not_found(App_error):
     pass

class Illegal_data(App_error):
     pass


class Infra_error(Exception):
     pass

class Database_error(Infra_error):
    #database error
    pass

class Unknown_error(Infra_error):
     pass
                 
                 
        