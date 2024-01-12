v=0
c=0
for letter in "HelloWorld":
    if letter.lower() in "aeiou":
        v=v+1
    
    else:
        c=c+1
print(v,c)

students={
    "male":["Tom", "Raaghab","Kaushik"],
    "female":["Priya","Teju", "Preeti"]
    }

for key in students.keys():
    for name in students[key]:
        if "a"*2 in name:
            print(name)
