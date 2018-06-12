import pygments.token
import pygments.lexers
from difflib import SequenceMatcher

def tokenize(filename):
    file=open(filename, "r")
    text=file.read()
    lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
    tokens = lexer.get_tokens(text)
    tokens=list(tokens)
    result=[]
    lenT=len(tokens)
    for i in range(lenT):
        if tokens[i][0] == pygments.token.Name and not i == lenT-1 and not tokens[i+1][1] == '(':
            result.append('N')
        elif tokens[i][0] in pygments.token.Literal.String:
            result.append('S')
        elif not i == lenT-1 and tokens[i+1][1]=='(' and not tokens[i][0] in pygments.token.Keyword:
            result.append('F')
        elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment:
            pass
        else:
            result.append(tokens[i][1])

    cleanText=''.join(str(x) for x in result)
    return cleanText

def plagerised_ratio(file1,file2):
    file1=tokenize(file1)
    file2=tokenize(file2)
    print(file1)
    print(file2)
    similarity_ratio = SequenceMatcher(None,file1,file2).ratio()
    print (similarity_ratio)# required ratio of plagerise
