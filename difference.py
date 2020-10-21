

print("Give me two numbers to compare:")
number_one = float(input("First number > "))
number_two = float(input("Second number > "))


def difference(number_two, number_one):
    diff = number_two - number_one + 1
    return diff

if number_one > number_two:
    print(f" {number_one} is greater than {number_two}")
elif number_one == number_two:
    print(f" {number_one} is equal to {number_two}")
else:
    diff = difference(number_two, number_one)
    print(f" {number_one} is less than {number_two}. You must add {diff} for it to be greater.")
