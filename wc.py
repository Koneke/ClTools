import kinput;

class wc:
	def __init__(self):
		self.k = kinput.kinput();

	def run(self):
		print(len(self.k.stdin));

if __name__ == '__main__':
	wc().run();
