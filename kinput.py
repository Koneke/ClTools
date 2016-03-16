import sys, lambdatools;

class kinput:
	def __init__(self, stdinToArgs = True):
		lambdatools.setup();

		self.stdin = [];
		self.args = sys.argv[1:];
		self.switches = self.args.where(lambda a: a[0] == '-');
		self.args = self.args.where(lambda a: a not in self.switches);

		if not sys.stdin.isatty():
			for line in sys.stdin:
				if stdinToArgs:
					self.args.append(line.rstrip());
				self.stdin.append(line.rstrip());
