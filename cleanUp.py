import pygments.token
import pygments.lexers

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

str1=tokenize("test1.py")
print(str1)
