# fruits = ["mango","apple","avocado","strawberry"]

# for fruit in fruits:
#     print(fruit)


# insert data into the list

# my_list=[]
# n=int(input("enter the number of data you want to insert: "))

# for i in range(n):
#     element=int(input(f"number{i+1}:"))
#     my_list.append(element)
# add=sum(my_list)
# av=add/n
# print(av)
# print(my_list)


# student_heights = ["20","10","10"]
# for i in range(0, len(student_heights)):
#     student_heights[i] = int(student_heights[i])
# total_number=0
# numberofstudent=0 
 
# for height in student_heights:
#     total_number=+height
#     numberofstudent +=1
# print(total_number)
# print(numberofstudent)
    

# student_scores= ["78","65","89","55","91","64","89"]

# for i in range(0, len(student_scores)):
#     student_scores[i] = int(student_scores[i]) 
# highest=0
# for number in student_scores:
#     if number > highest:
#         highest= number
# print(highest)  

n=int(input("enter number in range of 0 and 1000: "))

sum=0
for i in range(1,n+1):
   if i % 2 == 0:
      sum=sum+i
print(f"the sum of even number: {sum}")
