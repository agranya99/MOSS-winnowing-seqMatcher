import pygments.token
import pygments.lexers
import hashlib
from cleanUP import *

#sha-1 encoding is used to generate hash values
def hash(text):
    #this function generates hash values
    hashval = hashlib.sha1(text.encode('utf-8'))
    hashval = hashval.hexdigest()[-4 :]
    hashval = int(hashval, 16)  #using last 16 bits of sha-1 digest 
    return hashval

#function to form k-grams out of the cleaned up text
def kgrams(text, k = 25):
    tokenList = list(text)
    n = len(tokenList)
    kgrams = []
    for i in range(n - k + 1):
        kgram = ''.join(tokenList[i : i + k])
        hv = hash(kgram)
        kgrams.append((kgram, hv, i, i + k))  #k-gram, its hash value, starting and ending positions are stored
        #these help in marking the plagiarized content in the original code.
    return kgrams

#function that returns the index at which minimum value of a given list (window) is located
def minIndex(arr):
    minI = 0
    minV = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] < minV:
            minV = arr[i]
            minI = i
    return minI

#we form windows of hash values and use min-hash to limit the number of fingerprints
def fingerprints(arr, winSize = 4):
    arrLen = len(arr)
    prevMin = 0
    currMin = 0
    windows = []
    fingerprintList = []
    for i in range(arrLen - winSize):
        win = arr[i: i + winSize]  #forming windows
        windows.append(win)
        currMin = i + minIndex(win)
        if not currMin == prevMin:  #min value of window is stored only if it is not the same as min value of prev window 
            fingerprintList.append(arr[currMin])  #reduces the number of fingerprints while maintaining guarantee
            prevMin = currMin  #refer to density of winnowing and guarantee threshold (Stanford paper)

    return fingerprintList

#takes k-gram list as input and returns a list of only hash values 
def hashList(arr):
    HL = []
    for i in arr:
        HL.append(i[1])

    return HL

def plagiarismCheck(file1, file2):
    f1 = open(file1, "r")
    token1 = tokenize(file1)  #from cleanUP.py
    str1 = toText(token1)    
    token2 = tokenize(file2)
    str2 = toText(token2)
    kGrams1 = kgrams(str1)  #stores k-grams, their hash values and positions in cleaned up text
    kGrams2 = kgrams(str2)
    HL1 = hashList(kGrams1)  #hash list derived from k-grams list
    HL2 = hashList(kGrams2)
    fpList1 = fingerprints(HL1)
    fpList2 = fingerprints(HL2)
    start = []   #to store the start values corresponding to matching fingerprints
    end = []   #to store end values
    code = f1.read()  #original code
    newCode = ""   #code with marked plagiarized content
    for i in fpList1:
        for j in fpList2:
            if i == j:   #fingerprints match
                match = HL1.index(i)   #index of matching fingerprints in hash list, k-grams list
                newStart = kGrams1[match][2]   #start position of matched k-gram in cleaned up code
                newEnd = kGrams1[match][3]   #end position
                for k in token1:
                    if k[2] == newStart:   #linking positions in cleaned up code to original code
                        start.append(k[1])
                    if k[2] == newEnd:
                        end.append(k[1])
    start = sorted(list(set(start)))
    if not len(start) == 0:
        newCode = code[: start[0]]
        for i in range(1, len(start)):
            newCode = newCode + '\x1b[6;30;42m' + code[start[i-1] : start[i]] + '\x1b[0m' #marking plagiarized code
        newCode = newCode + '\x1b[6;30;42m' + code[start[i] : end[len(end) -1]] + '\x1b[0m'
        newCode = newCode + code[end[len(end) - 1] :]
        print(newCode)
    else:
        print("NOT plagiarized")

fn1 = input("Enter the path/name of program 1: ")
fn2 = input("Enter the path/name of program 2: ")
plagiarismCheck(fn1, fn2)
