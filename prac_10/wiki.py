import wikipedia

while True:
    # Prompt the user for a page title or search phrase
    search_input = input("Enter a page title or search phrase (or leave blank to exit): ")
    if not search_input:
        break  # Exit the loop if the input is blank