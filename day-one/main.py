list_one = []
list_two = []

def parse_lists(filename = "data.txt"):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) == 2:
                num1 = int(parts[0])
                num2 = int(parts[1])
                list_one.append(num1)
                list_two.append(num2)

    return list_one, list_two


def confirm_list_length(list_one, list_two):
    if len(list_one) != len(list_two):
        sys.exit("Lists are not the same length")

def list_orderer(list_one, list_two):
    list_one.sort()
    list_two.sort()

    return list_one, list_two

def compare_lists(list_one, list_two):
    total = 0
    for i in range(len(list_one)):
        if list_one[i] > list_two[i]:
            distance = list_one[i] - list_two[i]
            total += distance
        elif list_one[i] < list_two[i]:
            distance = list_two[i] - list_one[i]
            total += distance
    return total

def main():
    parse_lists(filename = "data.txt")
    confirm_list_length(list_one, list_two)
    list_orderer(list_one, list_two)
    total = compare_lists(list_one, list_two)
    print(total)

if __name__=="__main__":
    main()