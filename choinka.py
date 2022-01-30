def create_tree():
    try:
        height = int(input("Jak wysoką chcesz mieć choinkę? (wpisz liczbę): "))
    except ValueError:
        print("to nie jest właściwa wysokość (spróbuj użyć liczby")
        height = 0

    for i in range(height):
        print(" " * (height-i) + "*" * (i*2+1) + " " * (height-i))
    print(" "*height + "|")
    print("\n"*2)


are_we_finished = "N"
while are_we_finished == 'Y' or 'y':
    create_tree()
    input("kończymy? (Y/N): ")
