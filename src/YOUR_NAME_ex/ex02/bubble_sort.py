def bubble_sort(iterable):
    data = list(iterable)
    sorting_lenght = len(data) - 1
    for i in range(sorting_lenght):
        for j in range(sorting_lenght - i):
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1], data[j]
    return data


if __name__ == "__main__":
    for data in ((),(1,),(1, 3, 8, 12),(12, 8, 3, 1),(8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
        
        
