#coding UTF-8
import sys, random
random.seed()
bytes = {}
base = {}
build = {}
i = 0
s = 0
d = random.randint(2,16)
d2 = random.randint(2,16)

while sys.stdin:
    i += 1
    if i == d2:
        sys.stdout.write("! ")
        sys.stdout.flush()
        i = 0
        d2 = random.randint(2,16)
    character = sys.stdin.read(1)
    if not character:
        sys.stdout.flush()
        exit()
    charbyte = character.encode('hex')
    bytes[0] = int(charbyte[0], 16)
    bytes[1] = int(charbyte[1], 16)
    pad_1 = "q" * (16 - bytes[0])
    pad_2 = "q" * (16 - bytes[1])
    a = ("Q" * bytes[0]) + pad_1
    b = ("Q" * bytes[1]) + pad_2
    a_scramble = list(a)
    random.shuffle(a_scramble)
    a = ''.join(a_scramble)
    b_scramble = list(b)
    random.shuffle(b_scramble)
    b = ''.join(b_scramble)
    coded = a + b
    for char in coded:
        sys.stdout.write(char)
        s += 1
        if s == d:
            sys.stdout.write(" ")
            sys.stdout.flush()
            s = 0
            d = random.randint(2,16)
