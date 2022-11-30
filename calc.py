while True:
    a=float(input("Веддіть число: "))
    what=input("Введіть дію: ")
    b=float(input("Веддіть число: "))
    if what == "+":
        print(a+b)
    elif what == "-":
        print(a-b)
    elif what == "*":
        print(a*b)
    elif what == "/":
        if b == 0:
            print("на нуль ділити не можна")
        else:
            print(a/b)
    else:
        print("Вибрана не правильна дія")