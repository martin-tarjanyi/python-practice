import requests

a = "hello"
print(f'type: {type(a)} value: {a}')  # string interpolation, before string there is a f

a = 5  # dynamic typing
print(f'type: {type(a)} value: {a}')

integerDivision = 17 / 3  # integer division
print(f'Simple division result: {integerDivision}')

flooredIntegerDivision = 17 // 3  # integer division, like Java by default
print(f'Floored integer division result: {flooredIntegerDivision}')


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return int(fahrenheit)  # convert to int


# int has to be converted to str explicitly to be able to concatenate
celsius = str(celsius_to_fahrenheit(25))
print("25 celsius to fahrenheit: " + celsius)

# named parameters
print("25 celsius to fahrenheit: " + str(celsius_to_fahrenheit(celsius=25)))

if celsius != 77:
    print("String and int can be compared but never equal.")

if celsius == "77" and not False:
    print("Expect to print this.")
elif celsius == "77":
    print("Should not print this.")
else:
    print("Should not print this.")

if True:
    pass  # does nothing

list = ["1", "2", "3", "4"]

for item in list:
    print(f'list item: {item}')

try:
    5 / 0
except:  # catch clause
    print("Some error happend.")

# while True:
#     userInput = input("Write something.\n")
#     print(f"User has written: {userInput}")
#     if userInput == "done":
#         break

result = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")

content = result.json()

print(content)

list_of_lists = [[1, 2], [3, 4, 5], [6, 7, 8]]
flatten = [item for sublist in list_of_lists if len(sublist) > 2 for item in sublist]
print(flatten)
