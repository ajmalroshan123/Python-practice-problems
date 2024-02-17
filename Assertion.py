# Assertion 
"""
The assert key is used when debugging the code.
The assert key lets you test if a condition in your code return True, if not, the program will raise an        
Assertion error
You can write a message to be written if the code returns False, check the example below
"""
x = "hello"

# if condition returns True, then nothing happens:
assert x == "hello"
print("Passing the Hello")

# if the condition returns false, Assertion is raised:
assert x == "goodbye"

y = 'Hello'
# Write a message if the condition is False
assert y == "good","x should be 'Hello'"