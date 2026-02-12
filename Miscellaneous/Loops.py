#loops - To repeat instructions
#while
# count = 1
# while count<=5:
#     print("hello" , count)
#     count+=1
# print(count)

# print numbers from 1 to 100

# i = 1
# while i<=100:
#     print(i)
#     i+=1
# print(i)


# print numbers from 100 to 1

# i = 100
# while i >=1:
#     print(i)
#     i-=1
# print(i)


#print multiplication table of a number n

# n = int(input("Enter a number:"))
# i = 1
# while i<=10:
#     print(i * n)
#     i+=1
# print("Table of number", n)


#print elements of following list using a loop

# list1 = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<len(list1):
#     print(list1[i])
#     i+=1


# search for a number x in the tuple using loop
# tupe1 = (1,4,9,16,25,36,49,64,81,100,36)
# print(tupe1)
# n = int(input("enter the number to search from above given tuple: "))
# i = 0
# while i<len(tupe1):
#     if tupe1[i] == n:
#         print("Element", n, "is found in", i ,"position of the tuple")
#         break
#     i+=1
  
# else:
#     print("element is not found ")

#to print odd numbers
# i = 1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue #skip
#     print(i)
#     i+=1


# for loop
# str ='abhishek'
# for ele in str:
#     if ele == 'i':
#         print(ele, 'found' , end = ',')
#         continue
#     print(ele)
# else:
#     print('Done')

# tup1 = (1,4,9,16,25,36,49,64,81,100,16)
# idx = 0
# x = int(input("Enter the number: "))
# for y in tup1:
#     if y == x:
#         print("Element",x ,"is found in", idx, "position")
#         break
#     idx+=1

# #print 100 to 1
# for ele in range(100,0,-1):
#     print(ele)

# Multiplication of numbers using while and for
# n = int(input("Enter the number: "))
# i = 1
# while i<11:
#     print(i*n)
#     i+=1
# for mul in range(1,11):
#     print(n*mul)

# for ele in range(5):
#     pass #place holder for future code
# print("some")


# sum of first n number using while
# n = int(input())
# i = 1
# sum = 0
# while i<=n:
#     sum +=i
#     i+=1
# print("total sum is",sum)
  

# n= 5
# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print("total sum is",sum)

#factorial of numbers
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print("factorial of 5 is", fact)