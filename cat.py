import sys, lambdatools, os

def show(fpath, fname, longest):
	global switches;
	f = open(fpath);

	# banner
	if '-b' in switches:
		print('\n=============== ' + fpath + ' ===============');

	# file(path)
	if '-f' in switches:
		[print(fpath.rjust(longest, ' ') + ": " + line.rstrip('\n')) for line in f];
	# name
	if '-n' in switches:
		[print(fname.rjust(longest, ' ') + ": " + line.rstrip('\n')) for line in f];
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

	cwdlen = len(os.getcwd().replace("\\\\", "/")) + 1 if '-n' in switches else 0; 

	#b = list(arg[cwdlen:] for arg in args);
	b = [arg[cwdlen:] for arg in args];
	argfnames = dict(zip(args, b));

	longest = len(max([(v if '-n' in switches else k) for k,v in argfnames.items()], key=len));

	if len(args) > 0:
		#[show(arg, longest) for arg in args];
		[show(arg, fname, longest) for arg, fname in argfnames.items()];
	else:
		print('USAGE: cat <filename(s)>')
