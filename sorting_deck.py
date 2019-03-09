#!/usr/bin/env python3

import argparse


def bubbleSort(arr, file):
    n = len(arr)
    file.write(' '.join(str(v) for v in arr) + '\n')
    for x in range(n-1, -1, -1):
        for y in range(x):
            if arr[y+1] < arr[y]:
                arr[y+1], arr[y] = arr[y], arr[y+1]
                file.write('{} {}'.format(y, y+1) + '\n')
                print(*arr)


def insertSort(arr, file):
    file.write(' '.join(str(v) for v in arr) + '\n')
    for i in range(1, len(arr)):
        if arr[i] < max(arr[:i]):
            for j in range(i):
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                    file.write(str(j) + ' ')
            file.write(str(i) + '\n')
            print(*arr)


def quickSort(arr, left, right):
    if left < right:
        i, j, pivot = left, right, arr[left]
        while i <= j:
            if arr[i] > pivot > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            if arr[i] <= pivot:
                i += 1
            elif arr[i] > pivot and arr[j] >= pivot:
                j -= 1
        arr[left], arr[i - 1] = arr[i - 1], arr[left]
        print('P:', pivot)
        print(*arr)
        quickSort(arr, left, i - 2)
        quickSort(arr, i, right)


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
    if algor == 'insert':
        insertSort(arr, file)
    elif algor == 'quick':
        quickSort(arr, 0, len(arr) - 1)
    elif algor == 'merge':
        mergeSort(arr)
    else:
        bubbleSort(arr, file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str,
                        help='specify which algorithm to use for sorting among\
                        [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    parser.add_argument('N', nargs='+', type=int,
                        help='an integer for the list to sort')
    f = open('data', 'w')
    args = parser.parse_args()
    if args.gui:
        if len(args.N) > 15:
            print('Input too large')
        else:
            pass
    else:
        if args.algo:
            main(args.algo, args.N, f)
        else:
            bubbleSort(args.N, f)
    f.close()
