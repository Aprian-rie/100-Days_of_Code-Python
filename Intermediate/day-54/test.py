def outer_function():
    print("I'm Outer")

    def nested_function():
        print("I'm Inner")

    return nested_function


inner_function = outer_function()
inner_function()
