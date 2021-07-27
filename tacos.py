from itertools import count

# init array
arr = ["tortilla", "cheese", "meat", "MORE MEAT"]

# main function


def main():
    for _ in count(0):
        inp = input("taco? > ")
        if "taco" in inp:
            if _ <= 4:
                print(arr[_-1])
            else:
                print(arr[3])
        else:
            _ -= 1
            print("Try again")


while True:
    main()
