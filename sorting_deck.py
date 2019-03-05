#!/usr/bin/env python3

import argparse


def bubbleSort(arr):
    n = len(arr)
    for x in range(n-1, -1, -1):
        for y in range(x):
            if arr[y+1] < arr[y]:
                arr[y+1], arr[y] = arr[y], arr[y+1]
                print(' '.join(str(v) for v in arr))


def insertSort(arr):
    n = len(arr)
    for x in range(1, n):
        temp = arr[x]
        count = x - 1
        swap = False
        while count >= 0 and temp < arr[count]:
            swap = True
            arr[count+1] = arr[count]
            count -= 1
        if swap:
            print(' '.join(str(v) for v in arr))
        arr[count+1] = temp


def quickSort(arr, left, right):
    if left == right:
        return
    pivot = arr[int((left + right) / 2)]
    i, j = left, right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    print('P: {}'.format(pivot))
    print(' '.join(str(v) for v in arr))
    if left < j:
        quickSort(arr, left, j)
    if right > i:
        quickSort(arr, i, right)
    return True


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
        print(' '.join(str(v) for v in arr))


def main(algor, arr):
    if algor == 'insert':
        insertSort(arr)
    elif algor == 'quick':
        quickSort(arr, 0, len(arr) - 1)
    elif algor == 'merge':
        mergeSort(arr)
    else:
        bubbleSort(arr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str,
                        help='specify which algorithm to use for sorting among\
                        [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    parser.add_argument('N', nargs='+', type=int,
                        help='an integer for the list to sort')

    args = parser.parse_args()
    if args.gui:
        if len(args.N) > 15:
            print('Input too large')
        else:
            pass
    else:
        if args.algo:
            main(args.algo, args.N)
        else:
            bubbleSort(args.N)
