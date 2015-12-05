import sys

if len(sys.argv) > 1:
    [[print(line.rstrip('\n')) for line in open(arg)] for arg in sys.argv[1:]]
else:
    print('USAGE: cat <filename(s)>')
