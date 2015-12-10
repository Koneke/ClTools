import sys, lambdatools

def createShortcut(shortcut, target):
	global switches;

	if '-f' in switches:
		return '\n'.join([
			'@echo off',
			'cd /D {TARGET}'
				.replace('{TARGET}', target)
		]);
		

	return '\n'.join([
		'@echo off',
		'if "%home%"=="" (cd /D %homedrive%%homepath%\{TARGET}) else (cd /D %home%\{TARGET})'
			.replace('{TARGET}', target)
			.replace('\\;', '')
	]);

if __name__ == "__main__":
	global switches;
	lambdatools.setup();
	args = list(sys.argv[1:]);
	switches = args.where(lambda a: a[0] == '-');
	args = args.where(lambda a: a not in switches);

	if len(args) > 1:
		with open('shortcuts\\' + args[0] + '.bat', 'w') as f:
			f.write(createShortcut(args[0], args[1]));
