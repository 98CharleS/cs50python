def main():
    u_time = input("What time is it? ")
    if any(u_time):
        d_time = convert(u_time)
        if 7 <= d_time and 8 >= d_time:
            print("breakfast time")
        elif 12 <= d_time and 13 >= d_time:
            print("lunch time")
        elif 18 <= d_time and 19 >= d_time:
            print("dinner time")
    else:
        None


def convert(time):
    h, m = time.split(sep=":")
    return int(h) + int(m)/60



if __name__ == "__main__":
    main()
