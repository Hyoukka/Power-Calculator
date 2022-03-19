number_powered = int(input("Type a number you want to power: "))
power = int(input("Type a exponent: "))


def power_function():
    return number_powered ** power


number_power = power_function()
print(str(number_powered) + "^" + str(power) + " is " + str(number_power))
