legal_age = 21

print("-- Welcome to the Hacktoberfest bar --")

# age = int(input("How old are you? "))

def bar(age):

    if age >= legal_age:
        return "Have a beer!"
    elif age == 20:
        return "So close..one more year kid."
    else:
        return f"Sorry, {age} is too young for a beer, how about a soda?"
