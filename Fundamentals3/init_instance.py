class AutoCallable:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        # Automatically run the function when accessed
        return self.func()

# Define the lambda function
custombeh = lambda: print("test")

# Assign it to an instance of AutoCallable
custombeh = AutoCallable(custombeh)

# Access the variable, and it will run automatically
custombeh  # This will print "test"