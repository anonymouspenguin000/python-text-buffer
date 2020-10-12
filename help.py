from colorama import *

help = {
    'all': Fore.CYAN + 'export [var, path]' + Fore.WHITE + ' exports the text from a variable to a file\n'
         + Fore.CYAN + 'get [--var]' + Fore.WHITE + ' shows the value of a variable or a list of variables\n'
         + Fore.CYAN + 'set [var, val]' + Fore.WHITE + ' sets an item to local storage\n'
         + Fore.CYAN + 'del [var]' + Fore.WHITE + ' deletes an item from local storage\n'
         + Fore.CYAN + 'export-end [var, path]' + Fore.WHITE + ' exports the text from variable to the END of file\n'
         + Fore.CYAN + 'import [var, path]' + Fore.WHITE + ' imports the text from the file to the local storage\n'
         + Fore.CYAN + 'exit' + Fore.WHITE + ' exit program\n'
         + Fore.CYAN + 'help [--comm]' + Fore.WHITE + ' shows help for command/command list\n',

    'export': Fore.CYAN + 'export [var, path]' + Fore.WHITE + ' exports the text from a variable to a file\nVAR - Storage item name which contains text value.\nPATH - Path to text file to write text. If not exist - it will create new.\n' + Fore.YELLOW + 'WARNING: Old text will be DELETED!',
    'get': Fore.CYAN + 'get [--var]' + Fore.WHITE + ' shows the value of a variable or a list of variables\nVAR (NOT required) - Storage item name which contains text value. If not - variable list.',
    'set': Fore.CYAN + 'set [var, val]' + Fore.WHITE + ' sets an item to local storage\nVAR - Storage item name which contains text value.\nVAL - text value to set.\n' + Fore.YELLOW + 'WARNING: Old text will be DELETED!',
    'del': Fore.CYAN + 'del [var]' + Fore.WHITE + ' deletes an item from local storage\nVAR - Storage item name which contains text value.\n' + Fore.YELLOW + 'WARNING: Think one, two, three before delete!',
    'export-end': Fore.CYAN + 'export-end [var, path]' + Fore.WHITE + ' exports the text from variable to the END of file\nVAR - Storage item name which contains text value.\nPATH - Path to text file to write text. If not exist - it will create new.',
    'import': Fore.CYAN + 'import [var, path]' + Fore.WHITE + ' imports the text from the file to the local storage\nVAR - Storage item name which contains text value.\nPATH - Path to text file to get text. If not exist - error.',
    'exit': Fore.CYAN + ' exit' + Fore.WHITE + ' exit program.',
    'help': Fore.CYAN + ' help [--comm]' + Fore.WHITE + ' shows help for command/command list.\nCOMM (NOT required) - command name to get help. If not - command list.'
}
