# Boolean And Conditional Logic

## Objectives
- Learn how to get user input in Python
- Learn about "Truthiness"
- Learn how to use comaprison operators to make a basic program


## User Input Function
- There is a built-in function in Python called "<b>input</b>" that will prompt the user and store the result to a variable



# Boolean Expressions

## Conditional Statements
- Conditional logic using if statements represents different paths a program can take based on some type of comparison of input.
  ```python 
  if some condition is True:
     do something
  elif some other condition is True:
     do something
  else:
      do something
  ```

## Conditional Checks
- Conditional logic using if statements represents different paths a program can take based on some tyhpe of comparison of input.
   ```python
    name = "Jon Snow"
    if name == "Arya Stark":
       print("Valar Morghulis")
    elif name == "Jon Snow"
        print("You know nothing")
    else:
        print("Carry on")
   ```
- Conditional logic using multiple elif statements
  ```python
  color = input("what's your favorite color ? ")
  if color == 'purple':
       print("excellent choice! ")
  elif color == 'teal':
       print("not bad! ")
  elif color == 'seafoam':
       print("mediocre ")
  elif color == 'pure darkness':
       print("I like how you think ")
  else:
       print("YOU MONSTER! ")
   ```
## Truthiness & Falsiness
- In Python, all conditional checks resolve to True or False
    ```python
    x = 1
    x is 1 # True
    x is 0 # False
    ```
- We can call values that will resolve to True "truthy", or values that will resolve to False "falsy".
- Besides False conditional checks, other things that are naturally falsy include:
  - empty objects
  - empty strings,
  - None
  - zero

