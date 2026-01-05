import subprocess
from analyzer import extract_error_info

def test_analyzer_with_real_crash():
	result = subprocess.run(
		["python3", "crash.py"],
		capture_output=True,
		text=True
	)

	error_output = result.stderr
	error = extract_error_info(error_output)

	assert error.error_type != "Unknown"
	assert error.error_type.endswith("Error")

def test_returns_unknown_for_clean_input():
	# Testing a file or text with no errors
	error = extract_error_info("all good\nno issues here")

	assert error.error_type == "Unknown"
	assert error.message == "No error found"

def test_handles_chained_exceptions():
	text = """
Traceback (most recent call last):
	File "a.py", line 1, in <module>
		int("x")
ValueError: invalid literal for int()

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
	File "b.py", line 2, in <module>
		raise RuntimeError("failed")
RuntimeError: failed
"""

	error = extract_error_info(text)

	assert error.error_type == "RuntimeError"
	assert error.message == "failed"
