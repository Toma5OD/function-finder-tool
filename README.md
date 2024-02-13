# Function Finder Tool

## Overview

The Function Finder Tool is a Python script designed to extract function names from Go files. It scans a specified Go source file for function declarations and logs each found function name to the console and a text file. This tool is particularly useful for developers looking to quickly identify and navigate through the functions defined in large Go files.

## Features

- Scans Go files for function declarations.
- Excludes anonymous functions (e.g., those declared with `defer func()`).
- Logs found function names to the console.
- Saves found function names to a text file (`function_names.txt`).

## Requirements

- Python 3.x

## Usage

1. Ensure Python 3.x is installed on your system.
2. Place `function-finder-tool.py` in your desired directory.
3. Open a terminal and navigate to the directory containing `function-finder-tool.py`.
4. Run the script using Python:

``` python3 function-finder-tool.py ```


5. When prompted, enter the full path to the Go file you wish to scan for function names.

## Example

``` Enter the path to the file: /path/to/your/file.go ```


The script will then process the specified Go file and output the names of all functions found, both to the console and to `function_names.txt` within the same directory as the script.

