import json
import matplotlib.pyplot as plt
import argparse
import mplcursors
from ganymede import dict_summary
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-v', '--verbose', help="Verbosity. Options=0, 1, 2. Default=1.", type=int, default=1)
args = parser.parse_args()



if __name__ == "__main__":
	
	with open(args.filename) as fh:
		json_data = json.load(fh)
	
	if not json_data:
		print(f"Failed to read file {args.filename}!")
		sys.exit()
	
	dict_summary(json_data, verbose=args.verbose)