import sys

def createShortcut(shortcut, target):
	return '\n'.join([
		'@echo off',
		'if "%home%"=="" (cd /D %homedrive%%homepath%\{TARGET}) else (cd /D %home%\{TARGET})'
			.replace('{TARGET}', target)
			.replace('\\;', '')
	]);

if __name__ == "__main__":
	if len(sys.argv) > 2:
		with open('shortcuts\\' + sys.argv[1] + '.bat', 'w') as f:
			f.write(createShortcut(sys.argv[1], sys.argv[2]));
