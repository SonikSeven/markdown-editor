def header():
    level = int(input("Level: "))
    if not 1 <= level <= 6:
        print("The level should be within the range of 1 to 6")
        return header()
    text = input('Text: ')
    return f"{'#' * level} {text}\n"


def four_in_one(k):
    char = {"plain": "", "bold": "**", "italic": "*", "inline-code": "`"}
    text = input('Text: ')
    return f"{char[k]}{text}{char[k]}"


def link():
    label, url = input('Label: '), input('URL: ')
    return f"[{label}]({url})"


def lists(k):
    char = {"ordered-list": "f'{n}. '", "unordered-list": "'* '"}
    rows = int(input("Number of rows: "))
    if rows < 1:
        print("The number of rows should be greater than zero")
        return lists(k)
    return "".join([eval(char[k]) + input(f"Row #{n}: ") + "\n" for n in range(1, rows + 1)])


def main(result=""):
    user_input = input("Choose a formatter: ")
    if user_input == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif user_input == "!done":
        with open("output.md", "w") as output:
            output.write(result)
        return
    elif user_input == "header":
        result += header()
    elif user_input in ("plain", "bold", "italic", "inline-code"):
        result += four_in_one(user_input)
    elif user_input == "new-line":
        result += "\n"
    elif user_input == "link":
        result += link()
    elif user_input in ("ordered-list", "unordered-list"):
        result += lists(user_input)
    else:
        print("Unknown formatting type or command")
        return main(result)
    print(result)
    return main(result)


main()
