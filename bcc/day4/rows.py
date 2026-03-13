# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(n+1-i),end=" ")
#     print()

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(i,end=" ")
    print()