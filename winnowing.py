import pygments.token
import pygments.lexers
import hashlib
from cleanUP import *


def hash(text):
    hashval = hashlib.sha1(text.encode('utf-8'))
    hashval = hashval.hexdigest()[-4 :]
    hashval = int(hashval, 16)
    return hashval

def kgrams(text, k = 25):
    tokenList = list(text)
    n = len(tokenList)
    kgrams = []
    for i in range(n - k + 1):
        kgram = ''.join(tokenList[i : i + k])
        hv = hash(kgram)
        kgrams.append((kgram, hv, i, i + k))
    return kgrams

def minIndex(arr):
    minI = 0
    minV = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] < minV:
            minV = arr[i]
            minI = i
    return minI

def fingerprints(arr, winSize = 4):
    arrLen = len(arr)
    prevMin = 0
    currMin = 0
    windows = []
    fingerprintList = []
    for i in range(arrLen - winSize):
        win = arr[i: i + winSize]
        windows.append(win)
        currMin = i + minIndex(win)
        if not currMin == prevMin:
            fingerprintList.append(arr[currMin])
            prevMin = currMin

    return fingerprintList

def hashList(arr):
    HL = []
    for i in arr:
        HL.append(i[1])

    return HL

def plagiarismCheck(file1, file2):
    f1 = open(file1, "r")
    token1 = tokenize(file1)
    str1 = toText(token1)
    token2 = tokenize(file2)
    str2 = toText(token2)
    kGrams1 = kgrams(str1)
    kGrams2 = kgrams(str2)
    HL1 = hashList(kGrams1)
    HL2 = hashList(kGrams2)
    fpList1 = fingerprints(HL1)
    fpList2 = fingerprints(HL2)
    start = []
    end = []
    code = f1.read()
    newCode = ""
    for i in fpList1:
        for j in fpList2:
            if i == j:
                match = HL1.index(i)
                newStart = kGrams1[match][2]
                newEnd = kGrams1[match][3]
                for k in token1:
                    if k[2] == newStart:
                        start.append(k[1])
                    if k[2] == newEnd:
                        end.append(k[1])
    start = sorted(list(set(start)))
    if not len(start) == 0:
        newCode = code[: start[0]]
        for i in range(1, len(start)):
            newCode = newCode + '\x1b[6;30;42m' + code[start[i-1] : start[i]] + '\x1b[0m'
        newCode = newCode + '\x1b[6;30;42m' + code[start[i] : end[len(end) -1]] + '\x1b[0m'
        newCode = newCode + code[end[len(end) - 1] :]
        print(newCode)
    else:
        print("NOT plagiarized")

plagiarismCheck("test2.py", "test3.py")
