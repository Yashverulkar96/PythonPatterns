# Pattern 21
# n=int(input("Enter The Number"))
# for i in range(n,0,-1):
#     for j in range(n,n-i,-1):
#         print(chr(64+i),end=" ")
#     print()

#OR
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(65+n-i),end=" ")
#     print()



# Pattern 22
#n=int(input("Enter The Number"))
# for i in range(n,0,-1):
#     for j in range(n,n-i,-1):
#         print(chr(64+j),end=" ")
#     print()

#OR
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(65+n-j),end=" ")
#     print()

# Pattern 23
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i,end=" ") #or end="\n"
#     print()

# Pattern 24
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
#OR
# for i in range(1,n+1):
#     print(" "*(n-i),(str("*")*i))

# Pattern 25
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
#OR
# for i in range(1,n+1):
#     print(" "*(n-i),(str(i)*i))

# Pattern 26
# n= int(input("Enter the number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# Pattern 27
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     print(" "*(n-i),(chr(64+i)*i))


# Pattern 28
# n=int(input("Enter The Number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(64+j),end="")
#     print()

# Pattern 29
# n=int(input("Enter The Number"))
# for i in range(1,n+1):
#     print(" "*(i-1),"*"*(n-i))

# Pattern 30
# n=int(input("Enter the Number"))
# for i in range(1,n+1):
#     print(" "*(i-1),str(n+1-i)*(n+1-i))
