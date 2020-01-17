#exercise 3-5

guests = ['kathy bates', 'lucy lawless', 'angela bassett']
message = " you are invited to dinner"
print("Hello, " + guests[0].title() + message)
print("Hello, " + guests[1].title() + message)
print("Hello, " + guests[2].title() + message)

del guests[0]
guests.append('viola davis')
print("Hello, " + guests[0].title() + message)
print("Hello, " + guests[1].title() + message)
print("Hello, " + guests[2].title() + message)
