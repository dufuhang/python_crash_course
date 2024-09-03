from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()
# lines is a list[]
lines = contents.splitlines()
print(lines)

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("your birthday, in the from mmddyy: ")
if birthday in pi_string:
    print("Yes!")
else:
    print("No!")
