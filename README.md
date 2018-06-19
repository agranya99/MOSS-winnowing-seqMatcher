# Measure of Software Similarity (Plagiarism Checker)
This project gives the measure of plagiarized content between software codes and also highlights the similar blocks
Python implementation of Winnowing approach as well as Sequence Matcher (difflib) approach

## Getting Started
 - Python 3.5+ required to execute seqMatcher.py and Python 3+ for winnowing.py

 - Pygments 2.1+
 
  Linux terminal
  ```
  sudo apt-get install python-pygments
  ```
  Windows shell (administrator)
  ```
  pip install pygments
  ```
## Usage
Run either winnowing.py / seqMatcher.py
```
python3 winnowing.py
```
```
python3 seqMatcher.py
```
The program will prompt you to enter path to the codes to be checked for plagiarism.

# cleanUp.py
The above program cleans the software codes to be checked for plagiarism by removing white spaces, denoising the content i.e replacing variable names throughout by 'N', strings by 'S' and  user defined function names by 'F'.

By cleaning up the codes, the efficiency of plagiarism detector is no longer affected by changes in identifiers.

# winnowing.py 
This program employs winnowing algorithm to detect plagiarized content. 

It takes paths to two code files as input. The output is the content of file 1 with plagiarized content highlighted. If there is no plagiarized content between the two code files then the output is simply 'Not Plagiarized'.

# seqMatcher.py
### Just a demonstration. For MOSS application, winnowing is more suited.
This program again  takes paths to two code files as input and produces two outputs:
1. The ratio of plagiarized content between them
2. The blocks of plagiarized code are printed (file 1 is used for printing). 

# Sequence Matcher approach 
### This approach although not preferable for building MOSS, can come handy in building normal text plagiarism checkers
Sequence matcher from Python module difflib is used after cleaning up the code to get percentage of plagiarized content as well as matching blocks.

The matching blocks are mapped to the original codes and the plagiarized code snippet is printed.

Changes in positions of blocks of codes does not affect the efficiency.

# Author
### Agranya Pratap Singh
Thanks to Shashwat Sanket (@shashwatsanket997) for suggesting use of Python difflib module (sequence matcher).

# References - Winnowing approach
The following research paper was referred for implementation of winnowing approach:      

(http://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf)    
