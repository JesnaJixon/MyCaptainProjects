list1 =[]
number =int(input("Please enter the number of numerical elements in the list :  "))
for i in range (1, number+1):
    value= int (input("Please enter the values of %d Element : "%i))
    list1.append(value)
print("The positive numbers in the list are : ")
for j in range (number):
    if(list1[j]>=0):
        print(list1[j], end=' ')