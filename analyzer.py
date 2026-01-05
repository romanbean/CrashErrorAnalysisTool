# imports
import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

@dataclass
class ErrorInfo:
	error_type: str
	message: str
	line_number: Optional[int]

# ---- Core parsing logic ----
def extract_error_info(text: str) -> str:
	"""
	Extract the most relevant error or exception line from a text file.
	Prioritizes Python traceback exceptions.
	"""
	lines = text.splitlines()

	# Regex for Python exception lines like:
	# ValueError: message
	# ZeroDivisionError: division by zero
	# et cetera
	exception_pattern = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*Error|Exception):\s*(.*)")

	last_exception = None

	for line in lines:
		match = exception_pattern.match(line.strip())
		if match:
			last_exception = match

	if last_exception:
		error_type, message = last_exception.groups()
		return ErrorInfo(error_type, message, None)

	# Fallback: generic error detection
	for line in reversed(lines):
		lower = line.lower()
		if "error" in lower or "exception" in lower:
			return ErrorInfo("Unknown", line.strip(), None)

	return ErrorInfo("Unknown", "No error found", None)

# ---- File handling ----
def analyze_file(filepath: Path) -> str:
	"""
	Read a file and analyze it for errors.
	"""
	try:
		content = filepath.read_text()
	except OSError as e:
		return f"Failed to read file: {filepath}\n{e}"

	error_type = extract_error_type(content)
	return (
		"Detected error:\n"
		f"Type		: {error.error_type}\n"
		f"Message	: {error.message}\n"
		f"Line		: {error.line_number}"
	)

# ---- CLI entrypoint ----
def main():
	parser = argparse.ArgumentParser(description="Analyze a file for error messages.")
	parser.add_argument("file", type=Path, help="Path to the error file")

	args = parser.parse_args()
	result = analyze_file(args.file)
	print(result)


if __name__ == "__main__":
	main()
