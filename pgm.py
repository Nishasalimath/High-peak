f = open("input.txt", "r")
#print(f)
lst=[]
new_lst=[]
for x in f:
    new_lst.append(x)
    pu=x.split()
    lst.append(pu)
lst1=[]
for i in range(1,len(lst)):
    lst1.append(int(lst[i][-1]))
#lst1.sort()
arr=sorted(lst1)
employee_list=[4,6,2]
f2 = open("sample_output.txt","w")
for i in employee_list:
    f2.write("Number of employees: ")
    f2.write(str(i))
    f2.write("\n\n")
    f2.write("Here the goodies that are selected for distribution are:\n")
    diff=10**20
    for k in range(len(lst1)-i-1):
        var1=k+i-1
        if arr[var1]-arr[k] < diff:
             
            diff = arr[var1]-arr[k]
            m=k
            res_lst=[]
            while(m<k+i):
                res_lst.append(arr[m])
                m+=1
    for x in res_lst:
        for y in new_lst:
            if str(x) in y:
                f2.write(y)
    f2.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is :")
    f2.write(str(diff))
    f2.write("\n\n")
 
f.close()
f2.close()