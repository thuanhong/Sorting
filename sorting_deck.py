#!/usr/bin/env python3

import argparse


def bubbleSort(arr, file):
    n = len(arr)
    for x in range(n-1, -1, -1):
        for y in range(x):
            if arr[y+1] < arr[y]:
                arr[y+1], arr[y] = arr[y], arr[y+1]
                file.write('{} {}'.format(y, y+1) + '\n')
                print(*arr)


def insertSort(arr, file):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        swapped = False
        if temp < arr[j]:
            file.write(str(i) + ' ')
        while j >= 0 and temp < arr[j]:
            file.write(str(j) + ' ')
            arr[j+1] = arr[j]
            swapped = True
            j -= 1
        arr[j+1] = temp

        if swapped:
            print(*arr)
            file.write('\n')


def quickSort(arr, left, right, file):
    if left < right:
        i = (left -1)
        pivot = arr[right]
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                if i == j:
                    continue
                arr[i], arr[j] = arr[j], arr[i]
                file.write('{} {} {}\n'.format(i, j, right))


        arr[i+1],arr[right] = arr[right], arr[i+1]
        file.write('{} {} {}\n'.format(i+1, right, right))
        pi = i+1
        print('P:', pivot)
        print(*arr)
        quickSort(arr, left, i, file)
        quickSort(arr, i+2, right, file)


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i+1
            else:
                arr[k] = right[j]
                j = j+1
            k = k+1

        while i < len(left):
            arr[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            arr[k] = right[j]
            j = j+1
            k = k+1
        print(*arr)


def main(algor, arr, file):
    if algor.isdigit():
        file.write('bubble' + '\n')
    else:
        file.write(algor + '\n')
    file.write(' '.join(str(v) for v in arr) + '\n')
    if algor == 'insert':
        insertSort(arr, file)
    elif algor == 'quick':
        quickSort(arr, 0, len(arr) - 1, file)
    elif algor == 'merge':
        mergeSort(arr)
    else:
        bubbleSort(arr, file)


def take_arugment():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str,
                        help='specify which algorithm to use for sorting among\
                        [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    parser.add_argument('N', nargs='+', type=int,
                        help='an integer for the list to sort')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = take_arugment()
    f = open('data', 'w')

    if args.algo:
        main(args.algo, args.N, f)
    else:
        file.write('bubble' + '\n')
        bubbleSort(args.N, f)
    f.close()

    if args.gui:
        if len(args.N) > 15:
            print('Input too large')
        else:
            from graphic import main
            main()
