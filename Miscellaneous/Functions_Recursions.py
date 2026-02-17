# #function
# def sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# sum(1,2)
# sum(4,5)

#or
# def sum(a,b):
#     sum = a+b
#     return sum
# print(sum(3,4))


# def display():
#     str1 = input("Enter the string: ")
#     print(str1)
#     return str1
# display()

# def print_hello():
#     print("Hello World")
# print_hello()

#creating a function that calculates average of 3 numbers
# def calc_avg(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg
# calc_avg(1,2,3)

# def cal_prod(b,a=5): #default
#     print(a*b)
#     return a*b
# cal_prod(3,3)


# #WAF to print length of a list where list is the paramater
# def length():
#     lst = []
#     print("Enter numbers one by one: ")
#     print("Enter done to stop")
#     while True:
#         user_input = input("Enter the number: ")
#         if user_input.lower() == "done":
#             break
#         lst.append(float(user_input))
#     count = 0
#     for i in lst:
#             count+=1
#     if count==0:
#         print('No numbers entered')
#     else:
#         print(lst,count)
# length()

# def length():
#     lst = []
#     print("Enter numbers one by one: ")
#     print("Enter done to stop")
#     while True:
#         user_input = input("Enter the number: ")
#         if user_input.lower() == "done":
#             break
#         lst.append(float(user_input))
    
#     if len(lst)==0:
#         print('No numbers entered')
#     else:
#         print(len(lst))
# length()

# #waf to print the elemets of a list in a single line(list is the parameter)
# def display():
#     lst = []
#     print("Enter numbers one by one: ")
#     print("Enter done to stop")
#     while True:
#         user_input = input("Enter the number: ")
#         if user_input.lower() == "done":
#             break
#         lst.append(float(user_input))
#     for i in lst:
#         print(i, end = ' ')

# display()

# def view(lst):
#     for i in lst:
#         #return i
#         yield i
# result = view([1,2,3])
# print(next(result))
# print(next(result))
# print(next(result))


# def sumation(*args):
#         total = sum(args)
#         return total
# print(sumation(1,2,3,4))



#waf to find the factorial of a number (n is the parameter)

# def fact(n):
#     facti = 1
#     for i in range(1, n+1):
#         facti*=i
#     print(facti)
#     return facti
# n = int(input("Enter the number to calculate factorial: "))
# fact(n)


#waf to convert USD to INR
# rate = 90.56
# def currency(USD):
#     INR = USD * rate
#     print(USD, "Usd_Value is" ,INR,  "Inr_value")
#     return INR
# USD = float(input("Enter how many USD: "))
# currency(USD)



# def calculate_average():
#     numbers = []

#     print("Enter numbers one by one.")
#     print("Type 'done' to stop.")

#     while True:
#         user_input = input("Enter number: ")

#         if user_input.lower() == "done":
#             break

#         numbers.append(float(user_input))

#     total = 0
#     count = 0

#     for num in numbers:
#         total += num
#         count += 1

#     if count == 0:
#         print("No numbers entered.")
#     else:
#         print("Average =", total / count)


# calculate_average()

# # waf for odd and even
# def even_odd(n):
#     return "Even" if n%2==0 else "Odd"
# n = int(input("enter a number: "))
# print(even_odd(n))

#Recursion
# def show(n):
#     return n
# print(show(4)) #4,3,2,1

# import sys
# print(sys.getrecursionlimit())
# def show(n):
#     if(n == 0):
#         return 
#     print(n)
#     show(n-1)
#     print("end")
# print(show(2))

#factorial
# def facti(n):
#     if(n==1 or n==0): #base case
#         return 1
#     r= facti(n-1)*n
#     return r
# print(facti(5))
#Understand how it works.


#write a function to calculate sum of first n natural numbers
# def cal_sum(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     return total
# print(cal_sum(4))

#Now using recursion
# def rec_sum(n):
#     if(n==0):
#         return 0
#     return rec_sum(n-1) + n
# print(rec_sum(5))


#recursive function to print all elements of the list
# def ilist(list, idx=0):
#     if (idx == len(list)):
#         return 
#     print(list[idx], end=' ')
#     ilist(list,idx+1)

# fruits = ["Apple", "Mango","Litchi"]

# ilist(fruits)
