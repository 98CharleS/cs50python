import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

table = []


def main():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            for row in reader:
                last, first = row["name"].split(",")

                table.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in table:
            writer.writerow(
                {"first": row["first"], "last": row["last"], "house": row["house"]}
            )


if __name__ == '__main__':
    main()
