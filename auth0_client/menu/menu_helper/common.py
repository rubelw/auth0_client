from os.path import expanduser
import re
import operator
from io import StringIO
import math
import os
import sys

if sys.version_info[0] < 3:
    import ConfigParser as configparser
else:
    import configparser


DEBUG = 0


def yes_or_no(title):

    menu = {1:['Yes',True],2:['No',False]}


    print("\n")
    print('#' * len(title))
    print(str(title))
    print ('#'*len(title))
    for key in sorted(menu):
        print(str(key) + ":" + menu[key][0])

    pattern = r'^[0-9]+$'
    while True:
        ans = raw_input("Make A Choice: [ENTER]")
        if re.match(pattern, ans) is not None:
            if int(ans) in menu:
                answer = menu[int(ans)][1]
                break

    return answer


def multiple_choice(title, list):
    counter = 1
    menu = {}

    for l in list:
        menu[counter]=str(l)
        counter+=1

    print("\n")
    print('#########################################')
    print('## '+str(title)+' ##')
    print('#########################################')
    for key in sorted(menu):
        print(str(key) + ":" + menu[key])


    pattern = r'^[0-9]+$'
    while True:
        ans = raw_input("Make A Choice: [ENTER]")
        if re.match(pattern, ans) is not None:
            if int(ans) in menu:
                answer = menu[int(ans)]
                break

    return answer




def indent(rows, hasHeader=False, headerChar='-', delim=' | ', justify='left',
           separateRows=False, prefix='', postfix='', wrapfunc=lambda x:x):
    """Indents a table by column.
       - rows: A sequence of sequences of items, one sequence per row.
       - hasHeader: True if the first row consists of the columns' names.
       - headerChar: Character to be used for the row separator line
         (if hasHeader==True or separateRows==True).
       - delim: The column delimiter.
       - justify: Determines how are data justified in their column.
         Valid values are 'left','right' and 'center'.
       - separateRows: True if rows are to be separated by a line
         of 'headerChar's.
       - prefix: A string prepended to each printed row.
       - postfix: A string appended to each printed row.
       - wrapfunc: A function f(text) for wrapping text; each element in
         the table is first wrapped by this function."""
    # closure for breaking logical rows to physical, using wrapfunc
    def rowWrapper(row):
        newRows = [wrapfunc(item).split('\n') for item in row]
        return [[substr or '' for substr in item] for item in map(None,*newRows)]


    # break each logical row into one or more physical ones
    logicalRows = [rowWrapper(row) for row in rows]
    # columns of physical rows
    columns = map(None,*reduce(operator.add,logicalRows))
    # get the maximum of each column by the string length of its items
    maxWidths = [max([len(str(item)) for item in column]) for column in columns]
    rowSeparator = headerChar * (len(prefix) + len(postfix) + sum(maxWidths) + \
                                 len(delim)*(len(maxWidths)-1))
    # select the appropriate justify method
    justify = {'center':str.center, 'right':str.rjust, 'left':str.ljust}[justify.lower()]


    output=StringIO()
    if separateRows: print >> output, rowSeparator
    for physicalRows in logicalRows:
        for row in physicalRows:
            print >> output, \
                prefix \
                + delim.join([justify(str(item),width) for (item,width) in zip(row,maxWidths)]) \
                + postfix
        if separateRows or hasHeader: print >> output, rowSeparator; hasHeader=False
    return output.getvalue()

# written by Mike Brown
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/148061
def wrap_onspace(text, width):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).
    """

    if type(text) is str:
        return reduce(lambda line, word, width=width: '%s%s%s' %
                  (line,
                   ' \n'[(len(line[line.rfind('\n')+1:])
                         + len(word.split('\n',1)[0]
                              ) >= width)],
                   word),
                  text.split(' ')
                 )
    elif type(text) is list:
        new_text = ''
        counter = 0
        for e in text:
            counter += 1
            new_text += '('+str(counter)+') '+str(e)+"\n"
        #new_text = ''.join(str(e) for e in text)
        return reduce(lambda line, word, width=width: '%s%s%s' %
                  (line,
                   ' \n'[(len(line[line.rfind('\n')+1:])
                         + len(word.split('\n',1)[0]
                              ) >= width)],
                   word),
                  new_text.split(' ')
                 )



def wrap_onspace_strict(text, width):
    """Similar to wrap_onspace, but enforces the width constraint:
       words longer than width are split."""
    wordRegex = re.compile(r'\S{'+str(width)+r',}')

    if type(text) is str:

        return wrap_onspace(wordRegex.sub(lambda m: wrap_always(m.group(),width),text),width)
    elif type(text) is list:
        new_text = ''
        counter = 0
        for e in text:
            counter += 1
            new_text += '('+str(counter)+') '+str(e)+"\n"
        #new_text = ''.join(str(e) for e in text)
        return wrap_onspace(wordRegex.sub(lambda m: wrap_always(m.group(),width),new_text),width)



def wrap_always(text, width):
    """A simple word-wrap function that wraps text on exactly width characters.
       It doesn't split the text in words."""

    if type(text) is str:
        return '\n'.join([ text[width*i:width*(i+1)] for i in xrange(int(math.ceil(1.*len(text)/width))) ])
    elif type(text) is list:

        new_text = ''
        counter = 0
        for e in text:
            counter += 1
            new_text += '('+str(counter)+') '+str(e)+"\n"
        #new_text = ''.join(str(e) for e in text)
        return '\n'.join([ new_text[width*i:width*(i+1)] for i in xrange(int(math.ceil(1.*len(new_text)/width))) ])


def select_path(title, search_path):

    DIRS = []
    for child in os.listdir(search_path):
        path = os.path.join(search_path, child)
        if os.path.isdir(path):
            DIRS.append(path)

    MENU = {}
    UNSORTED_MENU = {}

    COUNTER = 0

    for d in DIRS:
        list = []

        list.append(d)

        matchObj = re.match(r'.*[!/]([a-zA-Z0-9-_]+)$', d, re.M | re.I)

        if matchObj:
            list.append(matchObj.group(1))
            UNSORTED_MENU[matchObj.group(1)] = list

    for key in sorted(UNSORTED_MENU):
        COUNTER += 1

        MENU[COUNTER] = UNSORTED_MENU[key]

    print("\n")
    print("####################################")
    print('## '+str(title)+' ##')
    print("####################################")

    for key in sorted(MENU):
        print(str(key) + ": " + MENU[key][1])

    while True:

        USER_RESPONSE = raw_input("Make a selection [ENTER] (Cntrl-C to exit):")
        if int(USER_RESPONSE) in MENU:
            directory = MENU[int(USER_RESPONSE)][0]
            break

    return directory

def read_ini_file_to_dictionary(filename):

    parser = configparser.ConfigParser()
    parser.optionxform = str
    parser.read(filename)
    confdict = {section: dict(parser.items(section)) for section in parser.sections()}

    return confdict

