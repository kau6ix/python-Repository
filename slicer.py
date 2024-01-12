# get user email

email=input("Please enter your email address : ")

# Slice out user name

user=email[:email.index("@")]

#slice domain name

domain=email[email.index("@")+1:]
print(domain)

#format message

output="Your username is : {} and your domain is : {}".format(user,domain)

#display output
print(output)
