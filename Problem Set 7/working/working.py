import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_format = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    time = r"^" + time_format + " to " + time_format + "$"
    if matches := re.search(time, s):
        format_12 = reformat(matches.group(1), matches.group(2), matches.group(3))
        format_24 = reformat(matches.group(4), matches.group(5), matches.group(6))
        return f"{format_12} to {format_24}"
    else:
        raise ValueError


def reformat(hh, mm, xm):
    if hh == "12":
        if xm == "AM":
            hr = "00"
        else:
            hr = "12"
    else:
        if xm == "AM":
            hr = f"{int(hh):02}"
        else:
            hr = f"{int(hh) + 12}"
    if mm == None:
        min = "00"
    else:
        min = f"{int(mm):02}"

    return f"{hr}:{min}"


if __name__ == "__main__":
    main()
