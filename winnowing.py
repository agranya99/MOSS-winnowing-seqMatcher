import pygments.token
import pygments.lexers
import hashlib
from cleanUP import *

class winnowing():
    def __init__(self,file1,file2):
        self.file1=file1
        self.file2=file2
        self.token1 = tokenize(file1)  #from cleanUP.py
        self.str1 = toText(self.token1)
        self.token2 = tokenize(file2)
        self.str2 = toText(self.token2)
        self.kGrams1 = self.kgrams(self.str1)  #stores k-grams, their hash values and positions in cleaned up text
        self.kGrams2 = self.kgrams(self.str2)
        self.HL1 = self.hashList(self.kGrams1)  #hash list derived from k-grams list
        self.HL2 = self.hashList(self.kGrams2)
        self.fpList1 = self.fingerprints(self.HL1)
        self.fpList2 = self.fingerprints(self.HL2)

    def plagiarismCheck(self):
        file1 = self.file1
        file2 = self.file2
        f1 = open(file1, "r")
        start = []   #to store the start values corresponding to matching fingerprints
        end = []   #to store end values
        code = f1.read()  #original code
        newCode = ""   #code with marked plagiarized content
        points = []
        for i in self.fpList1:
            for j in self.fpList2:
                if i == j:   #fingerprints match
                    flag = 0
                    match = self.HL1.index(i)   #index of matching fingerprints in hash list, k-grams list
                    newStart = self.kGrams1[match][2]   #start position of matched k-gram in cleaned up code
                    newEnd = self.kGrams1[match][3]   #end position
                    for k in self.token1:
                        if k[2] == newStart:   #linking positions in cleaned up code to original code
                            startx = k[1]
                            flag = 1
                        if k[2] == newEnd:
                            endx = k[1]
                    if flag == 1:
                        points.append([startx, endx])
        points.sort(key = lambda x: x[0])
        points = points[1:]
        mergedPoints = []
        mergedPoints.append(points[0])
        for i in range(1, len(points)):
            last = mergedPoints[-1]
            if points[i][0] >= last[0] and points[i][0] <= last[1]: #merging overlapping regions
                if points[i][1] > last[1]:
                    mergedPoints = mergedPoints[:-1]
                    mergedPoints.append([last[0], points[i][1]])
                else:
                    pass
            else:
                mergedPoints.append(points[i])
        newCode = code[: mergedPoints[0][0]]
        plagCount = 0
        for i in range(len(mergedPoints)):
            if mergedPoints[i][1] > mergedPoints[i][0]:
                plagCount += mergedPoints[i][1] - mergedPoints[i][0]
                newCode = newCode + '\x1b[6;30;42m' + code[mergedPoints[i][0] : mergedPoints[i][1]] + '\x1b[0m'
                if i < len(mergedPoints) - 1:
                    newCode = newCode + code[mergedPoints[i][1] : mergedPoints[i+1][0]]
                else:
                    newCode = newCode + code[mergedPoints[i][1] :]
        return {"ratio":(plagCount/len(code)),"Code":newCode}

    #we form windows of hash values and use min-hash to limit the number of fingerprints
    def fingerprints(self,arr, winSize = 4):
        arrLen = len(arr)
        prevMin = 0
        currMin = 0
        windows = []
        fingerprintList = []
        for i in range(arrLen - winSize):
            win = arr[i: i + winSize]  #forming windows
            windows.append(win)
            currMin = i + self.minIndex(win)
            if not currMin == prevMin:  #min value of window is stored only if it is not the same as min value of prev window
                fingerprintList.append(arr[currMin])  #reduces the number of fingerprints while maintaining guarantee
                prevMin = currMin  #refer to density of winnowing and guarantee threshold (Stanford paper)

        return fingerprintList
    #takes k-gram list as input and returns a list of only hash values
    def hashList(self,arr):
        HL = []
        for i in arr:
            HL.append(i[1])

        return HL
    #function to form k-grams out of the cleaned up text
    def kgrams(self,text, k = 25):
        tokenList = list(text)
        n = len(tokenList)
        kgrams = []
        for i in range(n - k + 1):
            kgram = ''.join(tokenList[i : i + k])
            hv = self.hash(kgram)
            kgrams.append((kgram, hv, i, i + k))  #k-gram, its hash value, starting and ending positions are stored
            #these help in marking the plagiarized content in the original code.
        return kgrams
    #function that returns the index at which minimum value of a given list (window) is located
    def minIndex(self,arr):
        minI = 0
        minV = arr[0]
        n = len(arr)
        for i in range(n):
            if arr[i] < minV:
                minV = arr[i]
                minI = i
        return minI

    #sha-1 encoding is used to generate hash values
    def hash(self,text):
        #this function generates hash values
        hashval = hashlib.sha1(text.encode('utf-8'))
        hashval = hashval.hexdigest()[-4 :]
        hashval = int(hashval, 16)  #using last 16 bits of sha-1 digest
        return hashval



