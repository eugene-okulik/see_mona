for r in range(1, 101):
    if r % 3 == 0 and r % 5 == 0:
        print("FuzzBuzz")
    elif r % 3 == 0:
        print("Fuzz")
    elif r % 5 == 0:
        print("Buzz")
    else:
        print(r)
