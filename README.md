# Software Code Plagiarism-checker
MOSS-Measure of software similarity.
Python implementation of Winnowing approach as well as Sequence Matcher (difflib) approach

# cleanUp.py
The above program cleans the software codes to be checked for plagiarism by removing white spaces, denoising the content i.e replacing variable names throughout by 'N', strings by 'S' and  user defined function names by 'F'.

By cleaning up the codes, the efficiency of plagiarism detector is no longer affected by changes in identifiers.

# winnowing.py
This program employs winnowing algorithm to detect plagiarized content. 

It takes paths to two code files as input. The output is the content of file 1 with plagiarized content highlighted. If there is no plagiarized content between the two code files then the output is simply 'Not Plagiarized'.

# seqMatcher.py
This program again  takes paths to two code files as input and produces two outputs:
1. The ratio of plagiarized content between them
2. The blocks of plagiarized code are printed (file 1 is used for printing). 

# Sequence Matcher approach
Sequence matcher from Python module difflib is used after cleaning up the code to get percentage of plagiarized content as well as matching blocks.

The matching blocks are mapped to the original codes and the plagiarized code snippet is printed.

Changes in positions of blocks of codes does not affect the efficiency.

# References - Winnowing approach
The following research paper is being referred to for implementation of winnowing approach:      

(http://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf)    
