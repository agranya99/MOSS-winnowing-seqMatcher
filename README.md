# Software Code Plagiarism-checker
MOSS-Measure of software similarity.
Python implementation of Winnowing approach as well as Sequence Matcher (difflib) approach

# References
The following research paper is being referred to for this implementation:      

(http://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf)    

# cleanUp.py
The above program cleans the software codes to be checked for plagiarism by removing white spaces, denoising the content i.e replacing variable names throughout by 'N', strings by 'S' and  user defined function names by 'F'.

By cleaning up the codes, the efficiency of plagiarism detector is no longer affected by changes in identifiers.

# Sequence Matcher approach
Sequence matcher from Python module difflib is used after cleaning up the code to get percentage of plagiarized content as well as matching blocks.

The matching blocks are mapped to the original codes and the plagiarized code snippet is printed.

Changes in positions of blocks of codes does not affect the efficiency.
