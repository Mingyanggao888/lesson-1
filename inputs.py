# Inputs

input_value = input("What's your name? ")
input_number = input("Which lesson is it? ")
input_number = int(input_number)
# input_number = float(input_number)

print(
    "Hello {}! This is your {} lesson".format(input_value, input_number)
)

print(
    f"Hello {input_value}! This is your {input_number} lesson"
)

template = "Hello {}! This is your {} lesson."
print(template.format(input_value, input_number))


