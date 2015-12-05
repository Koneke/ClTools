import sys, os, shutil;

options = {};
optionIndices = {};

optionKeysCopyCut = [];

optionKeysPaste = ['path'];
optionIndices['path'] = 0;

switches = [];

def readMode(line):
    return line.split(' ')[0];

def readNonMode(line):
    return ''.join(line.split(' ')[1:]).split(',');

def readName(line):
    return readNonMode(line)[0];

def readPath(line):
    return readNonMode(line)[1].rstrip('\n') if line != '' else '';

def getName(path):
    return getFullPath(path).split('\\')[-1];

def getFullPath(path):
    return os.getcwd() + '\\' + path;

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
                if readPath(line) == getFullPath(path):
                    return True;
    return False;

def append(mode, path):
    global switches;

    if not os.path.exists(path):
        raise Exception('No such file: ' + path);
    
    #with open(path) as f:
    if '-d' in switches:
        print('name: ' + getName(path));
        print('path: ' + getFullPath(path));
        print('');

    if alreadyExists(path) == False:
        return ''.join([mode, ' ', getName(path), ',', getFullPath(path)]);
 
if('copycat-clipboard' in os.environ):
    clipboardpath = os.environ['copycat-clipboard'] + os.environ['homepath'];
else:
    clipboardpath = os.environ['homedrive'] + os.environ['homepath'];
    clipboardpath += '\\.copycat-clipboard';

try:
    # Setup mode.
    mode = sys.argv[1].lower();

    shorthands = {};
    shorthands['p'] = 'paste';
    shorthands['c'] = 'copy';
    shorthands['x'] = 'cut';

    if mode in shorthands:
        mode = shorthands[mode];

    # Clone arguments.
    args = [arg for arg in sys.argv[2:]];

    # Setup switches
    for arg in args:
        if arg[0] == '-':
            switches.append(arg);

    # Clean args
    args = list(filter(lambda x: x not in switches, args));

    # Setup options.
    keysToRead = optionKeysPaste if mode == 'paste' else optionKeysCopyCut;
    for key in keysToRead:
        if len(args) > optionIndices[key]:
            options[key] = args[optionIndices[key]];

    # Mode + potential others.
    optionCount = len(list(filter(lambda x: x != None, options)));

    if '-d' in switches:
        print('clipboardpath: ' + clipboardpath);
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

                if 'path' in options:
                    destination = ''.join([os.getcwd(), '\\', options['path'], '\\', readName(line)]);
                else:
                    destination = ''.join([os.getcwd(), '\\', readName(line)]);

                copyCutMode = readMode(line);

                if '-d' in switches:
                    print('source: ' + source);
                    print('destination: ' + destination);

                    if 'path' in options:
                        print('target path: ' + options['path']);

                if os.path.isfile(source):
                    shutil.copy2(source, destination);
                    if copyCutMode == 'cut':
                        os.remove(source);
                else:
                    shutil.copytree(source, destination);
                    if copyCutMode == 'cut':
                        shutil.rmtree(source);
    else:
        raise Exception('Unknown mode: ' + mode + '.');
#except Exception as e:
except ValueError as e:
    print('error: ' + str(e) + '');
    print('usage: copycat (copy|c|cut|x [file1, file2 ... fileN])|paste|p [-d]');
