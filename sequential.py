


#selection statements
#simple if statements
n = 10
if n % 2 == 0:
    print (n)


# elif
l = 10
u = 12
x = 17
if l > u:
    if l > x:
        print("l value is big")
    else:
        print("x value is big")
elif u > x:
    print("u value is big")


#if-elif-else statements
v = 15
k = 12
if v == k:
    print("both are ewual")
elif v > k:
    print("v is greater than k")
else:
    print("v is smaller than k")
    #v is greater


#lists
empty_list = []
print(array := [1,2,3,4,5,6,7])
print(array[3])
array.append(10)
print(array)
#deleting a list


#tuples
my_tuple = (2,5, 4)
print(my_tuple)
print(my_tuple[0])
#cant be updated but can be used to form other tuples
print(my_2_tuple := (5,6,7))

