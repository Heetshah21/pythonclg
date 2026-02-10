def main():
    mylist=[1,2,3,4,5,6,7,8,9]  
    mylist2=list(filter(lambda n:n%2==0,mylist))
    print(mylist2)
    odd=list(filter(lambda n:n%2!=0,mylist))
    print(odd)
if __name__ == "__main__":
    main()