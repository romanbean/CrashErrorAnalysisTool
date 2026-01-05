# Crash & Error Analysis Tool

A lightweight Python CLI tool for analyzing program crash output and extracting meaningful error information from logs and Python tracebacks

---

## Overview

This tool reads error output (such as stderr or log files) and identifies the most relevant failure, including Python exceptions and chained tracebacks. It is designed to support debugging workflows by surfacing clear, structured error data.

---

## Features

- Parses runtime error logs and stderr output
- Detects Python exceptions from real tracebacks
- Handles chained exceptions correctly
- Extracts structured error information (type and message)
- Includes unit and integration tests using pytest

---

## Usage

Analyze an error log file:

---

## Example

Input:
ZeroDivisionError: division by zero

Output:
Detected error:
Type    : ZeroDivisionError
Message : division by zero
Line    : None

---

## Project Structure

analyzer.py        # Core parsing logic and CLI
test_analyzer.py   # Unit and integration tests
crash.py           # Sample crashing program used for testing

---

## Motivation

This project was built to practice writing production-style Python tools, with a focus on error handling, parsing, and automated testing. It serves as a small but realistic example of how debugging utilities are designed and tested.

---

## Future Improvements

- Extract line numbers from tracebacks

- Support JSON output

- Analyze multiple files or directories

- Extend parsing for non-Python logs

## Requirements

Python 3.10+

pytest (for testing)
