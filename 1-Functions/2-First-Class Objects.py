def hi():  # Header
    """
    An example of a function that does not require any input parameters.
    """
    print("Hello my friend")  # Statement


def hello(name):  # Header
    print(f"Hello dear {name}")  # Statement


hi()  # Function Call
hello("jimmy")  # Function Call

print(
    hi
)  # Print Function Object (for my system address in memory is <function hi at 0x0000017DD9AA2C00>)
print(
    hello
)  # Print Function Object (for my system address in memory is <function hello at 0x0000017DD9AA2660>)

Hi = hi  # Assign Function to Variable
print(Hi())  # Function Call via New Variable

my_list = [hi, hello]  # First-Class Objects

print(my_list)  # Print List of Function Objects
print(my_list[0]()) # Call First Function Object in List returns None because hi() does not return anything
my_list[0]()

print(my_list[1]("John"))
my_list[1]("Steve")

for func in my_list:  # Iterate over Function Objects
    if func == hello:  # Condition
        func("Sarah")  # Function Call with Argument
    else:
        func()  # Function Call without Argument
