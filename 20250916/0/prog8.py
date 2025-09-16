match int(input()):
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case n if n % 2 == 0:
        print("EVEN")
    case n:
        print(n, "is too much")