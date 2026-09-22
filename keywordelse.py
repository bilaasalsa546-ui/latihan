str_input = input('Enter your grade: ')
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 65:
    print("awesome")
else:
    print("below the passing grade")