# this function greets people by their name
def greet(name):
    print("Hello, " + name)
    if(name == "lionel"):
        print("is it me you're looking for?")
    print("How is it going?")
    the_answer = raw_input("> ")
    if(the_answer == "fantastic"):
        print("cool")
    print("Ok")
    print("goodbye")

# this line below actually calls the function
# greet("lionel")

# FOR LOOPS

for index in range(0, 500000):
    greet("lionel")








    
