def main():
    result = {}
    dict1 = [{"a": 2, "b": 3}, {"a": 4, "c": 1}]
    for d in dict1:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    print(result)
if __name__ == "__main__":
    main()