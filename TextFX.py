class attributesclass:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def GenText(attributes,text):
    generated = ''
    for i in attributes:
        generated += eval(f'attributesclass.{i.upper()}')
    generated += (text + attributesclass.ENDC)
    return generated

def Space(x):
    for _ in range(x):
        print()

def GenLine(length):
    generated = ''
    for _ in range(length*5):
        generated += '━'
    return generated

def TextOptions():
    Space(2)
    print(GenText(['bold','green', 'underline'], 'TextFX:'))
    print(GenText(['PURPLE'], '- PURPLE'))
    print(GenText(['BLUE'], '- BLUE'))
    print(GenText(['CYAN'], '- CYAN'))
    print(GenText(['YELLOW'], '- YELLOW'))
    print(GenText(['RED'], '- RED'))
    print(GenText(['BOLD'], '- BOLD'))
    print(GenText(['UNDERLINE'], '- UNDERLINE'))

    Space(2)
TextOptions()
