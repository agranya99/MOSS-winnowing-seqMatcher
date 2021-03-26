from winnowing import *
from seqMatcher import *


#Driver Code For Winnowing.py
check1 = winnowing("/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test2.py","/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test3.py")
result=check1.plagiarismCheck()
print("Approx ratio of plagiarized content in file 1: ", result['ratio'])
print(result['Code'])

#Driver Code For SeqMatcher.py
check2 = seqMatcher("/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test2.py","/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test3.py")
result=check2.plagerised_ratio()
print("Approx ratio of plagiarized content in file 1: ", result['ratio'])
print(result['Code'])