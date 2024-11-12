from prettytable import PrettyTable

table = PrettyTable()

aa=int(input("Enter Total No. of Leaves: "))

l=int(input("Enter Total No. of Leaves that can be taken in per month: "))


n=int(input("Enter No. of Months: "))

a=[[0 for _ in range(5)] for _ in range(n)]

b=5

for i in range(n):
    a[i][1]=int(input(f"Enter No. of Leaves in Month {i+1}: "))
    a[i][0]=i+1


for i in range(n):
    a[i][4]=aa
    
    if a[i][1]>=l:
   
        if a[i][4]<=(l-1):
            a[i][2]=a[i][4]
            a[i][3]=a[i][1]-a[i][2]
            a[i][4]=aa-a[i][2]
            aa=a[i][4]

        else:
            a[i][2]=l
            a[i][3]=a[i][1]-a[i][2]
            a[i][4]=aa-a[i][2]
            aa=a[i][4]

    else:

        if a[i][4]<(l-1):
            a[i][2]=a[i][4]
            a[i][3]=a[i][1]-a[i][2]
            a[i][4]=aa-a[i][2]
            aa=a[i][4]

        else:
            a[i][2]=a[i][1]
            a[i][3]=a[i][1]-a[i][2]
            a[i][4]=aa-a[i][2]
            aa=a[i][4]

table.field_names = ["Mon", "Lev", "Pai", "Unp", "Rem"]  

for i in range(n):
    table.add_row([i+1, a[i][1], a[i][2], a[i][3], a[i][4]])

print(table)
