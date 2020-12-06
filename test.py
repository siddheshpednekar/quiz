'''from tkinter import *

OPTIONS = (
    "egg",
    "go",
    "spam"
)

root = Tk()

var = StringVar()
var.set(OPTIONS[0]) # default

def callbackFunc(name, index, mode):
    value = var.get()
    if value == 'go':
        om.config(bg='green',fg='black',
                 activebackground='green',
                 activeforeground='black')
    else:
        om.config(bg='SystemButtonFace',fg='SystemButtonText',
                 activebackground='SystemButtonFace',
                 activeforeground='SystemButtonText')

om = OptionMenu(root, var, *OPTIONS)
om.pack()

Callbackname = var.trace_variable('w', callbackFunc)

root.mainloop()'''


'''from itertools import combinations_with_replacement
import random

def random_generate_comb(lst):
    x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    data =  set(combinations_with_replacement(x, 6))
    return "".join(random.choice(list(data.difference(lst))))

print(random_generate_comb(['abcggj', 'def7tg', 'ijkhh']))'''

'''import random
from string import ascii_letters,digits

def random_generate(in_list):
    x = ascii_letters + digits + '+/'
    random_ = ''.join(list((random.choice(x) for num in range(6))))
    while random_ in in_list:
        random_ = ''.join(list((random.choice(x) for num in range(6))))
    print(random_)


random_generate(['abcdef', 'defilk', 'imjklm'])'''


'''import random
from string import ascii_letters,digits

def random_generate(in_list):
    x = ascii_letters + digits + '+/'
    random_ = ''.join(list((random.choice(x) for num in range(6))))
    while random_ in in_list:
        random_ = ''.join(list((random.choice(x) for num in range(6))))
    print(random_)


random_generate([])'''
txt = "hello   ||   world"
txtspl = txt.split("   ||   ")
print(txtspl)
print(txtspl[1])
