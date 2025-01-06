from os import system

def clear_and_print(message, clear_console):
    """Clear the console and print a message, if specified."""
    if clear_console:
        system("cls")
    if message:
        print(message)

def validate_number(prompt, value_type, **kwargs):
    """
    Validate user input against multiple criteria.

    Args:
        prompt (str): The input prompt.
        value_type (type): The desired type of the input (e.g., int or float).
        kwargs: Additional keyword arguments for validation.

    Returns:
        value_type: The validated input value.
    """
    # Default error messages
    default_messages = {
        'min_value_error_message': "The value must be greater than or equal to the minimum allowed.",
        'max_value_error_message': "The value must be less than or equal to the maximum allowed.",
        'range_error_message': "The value is not within the allowed range.",
        'allowed_values_error_message': "The value is not in the list of allowed values.",
        'even_error_message': "The value must be an even number.",
        'odd_error_message': "The value must be an odd number.",
        'multiple_of_error_message': "The value must be a multiple of the specified number.",
        'type_error_message': "Invalid input type. Please enter a valid number."
    }

    while True:
        value = input(prompt)
        try:
            value = value_type(value)  # Convert to the desired type

            # Validation criteria and corresponding error messages
            validations = [
                (lambda v: 'min_value' not in kwargs or v >= kwargs['min_value'],
                 kwargs.get('min_value_error_message', default_messages['min_value_error_message'])),
                (lambda v: 'max_value' not in kwargs or v <= kwargs['max_value'],
                 kwargs.get('max_value_error_message', default_messages['max_value_error_message'])),
                (lambda v: 'range' not in kwargs or v in kwargs['range'],
                 kwargs.get('range_error_message', default_messages['range_error_message'])),
                (lambda v: 'allowed_values' not in kwargs or v in kwargs['allowed_values'],
                 kwargs.get('allowed_values_error_message', default_messages['allowed_values_error_message'])),
                (lambda v: 'even' not in kwargs or (kwargs['even'] and v % 2 == 0),
                 kwargs.get('even_error_message', default_messages['even_error_message'])),
                (lambda v: 'odd' not in kwargs or (kwargs['odd'] and v % 2 != 0),
                 kwargs.get('odd_error_message', default_messages['odd_error_message'])),
                (lambda v: 'multiple_of' not in kwargs or v % kwargs['multiple_of'] == 0,
                 kwargs.get('multiple_of_error_message', default_messages['multiple_of_error_message'])),
            ]

            # Iterate through validations
            for validate, error_message in validations:
                if not validate(value):
                    if error_message:  # Show message only if not None/False
                        clear_and_print(error_message, kwargs.get("clear_console", False))
                    break
            else:
                # If all validations pass, return the value
                return value

        except ValueError:
            clear_and_print(kwargs.get('type_error_message', default_messages['type_error_message']),
                            kwargs.get("clear_console", False))


def input_int(prompt, **kwargs):
    return validate_number(prompt, int, **kwargs)

def input_float(prompt, **kwargs):
    return validate_number(prompt, float, **kwargs)

# String input function with keyword arguments for validation
def validate_string(prompt, **kwargs):
    """
    Validate user input as a string against multiple criteria.

    Args:
        prompt (str): The input prompt.
        kwargs: Additional keyword arguments for validation.

    Returns:
        str: The validated input string.
    """
    # Default error messages
    default_messages = {
        'strip_error_message': "The input cannot be empty after removing spaces.",
        'min_length_error_message': "The input is too short.",
        'max_length_error_message': "The input is too long.",
        'allowed_characters_error_message': "The input contains invalid characters.",
        'pattern_error_message': "The input does not match the required pattern."
    }

    while True:
        value = input(prompt)

        # Preprocessing options
        if kwargs.get("strip", False):
            value = value.strip()
        if kwargs.get("remove_spaces", False):
            value = value.replace(" ", "")
        if kwargs.get("uppercase", False):
            value = value.upper()
        if kwargs.get("lowercase", False):
            value = value.lower()

        # Validation criteria and corresponding error messages
        validations = [
            (lambda v: not kwargs.get("strip", False) or v, 
             kwargs.get("strip_error_message", default_messages['strip_error_message'])),
            (lambda v: "min_length" not in kwargs or len(v) >= kwargs["min_length"], 
             kwargs.get("min_length_error_message", default_messages['min_length_error_message'])),
            (lambda v: "max_length" not in kwargs or len(v) <= kwargs["max_length"], 
             kwargs.get("max_length_error_message", default_messages['max_length_error_message'])),
            (lambda v: "allowed_characters" not in kwargs or all(c in kwargs["allowed_characters"] for c in v), 
             kwargs.get("allowed_characters_error_message", default_messages['allowed_characters_error_message'])),
            (lambda v: "pattern" not in kwargs or __import__("re").match(kwargs["pattern"], v), 
             kwargs.get("pattern_error_message", default_messages['pattern_error_message'])),
        ]

        # Iterate through validations
        for validate, error_message in validations:
            if not validate(value):
                if error_message:  # Show message only if not None/False
                    clear_and_print(error_message, kwargs.get("clear_console", False))
                break
        else:
            # If all validations pass, return the string
            return value


def input_str(prompt, **kwargs):
    return validate_string(prompt, **kwargs)

test = input_int("Enter a number: ")