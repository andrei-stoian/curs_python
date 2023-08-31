meniu = ['1 - Afisare lista de cumparaturi', '2 - Adaugare element', '3 - Stergere element', '4 - Stergere lista de cumparaturi', '5 - Cautare in lista de cumparaturi', '6 - Iesire']
lista_cumparaturi = ['cartofi' ,'morocovi' ,'castraveti' ,'rosii' ,'branza']

while True:
    for lista_meniu in meniu:
        print(lista_meniu)

    selectare_meniu = input("Selectati varianta dorita: ")

    if selectare_meniu == '1':
        for list_produse in lista_cumparaturi:
            print(list_produse)

    elif selectare_meniu == '2':
        print("Adaugati in lista: ")
        adaugare_lista = input()
        lista_cumparaturi.append(adaugare_lista)
        for list_produse in lista_cumparaturi:
            print(list_produse)

    elif selectare_meniu == '3':
        print("Stergeti din lista: ")
        stergere_din_lista = input()
        lista_cumparaturi.remove(stergere_din_lista)
        print(lista_cumparaturi)

    elif selectare_meniu == '4':
        lista_cumparaturi.clear()
        print("Lista de cumparaturi a fost stearsa", lista_cumparaturi)

    elif selectare_meniu == '5':
        print("Cautati in lista de cumparaturi: ")
        cautare_lista = input()
        if cautare_lista in lista_cumparaturi:
            print(cautare_lista + " este in lista")
        else:
            print(cautare_lista + " nu este in lista")

    elif selectare_meniu == '6':
        print("Iesire din aplicatie. La revedere!")
        break

    else:
        print("Alegerea nu exista. Reincercati")

    into_menu = input("Reveniti la meniu? (da/nu): ")
    if into_menu.lower() != 'da':
        print("Iesire din aplicatie. La revedere!")
        break