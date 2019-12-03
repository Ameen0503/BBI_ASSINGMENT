def ab():
    # Reading the input
    a=input("enter your string")
    b=a.split(" ")
    a=" ".join(reversed(b))
    a=a.capitalize()
    return a
print(ab())
