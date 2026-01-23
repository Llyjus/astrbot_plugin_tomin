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

                 
                 
        