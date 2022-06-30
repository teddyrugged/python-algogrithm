'''creatiion of a cypher machine to encrypt and decrypt text messages to code and codes to text messages'''
from re import A


def chriptogtaphy():
    while True:
        req = input("Enter A to encrypt or B decrypt else q to quit: ").upper()
        if req == "Q":
            break
        text = input ("Enter plain text: ")
        try:
             key = int(input("input key: "))
        except ValueError:
            print("Invalide")
            chriptogtaphy()
        alpha = "abcdefghijklmnopqrstuvwxyz"
        res = []
        if req == "A":
            for i in text:
                if i in alpha:
                    res.append(alpha[(alpha.index(i)+key) % 26 ]) 
                else:
                    res.append(i)
            print("".join(res))
        elif req == "B":
            for i in text:
                if i in alpha:
                    res.append(alpha[(alpha.index(i)-key) % 26]) 
                else:
                    res.append(i)
            print("".join(res))
    return "Thanks for using our service!!!....."
      
print(chriptogtaphy())