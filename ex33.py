def while_func(how_many_times, increment = 1):
    i = 0
    numbers = []

    while i < how_many_times:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    return numbers

numbers = []
how_many_times = int(input("How many numbers?\n> "))
increment = int(input("The size of jumps?\n> "))

numbers = while_func(how_many_times, increment)

print("The numbers: ")

for num in numbers:
    print(num)