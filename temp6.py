def main():
    numbers = [3, 5, 2, 4, 1]
    result=[]
    sum = 0
    for i in numbers:
        sum += i;
        result.append(sum)
        
    print("Cumulative sums:", result)
if __name__ == "__main__":
    main()