import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt
import skrf
import graf.widgets as gw

parser = argparse.ArgumentParser(description="Plot the characteristic impedance (Z0) extracted from a touchstone file.")
parser.add_argument('filename', help="Touchstone file (.s2p, or .snp; ports 1 and 2 are used).")
parser.add_argument('--zref', help="Assumed port reference impedance in ohms. Default=50.", type=float, default=50.0)
parser.add_argument('-f', '--fixaxes', help="Fix y-axis limits to 0-100 Ohms for real, and -50-50 for imaginary.", action="store_true")
parser.add_argument('-s', '--sparam', help="Add a third axes plotting S11 and S21 in dB magnitude.", action="store_true")
parser.add_argument('-g','--richshow', help="Use Graf rich-show.", action="store_true")
args = parser.parse_args()


def extract_z0(s11, s21, zref):
	"""Characteristic impedance of a symmetric reciprocal 2-port from its S-parameters.
	
	Z0 = Zref * sqrt(((1+S11)^2 - S21^2) / ((1-S11)^2 - S21^2))
	
	The sign of the root is chosen so that Re(Z0) >= 0.
	"""
	z0 = zref * np.sqrt(((1 + s11)**2 - s21**2) / ((1 - s11)**2 - s21**2))
	return np.where(z0.real < 0, -z0, z0)


if __name__ == "__main__":
	
	try:
		with open(args.filename, "r") as f:
			ntwk = skrf.Network.from_string(f.read())
	except Exception as e:
		print(f"Failed to read file {args.filename}: {e}")
		sys.exit(1)
	
	if ntwk.nports < 2:
		print(f"File {args.filename} has {ntwk.nports} port(s); need at least 2.")
		sys.exit(1)
	
	# --zref overrides the port reference impedance assumed for the S-parameters
	# (the file's own header value is ignored).
	
	freq = ntwk.f
	z0 = extract_z0(ntwk.s[:, 0, 0], ntwk.s[:, 1, 0], args.zref)
	
	ncols = 3 if args.sparam else 2
	fig, axes = plt.subplots(1, ncols, sharex=True)
	ax1, ax2 = axes[0], axes[1]
	ax1.plot(freq/1e9, z0.real)
	ax1.set_ylabel("Re(Z0) (Ohms)")
	fig.suptitle(f"Z0 of {args.filename} (Zref = {args.zref:g} Ohms)")
	ax1.grid(True)
	ax2.plot(freq/1e9, z0.imag)
	ax2.set_ylabel("Im(Z0) (Ohms)")
	ax2.set_xlabel("Frequency (GHz)")
	ax2.grid(True)
	
	if args.sparam:
		ax3 = axes[2]
		with np.errstate(divide="ignore"):
			ax3.plot(freq/1e9, 20*np.log10(np.abs(ntwk.s[:, 0, 0])), label="S11")
			ax3.plot(freq/1e9, 20*np.log10(np.abs(ntwk.s[:, 1, 0])), label="S21")
		ax3.set_ylabel("Magnitude (dB)")
		ax3.set_xlabel("Frequency (GHz)")
		ax3.grid(True)
		ax3.legend()

	if args.fixaxes:
		ax1.set_ylim([0, 100])
		ax1.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
		ax2.set_ylim([-50, 50])
		ax2.set_yticks([-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50])
	
	plt.tight_layout()
	
	
	if args.richshow:
		gw.rich_show()
	else:
		plt.show()
