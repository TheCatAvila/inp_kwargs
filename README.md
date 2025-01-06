# inp_kwargs
**Easily validate user inputs with Python, no hassle required!**

A Python library for easy input validation using kwargs. This library helps to easily validate inputs such as integers, strings, and more, without needing to write complex validation logic. Additionally, these functions prevent the program from crashing due to invalid inputs, ensuring a robust and user-friendly experience.

## Example

### Validating an Integer Input

```python
from inp_kwargs import input_int

# Basic integer validation
# Ensures the program won't crash even if the user enters invalid data (e.g., a string).
test = input_int("Enter a number: ")
print(f"You entered: {test}")

# Request a number between 1 and 100
number = input_int("Enter a number between 1 and 100: ",
                   min_value=1,
                   max_value=100)

print(f"You entered: {number}")

# Request a number with custom error messages
number = input_int("Enter a number: ",
                   min_value=1,
                   max_value=100,
                   min_value_error_message="Error: Must be >= 1.",
                   max_value_error_message="Error: Must be <= 100.")
print(f"You entered: {number}")
```

## Available Functions
### 1. `input_int`
   Validate integer inputs with customizable criteria.

   #### Parameters:
   - **min_value** (*int*, optional): Minimum value allowed.
   - **max_value** (*int*, optional): Maximum value allowed.
   - **range** (*list*, optional): Restrict input to a specific range of values.
   - **allowed_values** (*list*, optional): Accept only specific values.
   - **even** (*bool*, optional): Ensure the number is even.
   - **odd** (*bool*, optional): Ensure the number is odd.
   - **multiple_of** (*int*, optional): Validate input is a multiple of the given number.
   - **type_error_message** (*str*, optional): Error message for invalid type.
   - **clear_console** (*bool*, optional): Clears the console after each invalid input.

   #### Example:
   ```python
   from inp_kwargs import input_int

   number = input_int("Enter a number: ", min_value=1, max_value=10, even=True)
   print(f"Validated number: {number}")
   ```

---

### 2. `input_float`
   Validate float inputs with customizable criteria.

   #### Parameters:
   Similar to `input_int`, but for float values.

   #### Example:
   ```python
   from inp_kwargs import input_float

   number = input_float("Enter a decimal number: ", min_value=0.5, max_value=9.9)
   print(f"Validated float: {number}")
   ```

---

### 3. `input_str`
   Validate string inputs with customizable criteria.

   #### Parameters:
   - **strip** (*bool*, optional): Remove leading and trailing spaces.
   - **min_length** (*int*, optional): Minimum string length.
   - **max_length** (*int*, optional): Maximum string length.
   - **allowed_characters** (*str*, optional): Restrict characters in input.
   - **pattern** (*str*, optional): Validate input using a regex pattern.
   - **clear_console** (*bool*, optional): Clears the console after each invalid input.
   - **strip_error_message** (*str*, optional): Message when string is empty after trimming.
   - **min_length_error_message** (*str*, optional): Error message for short strings.
   - **max_length_error_message** (*str*, optional): Error message for long strings.

   #### Example:
   ```python
   from inp_kwargs import input_str

   text = input_str("Enter a word: ", min_length=3, max_length=8, strip=True, allowed_characters="abcdefghijklmnopqrstuvwxyz")
   print(f"Validated string: {text}")
   ```

---

### Function Dictionary
| Function Name | Purpose                        | Input Type |
|---------------|--------------------------------|------------|
| `input_int`   | Validate integer inputs        | Integer    |
| `input_float` | Validate float inputs          | Float      |
| `input_str`   | Validate string inputs         | String     |

## Features
- Customizable validation for integers, floats, and strings.
- Supports custom error messages or default messages for ease of use.
- Clears the console between attempts for a clean interface.
- Handles common validation needs such as ranges, patterns, and allowed values.

## Installation
You can install `inp_kwargs` directly from PyPI:
```bash
pip install inp_kwargs
```

## License
MIT License. See the LICENSE file for more details.

