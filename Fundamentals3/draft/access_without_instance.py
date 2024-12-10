class MyClass:
    @staticmethod
    def some_function():
        return "Static Dynamic Value"

    @property
    def result(cls):  # Using classmethod for dynamic return
        return cls.some_function()

# Example Usage
print(MyClass.result)  # Call the function directly
