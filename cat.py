import sys, lambdatools, os

def show(fpath, fname, longest):
	global switches;
	f = open(fpath);

	# banner
	if '-b' in switches:
		print('\n=============== ' + fpath + ' ===============');

	lefthand = "";
	# file(path)
	if '-f' in switches:
		lefthand = fpath.rjust(longest, ' ');
	# name
	if '-n' in switches:
		lefthand = fname.rjust(longest, ' ');

	digits = 0;
	if '-l' in switches:
		# Not cheap, but makes for nicer output.
		# (and I don't think the performance will be an issue really.)
		digits = len(str(sum(1 for line in open(fpath))));
		lefthand = lefthand + " {l#}";

	if lefthand != "":
		lefthand = lefthand + ": ";

	linenumber = 1;
	for line in f:
		if '-l' in switches:
			print(lefthand.replace("{l#}", str(linenumber).rjust(digits, ' ')) + line.rstrip('\n'));
		else:
			print(lefthand + line.rstrip('\n'));
		linenumber = linenumber + 1;

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

	b = [arg[cwdlen:] for arg in args];
	argfnames = dict(zip(args, b));

	longest = len(max([(v if '-n' in switches else k) for k,v in argfnames.items()], key=len));

	if len(args) > 0:
		[show(arg, fname, longest) for arg, fname in argfnames.items()];
	else:
		print('USAGE: cat <filename(s)>')
