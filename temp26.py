def main():
    s = "banana"
    char_map = {}

    for index, char in enumerate(s):
        if char not in char_map:
            char_map[char] = []
        char_map[char].append(index)


    for char in char_map:
        char_map[char] = tuple(char_map[char])

    print(char_map)


if __name__ == "__main__":
    main()
