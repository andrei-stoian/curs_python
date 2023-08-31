text = input("Introduceti valoarea liniei:")
nume = input("Nume:")

if text.isnumeric():
        print("Acesta este un sir de caractere tip integer")
elif isinstance(text, str):
        print("Sirul  de caractere acesta a fost gasit de ", {nume})
else:
    print("Textul este:", text)


numar = int(input("Introduceti numarul:"))

if numar % 2 == 0:
    print("Acesta este un numar par")
elif numar % 2 != 0:
    print("Acesta este un numar impar")

an = int(input("Introduceti an: "))

if an % 4 == 0:
    print("Acesta este un an bisect")
elif an % 4 != 0:
    print("Acesta nu este un an bisect")

numar = int(input('Introduceti numarul: '))

if numar > 0 and numar < 10:
    print("Numarul este mai mare ca 0 si mai mic ca 10")
elif numar == 0:
    print('Numarul este 0')
elif numar < 0:
    print(abs(numar))
else:
    print("Numarul nu este in range-ul din cerinta")




