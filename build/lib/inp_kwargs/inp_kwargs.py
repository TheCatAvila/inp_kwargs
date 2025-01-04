def input_int(prompt, **kwargs):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            # Check if the value is below the specified minimum value|
            if 'min_value' in kwargs and value < kwargs['min_value']:
                min_error_message = kwargs.get('min_value_error_message', None)
                if min_error_message:
                    print(min_error_message)
                continue
            # Check if the value is below the specified maximum value
            if 'max_value' in kwargs and value > kwargs['max_value']:
                max_error_message = kwargs.get('max_value_error_message', None)
                if max_error_message:
                    print(max_error_message)
                continue
            # Check if the value is in the specified range
            if 'range' in kwargs and value not in kwargs['range']:
                range_error_message = kwargs.get('range_error_message', None)
                if range_error_message:
                    print(range_error_message)
                continue
            # Check if the value is in the list of allowed values
            if 'allowed_values' in kwargs and value not in kwargs['allowed_values']:
                allowed_error_message = kwargs.get('allowed_error_message', None)
                if allowed_error_message:
                    print(allowed_error_message)
                continue
            # Check if the value is even
            if 'even' in kwargs and kwargs['even'] and value % 2 != 0:
                even_error_message = kwargs.get('even_error_message', None)
                if even_error_message:
                    print(even_error_message)
                continue
            # Check if the value is odd
            if 'odd' in kwargs and kwargs['odd'] and value % 2 == 0:
                odd_error_message = kwargs.get('odd_error_message', None)
                if odd_error_message:
                    print(odd_error_message)
                continue
            # Check if the value is a multiple of the specified number
            if 'multiple_of' in kwargs and value % kwargs['multiple_of'] != 0:
                multiple_error_message = kwargs.get('multiple_error_message', None)
                if multiple_error_message:
                    print(multiple_error_message)
                continue
            break
        except ValueError:
            if 'type_error_message' in kwargs:
                print(kwargs['type_error_message'])
    return value