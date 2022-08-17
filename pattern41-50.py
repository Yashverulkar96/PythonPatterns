# Pattern 41
# n=int(input("Enter The Number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(2*i-1,0,-1):
#         print(chr(64+j),end="")
#     print()

# Pattern 42
# n=int(input("Enter The Rows"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i):
#         print((i-j),end="")
#     for k in range(0,i):
#         print(k,end="")
#     print()

# Pattern 43
# n=int(input("Enter The rows"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i):
#         print(chr(64+1+(i-j)),end="")
#     for k in range(0,i):
#         print(chr(64+1+k),end="")
#     print()

# Pattern 44
# n=int(input("Enter The Rows"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(i-1,0,-1):
#         print(k,end="")
#     print()

# Pattern 45
# n=int(input("Enter The Rows"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(chr(64+j),end="")
#     for k in range(1,i):
#         print(chr(64+k),end="")
#     print()


# Pattern 46
# n=int(input("Enter The Rows"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(n,(n-i),-1):
#         print(j,end="")
#     print()

# Pattern 47
# n=int(input("Enter The Rows"))
# for i in range(1,n+1):
#     print(" "*(i),end="")
#     for j in range(1,n+2-i):
#         print("*",end="")
#     for k in range(1,n+1-i):
#         print("*",end="")
#     print()

# Pattern 48
# n=int(input("Enter The rows"))
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(1,n+2-i):
#         print((n+1-i),end="")
#     for k in range(1,n+1-i):
#         print((n+1-i),end="")
#     print()

# Pattern 49
# n=int(input("Enter The Rows"))
# for i in range(1,n+1):
#     print(" "*i,end="")
#     for j in range(1,n+2-i):
#         print(2*n+1-2*i,end="")
#     for k in range(1,n+1-i):
#         print(2*n+1-2*i,end="")
#     print()

# Pattern 50
# n=int(input("Enter the row"))
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(1,n+2-i):
#         print(j,end="")
#     for k in range(2,n+2-i):
#         print(n+k-i,end="")
#     print()
