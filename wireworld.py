#!/usr/bin/python
from time import sleep
from os import system
from copy import deepcopy


def printmap(map):
    system("clear")
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            print arr[y][x],
        print "\n\n"


def step(arr):
    tmp = deepcopy(arr)

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == "G":
                tmp[y][x] = "X"
                continue
            if arr[y][x] == "X":
                tmp[y][x] = "O"
                continue
            if arr[y][x] == "O":
                elcount = 0
                try:
                    if arr[y-1][x-1] == "G":
                        elcount += 1
                    if arr[y-1][x] == "G":
                        elcount += 1
                    if arr[y-1][x+1] == "G":
                        elcount += 1

                    if arr[y][x-1] == "G":
                        elcount += 1
                    if arr[y][x+1] == "G":
                        elcount += 1

                    if arr[y+1][x-1] == "G":
                        elcount += 1
                    if arr[y+1][x] == "G":
                        elcount += 1
                    if arr[y+1][x+1] == "G":
                        elcount += 1
                except IndexError:
                    pass

                if 1 <= elcount <= 2:
                    tmp[y][x] = "G"
                continue
    return tmp


if __name__ == "__main__":
    arr = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "O", "O", " ", " ", " ", " "],
        ["X", "G", "O", "O", "O", "O", " ", "O", "O", "O", "O"],
        [" ", " ", " ", " ", " ", "O", "O", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", "O", "O", " ", " ", " "],
        ["X", "G", "O", "O", "O", "O", " ", "O", "O", "O", "O"],
        [" ", " ", " ", " ", " ", " ", "O", "O", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ]
    while True:
        arr = step(arr)
        printmap(arr)
        sleep(1)
