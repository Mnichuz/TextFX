class attributesclass:
    PURPLE = '\033[95m'
    ORANGE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GRAY = '\033[90m'
    WHITE = '\033[37m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Text(attributes,text):
    generated = ''
    for i in attributes:
        generated += eval(f'attributesclass.{i.upper()}')
    generated += (text + attributesclass.ENDC)
    return generated

def purple(text):
    return Text(['purple'], text)

def cyan(text):
    return Text(['cyan'], text)

def green(text):
    return Text(['green'], text)

def yellow(text):
    return Text(['yellow'], text)

def orange(text):
    return Text(['orange'], text)

def red(text):
    return Text(['red'], text)

def gray(text):
    return Text(['gray'], text)

def white(text):
    return Text(['white'], text)

def bold(text):
    return Text(['bold'], text)

def underline(text):
    return Text(['underline'], text)

def Space(x):
    for _ in range(x):
        print()

def Line(length):
    generated = ''
    for _ in range(length*5):
        generated += '━'
    return generated

def TextOptions():
    Space(2)
    print(Text(['bold','green', 'underline'], 'TextFX:'))
    print(Text(['PURPLE'], '- PURPLE'))
    print(Text(['CYAN'], '- CYAN'))
    print(Text(['GREEN'], '- GREEN'))
    print(Text(['YELLOW'], '- YELLOW'))
    print(Text(['ORANGE'], '- ORANGE'))
    print(Text(['RED'], '- RED'))
    print(Text(['GRAY'], '- GRAY'))
    print(Text(['BOLD'], '- BOLD'))
    print(Text(['UNDERLINE'], '- UNDERLINE'))

    Space(2)

