print("Two numbers, or press 'q' to quit: ")

while True:
    first_num = input("First numbers: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if first_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
