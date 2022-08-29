for c in range(ord('a'), ord('z') + 1):
    if c != (ord('q') or ord('e')):
        print("{:c}".format(c), end=" ")
