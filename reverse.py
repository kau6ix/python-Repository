new=input("Please enter your string : ").strip().lower()
n=new[::-1]
print(n)
l=new.split()
print(l)
l1=[]
s=""
for i in l:
    s=s+" "+i[::-1]
    #l1.append(list(i[::-1]))
    #s=" ".join(l1)
    print(s)
print(s)
print(s[::-1])
