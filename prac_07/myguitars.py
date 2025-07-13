

from prac_06.guitar import Guitar
def main():
    guitars = read_file('guitars.csv')
    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitars)
        print(f"{guitar_to_add}, added.")
        name = input("Name: ").title()

    print("\nAll guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    guitars.sort()
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars : (Quick, go and buy one!")

def read_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)



main()