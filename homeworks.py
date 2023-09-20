#Problem 1:
# a = int(input("Enter a number "))
# # if a % 2 == 0:
# #   print("even number")
# # elif a % 2 != 0:
# #   print("odd number")
# # if a % 3 == 0:
# #   print("Bez ostatka")
# # elif a % 3 != 0:
# #     print("S ostatkom")
# b = 2
# total = a ** b
# if total >= 1000:
#   print(" a > 1000")
# else:
#   print("Ne bolshe")

#Problem 4
#if True:
#   print(1)

# #Problem 5
# a = 10 // 5
# b = 10 / 5
# if a == b:
#     print(a + b)

# #Problem 6
# number = int(input("Enter a number: "))
# if number < 0:
#     print(number)
# else:
#     print("This is a positive number")

# #Problem 7 and 8
# a = 10
# b = 5
# if a > 0 and b > 0:
#     print("Positive")
# if a > b:
#     print (a + 2)
# else:
#     print(b + 2)

# # Problem 9
# any_number = int(input("Enter a number: "))
# if any_number > 0:
#     print("Positive number")
# elif any_number == 0:
#     print ("Zero")
# else:
#     print("Negative number")

# #Problem 10
# age = int(input("Enter your age: "))
# if age > 18:
#     print("Access approved")
# elif age <= 4:
#     print("Not for kids, access restricted")
# else:
#     print("Underage")

# #Problem 11
# var1 = 45
# var2 = 6
# if var1 % var2 == 0:
#     print("It can be divided")
# else:
#     print("It cannot be divided")

# #Problem 12
# year = int(input("Enter the year:"))
# current_year = 2023
# if year < current_year:
#     print("PAST YEAR - ", year)
# elif year == current_year:
#     print("Current Year - ", year)
# else:
#   print("Future year - ", year)

# #Problem 13
# year = int(input("Enter your year of birthday: "))
# current_year = 2023
# age = current_year - year
# if age >= 18:
#     print("Access approved")
# elif age <= 4:
#     print("Not for kids, access restricted")
# else:
#     print("Underage")

# #Problem 14
# num = 478
# num2 = 575
# num3 = 222
# if num > num2 and num > num3:
#     print("num is the maximum")
# elif num < num2 and num < num3:
#     print("num is the minimum")
# elif num2 > num and num2 > num3:
#     print("num2 is the maximum")
# elif num2 < num3 and num2 < num:
#     print("num2 is the minimum")  
# elif num3 > num2 and num3 > num:
#     print("num3 is the maximum")
# elif num3 < num2 and num3< num:
#     print("num3 is the minimum")

# x = 13 ** 2
# print(x)
# # if x < 172:
# #   print(x ** 2)
# a = input("Enter a word")
# print(a * 2)

    # Class 3 - strings
#Task 0
# sen = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
# print(sen[0:len(sen)//2].upper())
# print(sen[len(sen)//2:].lower())
# # option 2
# print("{}{}".format(sen[0:len(sen)//2].upper(),  sen[len(sen)//2:].lower()))
# #option 3
# print(f"{sen[0:len(sen)//2].upper()}{sen[len(sen)//2:].lower()}")

# #Task 1 
# first_boolean = "True"
# second_boolean = str(True)
# print(first_boolean)
# print(second_boolean)

# #Task 2
# symbol = input("enter a symbol: ")
# string = 'GitHub'
# print(symbol.join(string))

#Task 3
# str5 = "Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 
зараженных систем"
# print(str5.replace("е", "3"))

# #Task 4
# username = input("Enter your name: ")
# movie = input("Enter your favorite movie: ")
# # print("Hello " + username)
# # print(movie + " ,  is a dope movie")

# # second option:
# print("hello {}, the best movie {}".format(username, movie))

#Task 5
# string = "Google создаст специальную команду для поиска багов в особо важных приложениях."
# word_count = len(string.split())
# print(word_count)

#Task 6
# str6 = "Самые важные собЫтия в миРе инфосека за сентябрь"
# print("|".join(str6))

#Task 7
# str3 = "хакеры слили в сеть данные пакистанской энергетической компании k-Electric"
# print(str3.title())

# Class 5 Tuples and Lists

# cutting:
# name = "Bootcamp"
# print(name[start: stop: step]) - [::] - to read from right to left

# name = "Loki"
# print("your name: %s " %name) - !old way to print s - string n - number

# names = ["Allan", "BOB", "James"]
# for i in names:
#   print(i.lower())

# #Task 0
# lists = ["Tobby", "Maccor", 56, 54.5, "Banzai"]
# print(lists)

#Task 1
# tuple = ("Name", "age", "address")
# print(tuple[0])
# print(tuple[1])
# print(tuple[2])

# option 2
# for in in range(len(tuples)):
#   print(i)


#Task 3
# names = ["Bob", "Tom", "Bill", "Kate", "Jack"]
# space = " "
# print(space.join(names))

# #Task 4
# list_1 = ["apple", "orange", "melon", "pineapple", "kiwi"]
# list_2 = ["strawberry", "blueberry", "cherry", "raspberry"]
# list_1.extend(list_2)
# print(list_1)

#Task 5
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 
'Jhon','Jack', 'Jimmy', 'Jack','Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 
'Jackson', 'Jhon',]
# print(names.count('Jack'))

# # #Task 6
# # if "Oskar" in names:
#   print(names.remove("Oskar")


#Task 7
# list = []
# list.append("Talant")
# list.append("1992")
# list.append("Python")
# print(list)

#Option 2
# list = []
# for i in range(3)
#   variable = input("Q: ")
#   list.append(variable)

# print(list)

#Task 9
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# result = 1
# for i in range(len(a)):
#   result *= a[i]
# print(result)

# #Task 10
# text = "Google создаст специальную 36 команду для поиска 24 багов в особо важных 17 
приложениях."
# list = text.split()
# numbers = []
# letters = []
# for i in list:
#   if i.isdigit():
#     numbers.append(i)
#   else:
#     letters.append(i)
# print(numbers)
# print(letters)

# #Task 11
# str = ["Integers", "Floats", "Strings", "Lists", "Tuples"]
# print(str[1:4])
