MESSAGE = "Fs knwlw wpaklmbm vns vjmzq hjgyjseslgjgn. La ug hjgyjsembm n Hqlzgfw s la ug ks eqdas."


# def decrypter(message, shift):
#     pass

def decrypter(message: str, shift: int) -> str:
    shift = 26 - shift
    result = ""
    for i in message:
        if i.isupper() and i.isalpha():
            result += chr((ord(i) + shift - 65) % 26 + 65)
        elif i.isalpha():
            result += chr((ord(i) + shift - 97) % 26 + 97)
        else:
            result += i
    return result


def brute_force_decrypter(message: str) -> list:
    ret_val = []
    for shift in range(26):
        result = ""
        for i in message:
            if i.isupper() and i.isalpha():
                result += chr((ord(i) + shift - 65) % 26 + 65)
            elif i.isalpha():
                result += chr((ord(i) + shift - 97) % 26 + 97)
            else:
                result += i
        ret_val.append(result)
    return ret_val


if __name__ == "__main__":
    print(decrypter(MESSAGE, 18))
    print()
    print(brute_force_decrypter(MESSAGE))
