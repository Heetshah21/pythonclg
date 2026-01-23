def main():
    inp=[1,3,5,6,7]
    number=int(input("enter a number to search its position: "))
    index=-1
    for i in range(len(inp)):
        if inp[i]<=number:
            continue
        else:
            index=i
            break
    print("index of the number is:", index)
if __name__ == "__main__":
    main()