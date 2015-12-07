import sys, lambdatools;

class kinput:
	def __init__(self):
		lambdatools.setup();

		self.args = sys.argv[1:];
		self.switches = self.args.where(lambda a: a[0] == '-');
		self.args = self.args.where(lambda a: a not in self.switches);

		if not sys.stdin.isatty():
			for line in sys.stdin:
				self.args.append(line.rstrip());
