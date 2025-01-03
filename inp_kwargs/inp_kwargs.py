def input_int(inp_txt, **kwargs):
    while True:
        value = input(inp_txt)
        try:
            value = int(value)
            if 'min_value' in kwargs and value < kwargs['min_value']:
                print(kwargs.get('error_min', f"Debe ser mayor o igual a {kwargs['min_value']}"))
                continue
            if 'max_value' in kwargs and value > kwargs['max_value']:
                print(kwargs.get('error_max', f"Debe ser menor o igual a {kwargs['max_value']}"))
                continue
            break
        except ValueError:
            if 'error_txt' in kwargs:
                print(kwargs['error_txt'])
    return value