# -*- coding: utf-8 -*-
import platform

if platform.system() == 'Windows':
    import colorama
    colorama.init()
else:
    pass

class Log:
    UseColor = True ## before changing to true, run "pip install colorama" in commandline

    ColorCodes = {
        'black':    '0;30', 'bright gray':  '0;37',
        'blue':     '0;34', 'white':        '1;37',
        'green':    '0;32', 'bright blue':  '1;34',
        'cyan':     '0;36', 'bright green': '1;32',
        'red':      '0;31', 'bright cyan':  '1;36',
        'purple':   '0;35', 'bright red':   '1;31',
        'yellow':   '0;33', 'bright purple':'1;35',
        'dark gray':'1;30', 'bright yellow':'1;33',
        'normal':   '0'
    }

    @classmethod
    def printcc(cls, color, text):
        """Print in color."""
        if cls.UseColor == True:
            print "\033[" + cls.ColorCodes[color] + "m" + text + "\033[0m",
        else:
            print text,

    # @classmethod
    # def printcc(cls, color, details):
    #     default_colors = cons.get_text_attr()
    #     default_bg = default_colors & 0x0070

    #     cons.set_text_attr(cons.FOREGROUND_RED | default_bg | cons.FOREGROUND_INTENSITY)
    #     print details
    #     cons.set_text_attr(default_colors)

    @classmethod
    def Warning(cls, message):
        details = "%s\n" % message
        print details
        #cls.printcc('yellow', details)

    @classmethod
    def Failed(cls, message, actual="--", expect="--"):
        details = message

        if actual != "--" and expect != "--":
            details = "%s\nactual: '%s'\nexpect: '%s'\n" % (message, actual, expect)

        #cls.printcc('red', details)
        print details
        raise "(Failed)"

    # def writec(text, color):
    #     """Write to stdout in color."""
    #     if usecolor == True:
    #         sys.stdout.write("\033[" + codeCodes[color] + "m" + text + "\033[0m")
    #     else:
    #         sys.stdout.write(text)

    # def switchColor(color):
    #     """Switch console color."""
    #     sys.stdout.write("\033[" + codeCodes[color] + "m")
