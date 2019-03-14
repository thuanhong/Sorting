#!/usr/bin/env python3

import argparse


def bubbleSort(arr, file):
    for x in range(len(arr)-1, -1, -1):
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


def partition(arr, left, right, file):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            file.write(' '.join(str(v) for v in range(left, j+1)))
            file.write(' {} {}\n'.format(i, right))
            i += 1

    arr[i],arr[right] = arr[right], arr[i]
    file.write('{} {} {}\n'.format(right, i, right))
    return i

def quickSort(arr, left, right, file):
    if left < right:
        pivot = partition(arr, left, right, file)
        print('P:', pivot)
        print(*arr)
        quickSort(arr, left, pivot-1, file)
        quickSort(arr, pivot+1, right, file)


def merge(arr, start, mid, end, file):
    start2 = mid + 1

    if arr[mid] <= arr[start2]:
        return
    i = start
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            while index != start:
                file.write(str(index) + ' ')
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            file.write(str(start) + ' ')
            file.write('\n')

            start += 1
            mid += 1
            start2 += 1
    print(*arr[i:end])

def mergeSort(arr, l, r, file):
    if l < r:
        m = int((l+r) / 2)

        mergeSort(arr, l, m, file)
        mergeSort(arr, m + 1, r, file)
        merge(arr, l, m, r, file)


def handle_algor(algor, arr, file):
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
        mergeSort(arr, 0, len(arr) -1, file)
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
        handle_algor(args.algo, args.N, f)
    else:
        f.write('bubble' + '\n')
        f.write(' '.join(str(v) for v in args.N) + '\n')
        bubbleSort(args.N, f)
    f.close()

    if args.gui:
        if len(args.N) > 15:
            print('Input too large')
        else:
            from graphic import main
            main()
