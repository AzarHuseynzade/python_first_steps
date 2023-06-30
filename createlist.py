n=int(input("Enter length: "))

user_list=[]

i=0

while i < n:
    variables="Enter element #" + str(i+1) + ": "
    user_list.append(input(variables))
    i+=1

print(user_list)
