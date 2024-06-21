NAME_TO_CODE = {"BABY BLUE": "#89cff0", "BABY PINK": "#f4c2c2", "BAKER-MILLER PINK": "ff91af", "BANANA MANIA": "#fae7b5", "BANANA YELLOW": "#ffe135",
                "BARN RED": "#7c0a02", "BATTLESHIP GRAY": "#848482", "BEAVER": "#9f8170", "BEIGE": "#f5f5dc", "BISQUE1": "#ffe4c4"}

is_valid_input = False
while not is_valid_input:
    try:
        colour_name = input("Enter colour name: ").upper()
        if colour_name == "":
            break
        colour_code = NAME_TO_CODE[colour_name]
        print(f"{colour_name.upper()}'s colour_code is {colour_code}")
    except KeyError:
        print("Invalid colour name")