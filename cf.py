import sys, os, shutil;

options = {};
optionIndices = {};

optionKeysCopyCut = [];

optionKeysPaste = ['path'];
optionIndices['path'] = 2;

switches = [];

def readMode(line):
    return line.split(' ')[0];

def readNonMode(line):
    return ''.join(line.split(' ')[1:]).split(',');

def readName(line):
    return readNonMode(line)[0];

def readPath(line):
    return readNonMode(line)[1].rstrip('\n') if line != '' else '';

def getName(f):
    return getPath(f).split('\\')[-1];
    #return f.name;

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
    global switches;

    if not os.path.exists(path):
        raise Exception('No such file: ' + path);
    
    with open(path) as f:
        if '-d' in switches:
            print('name: ' + getName(f));
            print('path: ' + getPath(f));
            print('');

        if alreadyExists(f) == False:
            return ''.join([mode, ' ', getName(f), ',', getPath(f)]);
 
if('copycat-clipboard' in os.environ):
    clipboardpath = os.environ['copycat-clipboard'] + os.environ['homepath'];
else:
    clipboardpath = os.environ['homedrive'] + os.environ['homepath'];
    clipboardpath += '\\bin\\copycat-clipboard';

try:
    # Setup mode.
    mode = sys.argv[1].lower();

    shorthands = {};
    shorthands['p'] = 'paste';
    shorthands['c'] = 'copy';
    shorthands['x'] = 'cut';

    if mode in shorthands:
        mode = shorthands[mode];

    # Setup options.
    for key in optionKeysPaste if mode == 'paste' else optionKeysCopyCut:
        if len(sys.argv) > optionIndices[key]:
            options[key] = sys.argv[optionIndices[key]];
        else:
            options[key] = None;

    # Mode + potential others.
    optionCount = len(list(filter(lambda x: x != None, options)));

    # Clone arguments.
    args = [arg for arg in sys.argv[2 + optionCount:]];

    # Setup args
    for arg in args:
        if arg[0] == '-':
            switches.append(arg);

    args = list(filter(lambda x: x not in switches, args));

    if '-d' in switches:
        print('cwd: ' + os.getcwd());
        print('optionCount: ' + str(optionCount));
        print('options: ' + str(options));
        print('switches: ' + str(switches));
        print('args: ' + str(args));
        print('');

    if mode in ['copy', 'cut']:
        # If we're not pasting, we need atleast one file supplied.
        if not len(sys.argv) > optionCount + 1:
            raise Exception('Copy/Cut requires atleast one file specified.');

        # Clear our clipboard. Optionally, we could just not do this?
        # But at the moment I want to emulate an ordinary OS clipboard,
        # i.e. hitting copy/cut replaces the current contents.
        # Having it actually append to it would be a possible
        # way of doing things too though.
        open(clipboardpath, 'w').close();

        out = '\n'.join([append(mode, arg) for arg in args]);

        with open(clipboardpath, 'a') as clipboard:
            clipboard.write(out);
            if '-d' in switches:
                print('resulting clipboard:\n' + out);

    elif mode in ['paste']:
        with open(clipboardpath, 'r') as clipboard:
            for line in clipboard:
                source = readPath(line);

                if not options['path']:
                    destination = ''.join([os.getcwd(), '\\', readName(line)]);
                else:
                    destination = ''.join([os.getcwd(), '\\', options['path'], '\\', readName(line)]);

                copyCutMode = readMode(line);

                if '-d' in switches:
                    print('source: ' + source);
                    print('destination: ' + destination);
                    print('target path: ' + options['path']);

                shutil.copyfile(source, destination);

                if copyCutMode == 'cut':
                    os.remove(source);
    else:
        raise Exception('Unknown mode: ' + mode + '.');
except Exception as e:
    print('error: ' + str(e) + '');
    print('usage: copycat (copy|c|cut|x [file1, file2 ... fileN])|paste|p [-d]');
