import sys, os

def readMode(line):
    return line.split(' ')[0];

def readNonMode(line):
    return ''.join(line.split(' ')[1:]).split(',');

def readName(line):
    return readNonMode(line)[0];

def readPath(line):
    return readNonMode(line)[1].rstrip('\n') if line != '' else '';

def getName(f):
    return f.name;

def getPath(f):
    return os.path.abspath(f.name);

def deleteLine(targetLine):
    global clipboardpath;
    with open(clipboardpath) as clipboard:
        lines = clipboard.readlines();

        clipboard.seek(0);
        for line in lines:
            if line != targetLine:
                clipboard.write(line);
        clipboard.truncate();

def alreadyExists(f):
    global clipboardpath;
    if not os.path.exists(clipboardpath):
        return False;

    with open(clipboardpath, 'r') as clipboard:
        for line in clipboard:
            if line != '':
                if readPath(line) == getPath(f):
                    return True;
    return False;

def append(mode, path):
    # Switch
    if path[0] == '-':
        pass;
    else:
        if not os.path.exists(path):
            raise Exception('No such file: ' + path);
        
        f = open(path);
        if alreadyExists(f) == False:
            #out += ''.join([mode, ' ', getName(f), ',', getPath(f), '\n']);
            #return ''.join([mode, ' ', getName(f), ',', getPath(f), '\n']);
            return ''.join([mode, ' ', getName(f), ',', getPath(f)]);
 
if('copycat-clipboard' in os.environ):
    clipboardpath = os.environ['copycat-clipboard'] + os.environ['homepath'];
else:
    clipboardpath = os.environ['homedrive'] + os.environ['homepath'];
    clipboardpath += '\\bin\\copycat-clipboard';

# Setup options
optionslength = 1;
optionMode = 1;

try:
    # All options + one file minimum.
    if len(sys.argv) > optionslength:
        mode = sys.argv[optionMode].lower();

        shorthands = {};
        shorthands['p'] = 'paste';
        shorthands['c'] = 'copy';
        shorthands['x'] = 'cut';

        if mode in shorthands:
            mode = shorthands[mode];

        if mode != 'paste':
            # If we're not pasting, we need atleast one file supplied.
            if not len(sys.argv) > optionslength + 1:
                raise Exception('Copy/Cut requires atleast one file specified.');

            # Clear our clipboard. Optionally, we could just not do this?
            # But at the moment I want to emulate an ordinary OS clipboard,
            # i.e. hitting copy/cut replaces the current contents.
            # Having it actually append to it would be a possible
            # way of doing things too though.
            open(clipboardpath, 'w').close();

            out = '\n'.join([append(mode, arg) for arg in sys.argv[(optionslength + 1):]]);

            with open(clipboardpath, 'a') as clipboard:
                #clipboard.write(out);
                print(out);
        else:
            # Not yet implemented.
            raise Exception('Paste not yet supported.');
except Exception as e:
    print('error: ' + str(e) + '');
    print('usage: copycat (copy|cut [file1, file2 ... fileN])|paste');
