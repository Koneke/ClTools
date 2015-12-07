from forbiddenfruit import curse, reverse

def where(self, fn):
	return list(filter(fn, self));

def exists(self, fn):
	return len(self.where(fn)) > 0;

def negate(fn):
	return lambda x: not fn(x);

hasSetup = False;

def setup():
	global hasSetup;

	if not hasSetup:
		curse(list, 'where', where);
		curse(list, 'exists', exists);
		hasSetup = True;
