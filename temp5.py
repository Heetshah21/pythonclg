def week(i):
    switcher = {
        0:"Sunday",
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday"        
    }
    return switcher.get(i,"Invalid day")

def main():
    day=week(4)
    print("Day is:",day)
  
if __name__ == "__main__":
    main()