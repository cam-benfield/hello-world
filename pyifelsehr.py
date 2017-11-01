nw = "Not Weird"
w = "Weird"
if __name__ == '__main__':
    n = int(raw_input())
    if n > 20 and n % 2 == 0:
        print nw

    if n <= 20 and n >= 6 and n % 2 == 0:
        print w

    if n % 2 != 0:
        print w

    if n == 2 or n == 4:
        print nw
