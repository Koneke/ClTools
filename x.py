import kinput;
from subprocess import call;

class x:
	def __init__(self):
		self.k = kinput.kinput(False);

		if not '$' in self.k.args:
			self.k.args.append('$');

	def run(self):
		for f in self.k.stdin:
			args = self.k.args[:];
			args = [f if x == '$' else x for x in args];
			call(args, shell = True);
			#call(' '.join(self.k.args + [f]), shell = True);

if __name__ == '__main__':
	x().run();
