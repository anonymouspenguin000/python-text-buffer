import sys
import os
from colorama import *
from help import help
from files import *
import db

texts = {}
texts = db.get()

print('----------------Text Buffer----------------')
print('Type <help> to get help. Type <cls> to clear the screen.')



def cmd():
    init()
    print(Fore.WHITE + '')
    c = input('Command>')
    kws = c.split() or [0]
    for i in kws:
        if i == '':
            c.remove(i)
    if kws[0] == 'export':
        try:
            f = File(kws[2], texts[kws[1]])
            dt = f.set()
            dt.close()
            print(Fore.GREEN + 'Success! Text has been exported.')
        except IndexError:
            print(Fore.RED + 'Enter the arguments!')
        except KeyError:
            print(Fore.RED + 'No such key!')
    elif kws[0] == 'get':
        try:
            print(Fore.CYAN + texts[kws[1]])
        except KeyError:
            print(Fore.RED + 'No such key! Try again!')
        except IndexError:
            for key in texts.keys():
                print(Fore.CYAN + key)
    elif kws[0] == 'set':
        try:
            db.set(kws[1], kws[2])
            texts[kws[1]] = kws[2]
            print(Fore.GREEN + 'Success! Variable has been saved.')
        except IndexError:
            print(Fore.RED + 'Enter the arguments!')
    elif kws[0] == 'del':
        try:
            db.dlt(kws[1])
            texts.pop(kws[1])
            print(Fore.GREEN + 'Success! Variable has been removed.')
        except IndexError:
            print(Fore.RED + 'Enter the argument!')
        except KeyError:
            print(Fore.RED + 'No such key! Try again!')
    elif kws[0] == 'exit':
        sys.exit()
    elif kws[0] == 'import':
        try:
            f = File(kws[2])
            txt = f.get()
            db.dlt(kws[1]);
            texts[kws[1]] = '';
            for line in txt:
                texts[kws[1]] += line + '\n';
            db.set(kws[1], texts[kws[1]])
            print(Fore.GREEN + 'Success! Text has been imported.')
        except IndexError:
            print(Fore.RED + 'Enter the arguments!')
        except FileNotFoundError:
            print(Fore.RED + 'No such file!')
    elif kws[0] == 'export-end':
        try:
            f = File(kws[2], texts[kws[1]])
            f.add()
            print(Fore.GREEN + 'Success! Text has been exported to end of file.')
        except IndexError:
            print(Fore.RED + 'Enter the arguments!')
    elif kws[0] == 'help':
        try:
            comm = kws[1]
        except IndexError:
            comm = 'all'
        try:
            print(help[comm])
        except KeyError:
            print(Fore.RED + 'No such command!')
    elif kws[0] == 'cls':
        os.system('cls')
    else:
        if kws[0] != 0:
            print(Fore.RED + 'Unknown command!')
    cmd()

cmd()

db.db.close()
db.connection.close()
