# Pattern 11
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# Pattern 12
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+i),end="")
#     print()

# Pattern 13
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end="")
#     print()

# Pattern 14
# n=int(input("Enter the number"))

# for i in range(n,0,-1):
#         print("*"*i)
#  OR

# for i in range(n,0,-1):
#     for i in range(0,i):
#         print("*",end="")
#     print()

# Pattern 15
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(n+1-i,0,-1):
#         print(i,end="")
#     print()

# Pattern 16
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(1,n+1-(i-1)):    #n+2-i
#         print(j,end="")
#     print()

#Pattern 17
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+i),end="")
#     print()

#Pattern 18
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end="")
#     print()

# Pattern 19
# n=int(input("Enter the number"))
# for i in range(n,0,-1):
#     for j in range(n,n-i,-1):
#         print(i,end=" ")
#     print()

# Pattern 20
# n=int(input("Enter The Number"))
# for i in range (n,0,-1):
#     for j in range(n,n-i,-1):
#         print(j,end=" ")
#     print()