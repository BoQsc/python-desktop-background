class MyClass:
    @classmethod
    def initialize_attribute(cls):
        if not hasattr(cls, '_new_attribute'):
            cls._new_attribute = "Initialized Value"
            print("Class attribute '_new_attribute' added and initialized.")
        else:
            print("Class attribute '_new_attribute' already exists.")
    
    # Ensure `initialize_attribute()` is called when the class is defined
    def __new__(cls, *args, **kwargs):
        cls.initialize_attribute()
        return super().__new__(cls, *args, **kwargs)

# Usage
print(MyClass()._new_attribute)  # Access the class attribute after initialization
