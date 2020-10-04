def a(s):
    for i in s:
        if i.isalnum():  
            return True
    return False
    
def b(s):
    for i in s:
        if i.isalpha():
            return True
    return False
    
def c(s):
    for i in s:
        if i.isalpha():
            return True

    return False

def d(s):
    for i in s:
        if i.isdigit(): 
            return True
    return False

def e(s):
    for i in s:
        if i.isupper():
            return True
    return False

if __name__ == '__main__':
    s = input()
    print(a(s))
    print(b(s))
    print(c(s))
    print(d(s))
    print(e(s))