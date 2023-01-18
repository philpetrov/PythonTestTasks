# Task 1. Create a function that takes a dictionary of objects like
#{ "name": "John", "notes": [3, 5, 4] } and returns
#a dictionary of objects like { "name": "John", "top_note": 5 }.

def topNote (nameOfYourArray, yourArray):
    # 0 step - is to put values into dictionary a and print it
    a = {"name": nameOfYourArray, "notes": yourArray}
    print(a)
    # 1 step - is to change create key variable "top_note"
    keyArray = "top_note"
    # 2 step - is to find top number of yourArray and redefine yourArray (keep only max number)
    largest_number = yourArray[0] #first elem array_1, after cycle we'll found largest
    for number in yourArray:
        if number > largest_number:
            largest_number = number
    # 3 step - is to redefine and print result
    a = {"name": nameOfYourArray, keyArray: [largest_number]}
    print(a)
    return
# check the result of 1 task
topNote ("John", [3,1000,3])

# Task 2.Create a function that takes a number num and returns its length
#/ The use of the len() function is prohibited.
# number_length(5000) ➞ 4

def lengthNum():
    print('Enter number or text:')
    inputValue = input() #for input number by User
    counter = 0 #at the start counter = 0
    for _ in inputValue:
        counter += 1  # increment the counter
    print(counter)  # outputs the length (9) of the string “educative”
    return
lengthNum()

# Task 3 - print a message once the condition is false
# i = 1
# while i < 6:
def falseCond():
    i=1
    while i < 6:
        i = i + 1
        if i == 6:
            print("ошибка")
falseCond()

# 4. Multiply argument a with argument b and return
#the result / using lambda
#*
multLamda = lambda a, b: a * b;
print (multLamda(3, 5))

# 5. Create a class named Person, use the __init__() 
#function to assign values for name and age:
def __init__(person : name, person : age) 
