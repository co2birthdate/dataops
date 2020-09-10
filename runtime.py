
'''
touch file for github-action logging
'''

import time
from pathlib import Path
import os

def main():

	runtime = time.strftime("%Y%m%d-%H%M%S")
	Path('logs'+os.sep+runtime+'.txt').touch()

if __name__ == "__main__":
	main()
