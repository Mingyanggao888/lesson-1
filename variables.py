# This is our variables program
# TODO: Finish this program
"""This is our program, it will show our code."""
print("Variables file!")

# Integers numbers -> ints
# int()
integer_number = 12
print("Integer number:", integer_number)

# Floating point numbers -> floats
# float()
floating_point_number = 9.8
print("Float number:", floating_point_number)

# String
# str()
empty_string = ""
text_string = "This is a string variable"
print("String value:", text_string)

# Boolean ( True / False )
# bool()
boolean_example = True
print("Boolean value true:", boolean_example)
print("Boolean value false:", False)

print(20 * "-")

# Operations with variables
new_text = text_string + " " + "Example of string."
print("New string:", new_text)

addition = integer_number + floating_point_number
print("Addition:", addition)
subtraction = integer_number - floating_point_number
rounded_result = round(subtraction, 1)
print("Subtraction:", subtraction)
print("Rounded subtraction:", rounded_result)
multiplication = integer_number * floating_point_number
print("Multiplication:", multiplication)
division_result= integer_number / floating_point_number
print("Division:", division_result)
var_to_power_two = integer_number ** 2
print("Power result:", var_to_power_two)
new_thing = 10 % 4
print("Reminder:", new_thing)
new_thing = 10 % 3
print("Reminder:", new_thing)

print(80 * "-")

one_less_two = 1 < 2
print("1 < 2:", one_less_two)
print("3 < 2:", 3 < 2)
print("3 == 2:", 3 == 2)
print("3 != 2:", 3 != 2)
print("3 <= 2:", 3 <= 2)
print("3 > 2:", 3 > 2)
print("3 >= 2:", 3 >= 2)

print("Text comparison:", "abc" < "abcd")

print(80 * "-")

# and
t_a_f = True and False
print("True and False", t_a_f )

# or
t_o_f = True or False
print("True or False", t_o_f)

print(80 * "-")

special_value = None
print("None value:", special_value)
print("None as bool:", bool(special_value))

print(80 * "-")

print("bool of -1:", bool(-1))
print("bool of 0:", bool(0))
print("bool of 123:", bool(123))
print("bool of 12.1:", bool(12.1))
print("bool of -0.00001:", bool(-0.00001))
print("bool of -0.0:", bool(-0.0))


