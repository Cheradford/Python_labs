def XOR(txt):
    key = "sekret"
    temp = ""
    for i in range(len(txt)):
        temp += chr(ord(key[i % len(key)]) ^ ord(txt[i]))
    return temp


def sycleShift(ch: int, shift: int) -> int:
    bitLen = 8
    signed = shift < 0

    if not signed:
        for _ in range(abs(shift)):
            l = ch // 2
            r = ch % 2
            ch = (r << bitLen - 1) + l
    else:
        for i in range(abs(shift)):
            l = ch // (2 ** (bitLen - 1))
            r = ch % (2 ** (bitLen - 1))
            ch = (r << 1) + l

    return ch

def Cicle(txt, key):
    temp = ""
    for i in txt:
        temp += chr(sycleShift(ord(i), key))
    return temp


def main_loop():
    text = input("Введите текст для шифрования->")
    key = 1
    print("1.\tШифрование с помощью операции \"XOR\"\n" +
          "2.\tШифрование с помощью циклического сдвига\n" +
          "3.\tВвести число позиций для шифрования путем циклического сдвига\n" +
          "4.\tВыход.")
    while True:
        i = input()
        if i == "1":
            print("Исходный текст->", text)
            text = XOR(text)
            print("Новый текст->", text)
        if i == '2':
            print("Исходный текст->", text)
            text = Cicle(text, key)
            print("Новый текст->", text)
        if i == '3':
            key = int(input("Введите новый ключ сдвига->"))
        if (i == '4') or (i == ''):
            exit(0)


main_loop()
