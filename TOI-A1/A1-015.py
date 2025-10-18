name = input()
lname = input()
age = input()

if len(name) > 5 and len(lname) > 5:
    pwd = name[:2] + lname[len(lname)-1] + age[len(age)-1]
else:
    pwd = name[:1] + age + lname[len(lname)-1]

print(pwd)