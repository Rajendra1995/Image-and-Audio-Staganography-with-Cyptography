import random
global plaintext, numP, q, j, z, X, C
# Encrypting Scheme used
global m, P, C, x, h, p, Text, y, w
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
          "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", ".", "!", "?", " ", "A", "B", "C", "D", "E", "F",
          "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

number = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
          "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
          "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45",
          "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57"]


# Second decrypt function used under Decrypt RSA
def decrypt(F, d):
    if d == 0:
        return 1
    if d == 1:
        return F
    w, r = divmod(d, 2)
    if r == 1:
        return decrypt(F * F % n, w) * F % n
    else:
        return decrypt(F * F % n, w)


# Correcting the decoded image message
def correct():
    for i in range(len(C)):
        if len(str(P[i])) % 2 != 0:
            y = str(0) + str(P[i])
            P.remove(str(P[i]))
            P.insert(i, y)


# Cipher used for encrypting message
def cipher(b, e):
    if e == 0:
        return 1
    if e == 1:
        return b
    w, r = divmod(e, 2)
    if r == 1:
        return cipher(b * b % n, w) * b % n
    else:
        return cipher(b * b % n, w)


# Grouping the Characters
def group(j, h, z):
    for i in range(int(j)):
        y = 0
        for n in range(h):
            y += int(numP[(h * i) + n]) * (10 ** (z - 2 * n))
        X.append(int(y))


# Finding GCD used in RSA
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def Decrypt(txt):
    # decrypts an encoded message
    global m, P, C, x, h, p, Text, y, w

    # Encoded Image
    hidden_text = txt

    P = []
    C = hidden_text

    for i in range(len(C)):
        x = decrypt(int(C[i]), d)
        P.append(str(x))
    correct()

    h = len(P[0])
    p = []
    for i in range(len(C)):
        for n in range(int(h / 2)):
            p.append(str(P[i][(2 * n):((2 * n) + 2)]))

    Text = []
    for i in range(len(p)):
        for j in range(len(letter)):
            if str(p[i]) == number[j]:
                Text.append(letter[j])
    PText = str()
    for i in range(len(Text)):
        PText = PText + str(Text[i])

    return PText


def Encrypt(txt):
    # encrypts a plaintext message using the current key
    global plaintext, numP, q, j, z, X, C

    plaintext = txt
    numP = []

    for i in range(len(plaintext)):
        for j in range(len(letter)):
            if plaintext[i] == letter[j]:
                numP.append(number[j])

    h = (len(str(n)) // 2) - 1
    q = len(numP) % h

    for i in range(h - q):
        numP.append(number[random.randint(0, 25)])
    j = len(numP) / h

    X = []
    z = 0

    for m in range(h - 1):
        z += 2
    group(j, h, z)
    k = len(X)
    C = []

    for i in range(k):
        b = X[i]
        r = cipher(b, e)
        C.append(r)

    return C[:-1]


def setup():
    global n, e, d
    while True:
        try:
            n = int(input(" Enter a value for n :"))
            if n > 2:
                break
        except ValueError:
            print('please enter a number')
    while 1 != 2:
        try:
            e = int(input(" Enter a value for e :"))
            if e >= 2:
                break
        except ValueError:
            print('please enter a number')
    while True:
        try:
            d = int(input(" Enter a value for d. If d unknown, enter 0 :"))
            if d >= 0:
                break
        except ValueError:
            print('please enter a number')


# setup()
n = 2537
e = 13
d = 937
