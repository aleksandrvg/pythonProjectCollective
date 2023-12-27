def BoubleSort(arr: list) -> list:
    pass


def Reverse(arr: list) -> list:
    reversed_list = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_list.append(arr[i])


if __name__ == "__main__":
    mass = [1, 2, 9, 3, 8, 23, 9, 228, 3]
    mass1 = BoubleSort(mass)
    mass2 = Reverse(mass)
    mass.reverse()
    if mass1 == mass2:
        print("Ok")
    else:
        print("Not Work")
