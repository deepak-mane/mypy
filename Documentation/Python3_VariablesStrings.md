# Variables & Strings

## Naming Restrictions
1. Variables must start with letter or underscore, cannot start with NUMBER.
   - _cats - OK
   - 2cats - Not OK
2. Rest of name mist consist of letters numbers.
   - cats2 - OK
   - hey@you - Not OK
3. Names are case sensitive
   - CATS != Cats
   - Cats != cats
   
   
## Naming Conventions
1. Most variables should be snake_case
2. Most variables should be lowercase, with some exceptions
   - CAPITAL_SNAKE_CASE usually refers to constatns
3. Variables with double underscore "called as dunders" are supposed to be private and not messed
   - __not__touchy


# Data Types
In any assignment, the assigned value must always be a valid data type.
- Python Data Types Includes :

|<b>Data Type<b/>|<b>Description<b/>|
|---|---|
|bool|True or False values|
|int|an integer (1,2,3)|
|str|(string) a sequence of Unicode characters, e.g "Deepak"|
|list|an ordered sequence of values of other data ty[es|
|dict|a collection of key: values, e.g {"first_name":"Deepak","last_name":"Mane"}|


# Dynamic Typing
- Python is highly flexible about reassigning variables to different types.
- We call this dynamic typing, since variables can change types readily.
- Other languages like C++ are statically typed and variables are originally stuck with their originally-assigned type.

# Special Value None
- The purpose of None is to represent NULL. (nothingness)
- to set a variable to be explicitly to null,
- child = None
- instead of using child = "" , when you use None the variable is created as container with None Type

# Declaration Strings
- ' ' or " "
- Can use Quotes in Quotes ' " " ' or "  ' ' "

# String Escape Characters/Sequences
- In Python there are also "escape characters", which are "metacharacters" - they get interpreted by Python to do something special.
- ' \n ' : puts new line when used in print()
- ' \\ ' : Use Double back Slash to use one back slash
- ' \b ' : e.g str = "hel\blo" gives print(str) as helo.
- ' \ ' ': here single quote is escaped using back slash.

# String Concatenation
- Concatenation is combining multiple strings together. In Python you can do this simply with the "+" operator.
    ```python
    str_one = "your"
    str_two = "face"
    str_three = str_one + str_two
    print(str_three)
    ```
- str + str = str
- str + int = weired result, error.
- " += " is a nice operator when assigning operators in strings
    ```name = name + " steele" is name += " steele"```

# String Formatting
- There are also several ways to format strings in Python to <b>interplate</b> variables.
- The new way(new in Python 3.6+) => F-Strings
  ```python 
  x = 10
  formatted = f"I 'v told you {x} times already!"
  
  guess = 8
  print(f"your guess of {guess + 1} was incorrect!")
  >>>your guess of 9 was incorrect!```

- The tried-and-true way(Python 2 -> 3.5) => <b>.format method</b>
  ```python 
  x = 10
  formatted = "I 'v told you {} times already!".format(10)```
  

- The OLD way => <b>% operator</b>(deprecated)
  ```python 
  x = 10
  formatted = "I 'v told you %d times already!" % (x)
  ```

# Strings and Indices
- Every character in string is index starting with '0' index
  ```python 
  >>>name = "Chuck"
  >>>name[0]
  'C'
  ```
- Negative One '-1' index gives the last character of the string
  ```python
  >>>name[-1]
  'k'
  ```
# Converting Data Types
- In string interpolation, data types are implicitly converted into  string form(more on this later in OOP)
- You can also explicity convert variables by using the name of the builtin type as a function
  ```python
   >>>decimal = 12.5656565656
   >>>int(decimal)
   12
   
   >>>my_list = [1, 2, 3]
   >>>my_list_as_a_string = str(my_list)  # "[1, 2, 3]"
   ```



  