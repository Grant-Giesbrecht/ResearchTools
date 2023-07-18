import pyperclip
from colorama import Fore, Style
import logging
import getopt, sys

#TODO: Could automatically change title
#TODO: Could remove when percent signs and other special characters are done incorrectly
#TODO: Could remove abstract

TEST_MODE = False
LOG_LEVEL = logging.INFO
replacement_indentation = "\t"

#-----------------------------------------------------------
# Parse arguments
argv = sys.argv[1:]

try:
	opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "debug", "info", "warning", "error", "critical", "test"])
except getopt.GetoptError as err:
	print("--help for help")
	sys.exit(2)
for opt, aarg in opts:
	if opt in ("-h", "--help"):
		print(f"{Fore.RED}Just kidding I haven't made any help text yet. ~~OOPS~~{Style.RESET_ALL}")
		sys.exit()
	elif opt == "--debug":
		LOG_LEVEL = logging.DEBUG
	elif opt == "--info":
		LOG_LEVEL = logging.INFO
	elif opt == "--test":
		TEST_MODE = True
	else:
		assert False, "unhandled option"
	# ...
#-----------------------------------------------------------


tabchar = "    "
prime_color = Fore.YELLOW
standard_color = Fore.WHITE
quiet_color = Fore.LIGHTBLACK_EX
cspecial = Fore.GREEN # COlor used to highlight content inside logging messages
logging.basicConfig(format=f'{prime_color}%(levelname)s:{standard_color} %(message)s{quiet_color} | %(asctime)s{Style.RESET_ALL}', level=LOG_LEVEL)

def find_nth(haystack, needle, n):
	""" https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string """
	start = haystack.find(needle)
	while start >= 0 and n > 1:
		start = haystack.find(needle, start+len(needle))
		n -= 1
	return start

text = pyperclip.paste()

print("Original Text:")
print(f"{Fore.RED}{text}{Style.RESET_ALL}")

#Strip invisibles
text = text.strip(" \t\n\r")

# Put last curly brace on new line
if text[-2:] == '}}':
	logging.info("Moving last curly brace to new line")
	text = text[:-1] + '\n'+ text[-1:]
else:
	logging.info("Final curly brace did not need to be moved.")

# Change \r\n used by IEEE export to \n{replacement_indentation}
n = 1
running = True
replacement = f"\n{replacement_indentation}"
while running:
	
	# Find occurance, break if not found
	
	idx = find_nth(text, "\r\n  ", 1)
	if idx == -1:
		running = False
		continue
	
	# Replace text
	text = text[:idx] + replacement + text[idx+4:]
	n += 1

if n > 1:
	logging.info(f"Replaced {n-1} non-standard characters.")

print("\nFormatted Text:")
print(f"{Fore.LIGHTBLUE_EX}{text}{Style.RESET_ALL}")

print("\nFormatted Text: (with hidden characters)")
print(f"{Fore.LIGHTBLACK_EX}{repr(text)}{Style.RESET_ALL}")

if not TEST_MODE:
	pyperclip.copy(text)