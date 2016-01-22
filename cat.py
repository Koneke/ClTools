import sys, lambdatools, os

def show(fpath, longest):
	global switches;
	f = open(fpath);

	if '-n' in switches:
		print('\n=============== ' + fpath + ' ===============');

	if '-f' in switches:

		[print(fpath.rjust(longest, ' ') + ": " + line.rstrip('\n')) for line in f];
	else:
		[print(line.rstrip('\n')) for line in f];

if __name__ == "__main__":
	global switches;
	lambdatools.setup();

	args = sys.argv[1:];

	switches = args.where(lambda a: a[0] == '-');
	args = args.where(lambda a: a not in switches);

	if not sys.stdin.isatty():
		for line in sys.stdin:
			args.append(line.rstrip());

	args = args.where(lambda a: os.path.isfile(a));
	longest = len(max(args, key=len));

	if len(args) > 0:
		[show(arg, longest) for arg in args];
	else:
		print('USAGE: cat <filename(s)>')
