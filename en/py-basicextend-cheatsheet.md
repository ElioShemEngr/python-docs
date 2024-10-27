# PYTHON Basics Extend - CheatSheet 🐍

### 1. COMMENTS
```python
# This is a comment on one line

'''
This is a
comment
on multiple
lines
'''
```

### 2. DATA TYPES
```python
my_string = "My first string"       # String
my_other_string = 'My other string' # String
my_int = 1                          # Integer
my_float = 3.14                     # Float
my_bool = True                      # Boolean
my_bool = False                     # Boolean
my_null = None                      # Nulls

# --------------------
# Data Hints
# Type labels only help to improve the readability and documentation of the code.
my_int: int = 2
my_float: float = 5.12
my_bool: bool = True
my_bool: bool = False
my_string: str = "My first string with label"
my_other_string: str = 'My other string with label'

def sumar(a: int, b: int) -> int: # Hints in function
    return a + b

# --------------------
# Casting
# specify the data type of a variable
x = str(3)    # x will be '3' (String)
y = int(3)    # y will be 3 (Integer)
z = float(3)  # z will be 3.0 (Floating)
```

### 3. VARIABLES

```python
# --------------------
# VALID VARIABLES:
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2

# --------------------
# NO VALID VARIABLES
first-name
first@name
first$name
first name
num-1
1num
```

### 4. PRINT()
```python
# print() : Display information in the console
print("Hello, World!")      # print a string

name = "John"
age = 22
print(nombre)                       # Print the value of the variable 'name'
print("Name:", name, "Age:", age)   # Print multiple values

# --------------------
# end= : Specify the end of printing
print("Hello", end="-")     # Ends output with a dash instead of a line break
print("World")              # It is printed on the same line
# Output > Hello-World

# --------------------
# sep= : Specify the sep of printing
print("John", "Anny", "Louis", sep="_")  # We use underscore(_) as separator
# Output > John_Anny_Luis

list_num = [1, 2, 3, 4, 5]
print(*list_num, sep=" - ")  # The * operator decomposes the list
# Output > 1 - 2 - 3 - 4 - 5

# --------------------
# f-strings and format table with f-strings
name = "John"
age = 22
print(f"My name is {name} and I'm {age} years old")
# Output > My name is John and I'm 22 years old

data_list = [("John", 22), ("Louis", 30)]
for name, age in data_list:
    print(f"Name: {name:10} | Age: {age:3}")
# Output >
# Name: John        | Age:  22
# Name: Louis       | Age:  30
```

## 5. TYPE()
```python
# type() : Checking Data Types
print(type(10))                  # Output > <class 'int'>
print(type(3.14))                # Output > <class 'float'>
print(type(1 + 3j))              # Output > <class 'complex'>
print(type('Asabeneh'))          # Output > <class 'str'>
print(type([1, 2, 3]))           # Output > <class 'list'>
print(type({'name':'Asabeneh'})) # Output > <class 'dict'>
print(type({9.8, 3.14, 2.7}))    # Output > <class 'set'>
print(type((9.8, 3.14, 2.7)))    # Output > <class 'tuple'>

# --------------------
# Checking types in function or return
def sum(a, b):
    return a + b

total = sum(3, 4)
print(type(total))  # Output > <class 'int'>

# --------------------
# Checking if the object is instance of the Class
class Person:
    pass

p = Person()
print(type(p))  # Output > <class '__main__.Person'>
```

## 6. INPUT()
```python
# input() : The data type received is a string
name = input("¿What's your name? ")
print(f"Hola, {name}!")

# --------------------
# Receive multiple values
values = input("Enter three numbers separated by commas: ")
list_values = values.split(",")  # Divide the input for commas
print("The numbers are:", list_values)

# --------------------
# Convert data type in the Input (str -> int and str -> float )

age = int(input("How old are you? ")) # Convert (str -> int) 
print(f"You have {age} years old")

weigth = float(input("What is your weight in kg? ")) # Convert (str -> float) 
print(f"Your weigth is {weigth} kg.")

# Convert two numbers and sum
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}.")
```

## 7. OPERATORS

1. **Arithmetic operators**
2. **Assignment operators**
3. **Comparison operators**
4. **Logical operators**
5. **Identity operators**
6. **Membership operators**

### 7.1 **Arithmetic operators**

|Operator|Description     |Example |Result|
|--------|----------------|------- |------|
|`+`     |Sum             |`5 + 3` |`8`   |
|`-`     |Rest            |`5 - 3` |`2`   |
|`*`     |Multiplication  |`5 * 3` |`15`  |
|`/`     |Division        |`5 / 2` |`2.5` |
|`//`    |Integer Division|`5 // 2`|`2`   |
|`%`     |Module          |`5 % 2` |`1`   |
|`**`    |Exponent        |`2 ** 3`|`8`   |

```python
a = 10
b = 3

result_sum = a + b         # 13
result_mult = a * b        # 30
result_div = a / b         # 3.33333
integer_div = a // b       # 3
result_mod = a % b         # 1
result_pow = a ** b        # 1000
```

### 7.2 **Assignment operators**

| Operator | Description                      | Example   | Equivalente a |
| -------- | ------------------------------   | --------- | ------------- |
| `=`      | Simple assignment                | `x = 5`   | `x = 5`       |
| `+=`     | Assignment with sum              | `x += 3`  | `x = x + 3`   |
| `-=`     | Assignment with subtraction      | `x -= 2`  | `x = x - 2`   |
| `*=`     | Assignment with multiplication   | `x *= 3`  | `x = x * 3`   |
| `/=`     | Assignment with division         | `x /= 2`  | `x = x / 2`   |
| `//=`    | Assignment with integer division | `x //= 2` | `x = x // 2`  |
| `%=`     | Assignment with module           | `x %= 2`  | `x = x % 2`   |
| `**=`    | Assignment with exponent         | `x **= 2` | `x = x ** 2`  |

```python
x = 9

x += 3  # x is now 12
x -= 2  # x is now 7
x *= 2  # x is now 18
x /= 3  # x is now 3
```

### 7.3 **Comparison operators**

| Operator | Description              | Example  | Result    |
| -------- | ------------------------ | -------- | --------- |
| ==       | Equality                 | `5 == 5` | `True`    |
| !=       | Inequality               | `5 != 3` | `True`    |
| >        | Greater than             | `5 > 3`  | `True`    |
| <        | Less than                | `3 < 5`  | `True`    |
| >=       | Greater than or equal to | `5 >= 5` | `True`    |
| <=       | Less than or equal to    | `3 <= 5` | `True`    |

```python
a = 10
b = 20

print(a == b)  # False
print(a < b)  # True
print(a > b)  # False
print(a != b)  # True
```

### 7.4 **Logical operators**

|Operator|Description                           |Example         |Result |
|--------|--------------------------------------|----------------|-------|
|`and`   |True if both conditions are true      |`True and False`|`False`|
|`or`    |True if at least one condition is true|`True or False` |`True` |
|`not`   |Inverts the logical value             |`not True`      |`False`|

```python
a = 5
b = 10
c = 15

print(a < b and b < c)  # True
print(a > b or b < c)   # True
print(not (a == b))     # True
```

### 7.5 **Identity operators**

|Operator|Description                         |Example     |Result |
|--------|------------------------------------|------------|-------|
|`is`    |True if both are the same object    |`a is b`    |`False`|
|`is not`|True if both are not the same object|`a is not b`|`True` |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False, Although they have the same content, they are different objects
print(a is c)  # True, a and c point to the same object
```

### 7.6 **Membership operators**

|Operator|Description                             |Example            |Result|
|--------|----------------------------------------|-------------------|------|
|`in`    |True if the value is in the sequence    |`"a" in "hola"`    |`True`|
|`not in`|True if the value is not in the sequence|`"z" not in "hola"`|`True`|

```python
my_list = [1, 2, 3, 4]

print(3 in my_list)       # True
print(5 not in my_list)   # True
```

## 8. DATA STRUCTURES

### 8.1 Strings ""
```python
# Strings ""
# The Strings are a type of data structures
text1 = 'Hello'
text2 = "World"

multiple_text = '''
This is a text
that spans
several lines.
'''

other_multiple_text = """
This is another example
of text written
on multiple lines.
"""

# --------------------
# Output sequences in Strings
# \n: nueva línea
# \t: tabulación (8 espacios)
# \\: barra invertida
# \': comilla simple (')
# \": comilla doble (")

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# Output >
I hope every one is enjoying the Python Challenge.
Are you ?
Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"


# --------------------
# Functions in string
text = "heLLo World"
print(text.upper())  # Output > "HELLO WORLD"
print(text.lower())  # Output > "hello world"
print(text.capitalize()) # Output > "Hello world"

print(text.count('o')) # Output > 2
print(text.count('ld')) # Output > 1

print(text.replace("World", "Python"))  # Output > "heLLo Python"
print(text.find("World"))  # Output > 6

print(text.startswith("heLLo"))  # Output > True
print(text.endswith("World"))   # Output > True

print(len(text))  # Output > 11
print(type(text))  # Output > <class 'str'>

print("r" in text) # Output > True


# -------------------- 
# character access and Slicing
print(text[0])  # Output > "h"
print(text[-1])  # Output > "d" (Negative index, count from the end)

# Slicing from index initial(included) to final(not included)
print(text[2:8])  # Output > "LLo Wo"
print(text[0:8:2])  # Output > "hLoW"
print(text[::-1])  # Output > "dlroW oLLeh"

text_strip = "  Hello World  "
print(text.strip())  # Output > "Hello World"


# --------------------
# operations with strings
greeting = "Hello" + " " + "World"
print(greeting)  # Output > "Hello World"

repeat = "Hello" * 3
print(repeat)  # Output > "HelloHelloHello"


# --------------------
# f-strings (formateo de strings)
# Define the number of decimals
pi = 3.141592653589793
print(f"The value of Pi is approximately {pi:.2f}") # Output > "The value of Pi is approximately 3.14"

name = "Ana"
print(f"|{name:<10}|")  # Left Alignment,       # Output > "|Ana       |"
print(f"|{name:>10}|")  # Right alignment,      # Output > "|       Ana|"
print(f"|{name:^10}|")  # Centered alignment,   # Output > "|   Ana    |"

number = 42
print(f"{number:05}")  # Output > "00042" (pad with 0 until the number has 5 characters)

percent = 0.75
print(f"Percent: {percent:.2%}")  # Output > "Percent: 75.00%"
```

### 8.2 Lists []
```python
#Listas []
my_list = [1, 2, 3, 4, 2]  # List of integers
my_list_str = ["apple", "banana", "pear"]  # List of strings
my_list_mixed = [1, "Hola", True, 3.14]  # List with elements of differents types
my_empty_list = [] # empty list

# -------------------- 
# access items
print(my_list_str[0])  # Output > "apple"
print(my_list[-1])  # Output > 6 (Negative index, count from the end)

# Slicing from index initial(included) to final(not included)
print(my_list[1:4])  # Output > [2, 3, 4]
print(my_list[0:4:2])  # Output > [1, 3]
print(my_list[::-1])  # Output > [6, 2, 4, 3, 2, 1]

# Modify items
my_list[1] = 99  # Output > [1, 99, 3, 4, 2]

# Add items
my_list_str.append("orange")  # Output > ["apple", "banana", "pear", "orange"]

# Insert items
my_list_str.insert(1, "watermelon")  # Output > ["apple", "watermelon", "banana", "pear", "orange"]

# Remove items
my_list_mixed.remove(3.14)  # Output > [1, "Hola", True]

# Remove items for index
my_list_mixed.pop(2)  # Output > [1, "Hola"]

# Remove all items from a list
my_list_mixed.clear() # Output > []

# --------------------
# Functions in list
print(my_list.sort()) # Output > [1, 2, 3, 4, 99] 
print(my_list.reverse()) # Output > [99, 4, 3, 2, 1] 

print(my_list_str.index("apple")) # Output > 0 
print(my_list_str.count('manzana')) # Output > 1
print(my_list.count(2)) # Output > 2

print(len(my_empty_list))  # Output > 0
print(type(my_empty_list))  # Output > <class 'list'>

print("banana" in my_list_str) # Output > True

# --------------------
# operations with list
combined_lists = my_list + my_list_str
print(combined_lists)  # Output > [1, 99, 3, 4, 2, "apple", "watermelon", "banana", "pear", "orange"]

repeat = my_list * 2
print(repeat)  # Output > [1, 99, 3, 4, 2, 1, 99, 3, 4, 2]
```

### 8.3 Tuples ()
```python
#Tuples ()
my_tuple = (3, 2, 1, 6, 5, 4, 9, 8, 7)
person_tuple = ("John", 30, "Enginner") # name, age, profession
coordinates_tuple = (10, 20, 8) # East, North, Elevation

# -------------------- 
# access items
print(my_tuple[0])  # Output > 1
print(my_tuple[-1])  # Output > 7 (Negative index, count from the end)

# Slicing from index initial(included) to final(not included)
print(my_tuple[1:4])  # Output > (2, 1, 6)
print(my_tuple[0:6:2])  # Output > (3, 1, 5)
print(my_tuple[::-1])  # Output > (7, 8, 9, 4, 5, 6, 1, 2, 3)

# --------------------
# Functions in tuples
print(my_tuple.index(5)) # Output > 4 
print(my_tuple.count(8)) # Output > 1

print(len(my_tuple))  # Output > 9
print(type(my_tuple))  # Output > <class 'tuple'>

print(7 in my_tuple) # Output > True

# --------------------
# Unpacking tuples
num1, num2, num3, num4, num5, num6, num7, num8, num9 = my_tuple
print(num1, num2, num3, num4, num5, num6, num7, num8, num9)
# Output > 3 2 1 6 5 4 9 8 7

num1, num2, num3, *rest = my_tuple
print(num1) # Output > 3
print(num2) # Output > 2
print(num3) # Output > 1
print(rest) # Output > [6, 5, 4, 9, 8, 7]

# --------------------
# Using tuples in dictionaries
dictionary = {(10, 20): "Point A", (30, 40): "Point B"}
print(dictionary[(10, 20)])  # Output > "Point A"

# --------------------
# Using tuples in functions
def coordenadas():
    return (10, 20)

x, y = coordenadas()  # Unpack the returned tuple
print(x, y) # Output > 10 20

'''
Notes:
* Tuples are inmutable data structures, so you cannot add, remove or change data in them

* To apply delete, modify or add functions on tuples, you must first convert it to a list and save it back as a tuple.

* Because tuples are immutable and hashable, they can be used as keys in dictionaries.
'''
```

### 8.4 Sets {}
```python
#Sets {} [()] 
my_first_set = {1, 3, 5, 7, 9, 11, 13}
my_second_set = set([2, 4, 6, 8, 10, 12, 14, 16, 18])
empty_set = set() # empty set

# -------------------- 
# perform mathematical operations
print(my_first_set - my_second_set)# Elements of the first set not including elements of the second set (Difference)
print(my_second_set - setsElio1)# Elements of the second set not including elements of the first set (Difference)
print(my_first_set & my_second_set)# Intersection of the two sets (Intersection)
print(my_first_set | my_second_set)# Union of the two sets (Union)
print(my_first_set ^ my_second_set)# Elements that are not in both sets. (Symetric Difference)

# -------------------- 
# access items
# The only way to access the elements of a set is through a for loop.
my_set = {"apple", "banana", "orange"}
for fruit in mi_set:
    print(fruit)
# Output >  banana
#           apple
#           orange

# Add items
my_first_set.add(15)
print(my_first_set) # Output >  {1, 3, 5, 7, 9, 11, 13, 15}

# Remove items (error!, if not exists)
my_second_set.remove(10) # Output >  {2, 4, 6, 8, 12, 14, 16, 18}

# Remove items (Not error!, if not exists)
my_second_set.discard(20) # Output >  {2, 4, 6, 8, 12, 14, 16, 18}

# Remove all items from a list
my_first_set.clear()
print(my_first_set)  # Output > set()


print(2 in my_second_set)  # Output > True
print(5 in my_second_set)  # Output > False

print(len(my_first_set))# Number of elements in the set
print(type(my_first_set))# Shows the data type

print(5 in my_first_set)# Search for an element in the set

# Frosenset
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)  # Output > frozenset({1, 2, 3, 4})

'''
Notes:
* The Sets are data structures in the mathematical sense.
* They do not respect the established order or duplicate elements.
* A frozenset cannot be modified, making it useful when an immutable set is needed.
'''
```

### 8.5 Dictionaries {key : value}
```python
#Diccionarios {}
my_first_dictionary = {
    "name": "John",
    "age": 30,
    "profession": "Enginner"
}

my_second_dictionary = dict(name="Ana", age=25, profession="Doctor")

# -------------------- 
# access items (error!, if not exists)
print(my_first_dictionary["name"])  # Output > 'John'

# access items (Not error!, if not exists)
print(my_first_dictionary.get("last_name", "Not available"))  # Output > 'Not available'

#Add items
my_second_dictionary["last_name"] = "Solis"
print(my_second_dictionary) # Output > {name="Ana", last_name="Solis", age=25, profession="Doctor"}

#Change items
my_first_dictionary["age"] = 30
print(my_first_dictionary) # Output > {name="John", age=30, profession="Enginner"}

#Remove items
del my_first_dictionary["profession"]
print(my_first_dictionary) # Output > {name="John", age=30}

my_second_dictionary.pop("age")
print(my_second_dictionary) # Output > {name="Ana", last_name="Solis", profession="Doctor"}

# Remove all items from a dicctionary
my_second_dictionary.clear()
print(my_second_dictionary) # Output > {}

#Update dictionary
my_first_dictionary.update(my_second_dictionary) 
print(my_first_dictionary)

# -------------------- 
# Iterate over a dictionary
# Iterate over keys
for key in my_first_dictionary.keys():
    print(key, my_first_dictionary[key])

# Iterate over values
for value in my_first_dictionary.values():
    print(value)

# Iterate over key-value pairs
for key, value in my_first_dictionary.items():
    print(f"{key}: {value}")

# --------------------
# Practical examples
# Structured data storage
person = {
    "name": "Ana",
    "age": 28,
    "profession": "Doctor",
    "hobbies": ["reading", "traveling", "photography"]
}

# Frequency counters
text = "hello hello bye"
counter = {}

for word in texto.split():
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)  # Output >  {'hello': 2, 'bye': 1}

'''
Notes:
* Indictionaries we can acces the elements from the key
* Which identifies them, for example: "name" : "Elio" (key : value)
'''
```
