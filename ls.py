import sys, lambdatools, dirtools, kinput, os, time, datetime, re;

class ls:
	def __init__(self):
		self.k = kinput.kinput();
		self.filt = None;

	def show(self, path):
		k = self.k;

		if self.filt:
			if not re.search(self.filt, path):
				return;

		if '-d' in k.switches:
			if os.path.isfile(path):
				return;

		if '-f' in k.switches:
			if not os.path.isfile(path):
				return;

		out = ""
		if not '-b' in k.switches:
			modifiedTime = str(datetime.datetime.fromtimestamp(os.path.getmtime(path)));
			modifiedTime = modifiedTime[:-7]; # strip milliseconds
			out += modifiedTime + '\t';

		out += path;
		print(out);

	def run(self):
		k = self.k;
		targetFolder = None;

		if len(k.args) > 0:
			if os.path.exists(k.args[0]):
				if not os.path.isfile(k.args[0]):
					targetFolder = k.args[0];

					if len(k.args) > 1:
						self.filt = k.args[1];
			else:
				self.filt = k.args[0];

		result = None;
		if targetFolder:
			result = os.listdir(dirtools.getFullPath(targetFolder));
		else:
			result = os.listdir(os.getcwd());

		for path in result:
			self.show(path);

if __name__ == '__main__':
	cmd = ls();
	cmd.run();
