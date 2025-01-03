# inp_kwargs
**Easily validate user inputs with Python, no hassle required!**

A Python library for easy input validation using kwargs. This library helps to easily validate inputs such as integers, strings, and more, without needing to write complex validation logic.

## Example

### Validating an Integer Input

```python
from inp_kwargs import input_int

# Request a number between 1 and 100
number = input_int("Enter a number between 1 and 100: ", 
                   error_txt="Error: You have to input an integer.",
                   min_value=1, 
                   error_min="Error: The number must be greater than or equal to 1.",
                   max_value=100, 
                   error_max="Error: The number must be less than or equal to 100.")

print(f"You entered: {number}")

# Request a number between 1 and 100 without custom error messages
number = input_int("Enter a number: ", min_value=1, max_value=100)
print(f"You entered: {number}")

```

## Features
- Validate integer inputs with custom error messages.
- Set minimum and maximum value constraints.
- Simple and reusable functions for input validation.


## Installation
You can install inp_kwargs directly from PyPI:
```bash
pip install inp_kwargs
```

## License
MIT License. See the LICENSE file for more details.