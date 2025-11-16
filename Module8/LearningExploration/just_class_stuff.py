class TestClass:
    is_this_static = "Static Check" # not actually static

    def __init__(self, name, instance_message):
        self.__name = name
        self.instance_message = instance_message
    
    def get_name(self):
        return self.__name

def main():
    test1 = TestClass("Hitest1", "This is test class 1")
    print(test1.get_name())
    print(test1.is_this_static)
    print(test1.instance_message)

    test2 = TestClass("Hitest2", "This is test class 2")
    print(test2.get_name())
    print(test2.is_this_static)
    print(test2.instance_message)

    test2.is_this_static = "XYZ" # only updates test2. Not static class attribute like Java

    test2.__name = "BrandNewName"

    print("-------")
    print(test1.get_name())
    print(test1.is_this_static)
    print(test2.get_name())
    print(test2.is_this_static)

if __name__ == "__main__":
    main()