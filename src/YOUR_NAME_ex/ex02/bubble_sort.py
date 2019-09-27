def bubble_sort(data):
    for i in data:
        res = data[i]-data[i+1]

    
    a=sorted(data)
    return a


if __name__ == "__main__":
    for data in ((),(1,),(1, 3, 8, 12),(12, 8, 3, 1),(8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
        
        
        
Start with the first element in the list, compare it with the second.
If they are in wrong order, exchange them.
Now compare the second and third element and exchange them if necessary.
Proceed with third and fourth, fourth and fifth, etc, until you have compared and, if necessary, swapped the second-last and last elements.
At this point, the last element in the list will be the largest element in the list (why?).
Now start again from the beginning of the list, but stop once you reach the second-last element in the list.
Then, start again from the begining of the list, but stop once you reach the third-last element in the list, etc, until just the first and second element are left to compare.