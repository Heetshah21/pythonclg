def main():
    input=[2,5,4,2,8,9,5,3,6,2,4]
    i=0
    while i <len(input):
        if (input.index(input[i])!=i):
            input.remove(input[i])
        else:
            i=i+1

    print("removed duplicates:", input)
if __name__ == "__main__":
    main()