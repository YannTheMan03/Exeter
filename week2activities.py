

def num1():
    name = 'Yann Bolton'
    age = 18
    birth_year = 2026 - age
    print(f'{name} is {age} years old, and was born in {birth_year}')

def num2():
    count = 0
    for i in range(1,11):
        print(i)
        print(i**2)
        count += i
    print(count)

def num3():
    x = int(input("Enter a starting number: "))
    while x != 0:
        print(x)
        x-=1
    print("Blast off!")

def num4():
    marks = [65,72,81,58,77]
    x = 0
    for count in marks:
        print(count)
        x += count
    print(x)
    print(x/len(marks))
    print(min(marks))
    print(max(marks))

def num5():
    fav_foods = ['Pizza', 'Carbonara','Burrito','Taco','Croissant']
    for x in fav_foods:
        print(x)
    x = " "
    while x != 'quit':

        x = input('Enter a food: ')
        fav_foods.append(x)
    print(fav_foods)


num1()
num2()
num3()
num4()
num5()