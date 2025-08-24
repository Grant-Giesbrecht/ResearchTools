import json
import matplotlib.pyplot as plt
import argparse
import mplcursors

parser = argparse.ArgumentParser()
parser.add_argument('filename')
# parser.add_argument('-f', '--fft', help='show fft of data', action='store_true')
# parser.add_argument('--trimdc', help='Removes DC from FFT data', action='store_true')
# parser.add_argument('--f1', help='Plot F1 file over FFT', action='store_true')
# parser.add_argument('-z', '--zerocross', help='Zero-crossing analysis', action='store_true')
# parser.add_argument('--zcmin', help='Zero-crossing analysis plot, minimum Y value', type=float)
# parser.add_argument('--zcmax', help='Zero-crossing analysis plot, maximum Y value', type=float)
args = parser.parse_args()

def plot_xy_from_json(filename):
	"""
	Reads a JSON file containing named lists (and possibly strings).
	Finds pairs of lists where names differ only by 'x' vs 'y'
	and plots them as X vs Y.
	"""
	# Load JSON file
	with open(filename, 'r') as f:
		data = json.load(f)
	
	# Keep only list entries
	lists_only = {k: v for k, v in data.items() if isinstance(v, list)}
	
	# Iterate over keys and find matching x/y pairs
	visited = set()
	for name in lists_only.keys():
		if name in visited:
			continue
		
		# Look for x <-> y substitution
		if 'x' in name:
			name_y = name.replace('x', 'y')
			if name_y in lists_only:
				x_vals = lists_only[name]
				y_vals = lists_only[name_y]
				if len(x_vals) == len(y_vals):  # sanity check
					plt.figure()
					plt.plot(x_vals, y_vals, marker='o')
					plt.xlabel(name)
					plt.ylabel(name_y)
					plt.title(f"{name} vs {name_y}")
					plt.grid(True)
				visited.update([name, name_y])
		
		elif 'y' in name:
			name_x = name.replace('y', 'x')
			if name_x in lists_only:
				# already handled in 'x' branch
				continue
	
	plt.show()


import json
import matplotlib.pyplot as plt

def plot_xy_from_json2(filename):
	"""
	Reads a JSON file containing named lists (and possibly strings).
	Finds pairs of lists where names differ only by 'x' vs 'y'
	(anywhere in the name, case-insensitive) and plots them as X vs Y.
	"""
	# Load JSON file
	with open(filename, 'r') as f:
		data = json.load(f)
	
	# Keep only list entries
	lists_only = {k: v for k, v in data.items() if isinstance(v, list)}
	
	visited = set()
	for name in lists_only.keys():
		if name in visited:
			continue
		
		# Handle lowercase x → y
		if "x" in name:
			candidate = name.replace("x", "y")
			if candidate in lists_only:
				x_vals = lists_only[name]
				y_vals = lists_only[candidate]
				if len(x_vals) == len(y_vals):
					plt.figure()
					plt.plot(x_vals, y_vals, marker='o')
					plt.xlabel(name)
					plt.ylabel(candidate)
					plt.title(f"{name} vs {candidate}")
					plt.grid(True)
				visited.update([name, candidate])
		
		# Handle uppercase X → Y
		if "X" in name:
			candidate = name.replace("X", "Y")
			if candidate in lists_only:
				x_vals = lists_only[name]
				y_vals = lists_only[candidate]
				if len(x_vals) == len(y_vals):
					plt.figure()
					plt.plot(x_vals, y_vals, marker='o')
					plt.xlabel(name)
					plt.ylabel(candidate)
					plt.title(f"{name} vs {candidate}")
					plt.grid(True)
				visited.update([name, candidate])
	
	plt.show()

if __name__ == "__main__":
	
	plot_xy_from_json(args.filename)