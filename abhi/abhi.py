def Abhi():
    return 'Abhishek Aggarwal'

def ReadFile(fname):
    with open(fname) as fi:
        return '\n'.join(fi.readlines())

def GetContent():
    return ReadFile('a.txt')





