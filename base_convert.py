#int => str
#can change the base of any given integer
def convert(num, b):
    if num//b == 0:
        if b < 10:
            return str(num%b)
        else:
            if num%b == 10:
                return 'A'
            elif num%b == 11:
                return 'B'
            elif num%b == 12:
                return 'C'
            elif num%b == 13:
                return 'D'
            elif num%b == 14:
                return 'E'
            elif num%b == 15:
                return 'F'
            else:
                return str(num%b)



    if b < 10:
        reduced = num//b
        y = convert(reduced,b)
        return y + str(num%b)

    else:
        reduced = num//b
        remainder = num%b
        y = convert(reduced,b)

        if remainder == 10:
            return y + 'A'
        elif remainder == 11:
            return y + 'B'
        elif remainder == 12:
            return y + 'C'
        elif remainder == 13:
            return y + 'D'
        elif remainder == 14:
            return y + 'E'
        elif remainder == 15:
            return y + 'F'
        else:
            return y + str(num%b)

