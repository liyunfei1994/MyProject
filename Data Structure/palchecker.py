import deque

def palchecker(astring):

    char = deque.Deque()

    for ch in astring:
        char.addrear(ch)

    print(char.items)

    stillequal = True

    while char.size() > 1 and stillequal:
        first = char.removefront()
        print("first-->", first)
        last = char.removerear()
        print("last-->", last)
        if first != last:
            stillequal = False

    return stillequal


print(palchecker( "abcdeba"))
