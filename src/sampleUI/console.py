import os

clear = lambda: os.system('cls')

class Console:

    @staticmethod
    def Clear():
        clear()

    @staticmethod
    def Title(title = "", description = "", separatorChar = "*", showLowerSeparator = True):
        s = separatorChar
        nTitle = len(title)
        nDesc = len(description)
        if(nTitle>nDesc):
            n = nTitle
        else:
            n = nDesc
        messageSeparator = ''.join([char*n for char in s])
        
        titleDescription = title
        if description != "": titleDescription += f"\n\n {description}"
        if(showLowerSeparator):
            print(f"""\n{messageSeparator}\n{titleDescription}\n{messageSeparator}\n""")
        else:
            print(f"""\n{messageSeparator}\n{titleDescription}\n""")
        