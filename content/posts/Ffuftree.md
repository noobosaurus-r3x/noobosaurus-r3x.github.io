+++
author = "Noobosaurus R3x"
title = "ffutree"
date = "2023-06-25 11:56"
description = "Tree view of ffuf output"
type = [
    "posts"
]
categories = [
    "tools"
]
tags = [
    "tools",
    "python"
]
+++


# ffuftree : a Directory Tree Builder for ffuf Output

This is a Python script that builds a directory tree from the JSON output of the ffuf tool. It parses the JSON data, extracts URLs, and their corresponding HTTP status codes, and then prints the directory tree along with the status codes using colored output.
---
## Requirements

- Python 3.x
- colorama
---
## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/noobosaurus-r3x/ffuftree
cd ffuftree
```


2. Install the required dependencies:
```bash
pip install colorama
```


---
## Usage

To use the directory tree builder, you need to provide the path to the JSON file containing the ffuf output. The script will read the file, parse the JSON data, and then print the directory tree with corresponding status codes.

Run the script using the following command:

```bash
python ffuftree.py /path/to/ffuf_output.json
```


Replace `/path/to/ffuf_output.json` with the actual path to your ffuf output JSON file.
---
## Output

The directory tree will be printed in the console, showing the hierarchical structure of directories and files, along with their HTTP status codes. The status codes will be colorized to make it easier to identify different status ranges:

- Successful (2xx) responses will be displayed in green.
- Redirects (3xx) will be displayed in yellow.
- Client errors (4xx) will be displayed in red.
- Server errors (5xx) will be displayed in blue.
---
## Example

Suppose your `ffuf_output.json` contains the following data:

```json
{
  "results": [
    {
      "url": "https://example.com/files/document.txt",
      "status": "200",
      "host": "example.com"
    },
    {
      "url": "https://example.com/files/image.jpg",
      "status": "404",
      "host": "example.com"
    },
    {
      "url": "https://example.com/files/music.mp3",
      "status": "200",
      "host": "example.com"
    }
  ]
}
```

Running the script with this JSON file:
```bash
python ffuftree.py ffuf_output.json
```
will output the following:
```bash
└── example.com
    ├── files
       ├── document.txt (Status: 200)
       ├── image.jpg (Status: 404)
       └── music.mp3 (Status: 200)
```
---
## Ffuf
https://github.com/ffuf/ffuf

## Final words
I am not a proper developper, so you might encounter some problems with some outputs. That is mainly an exercice, but it works pretty well here.
---
If you want to check the file [ffuftree.py](../../static/files/ffuftree.py):
```python
import argparse
import json
from collections import defaultdict
import logging
from colorama import init, Fore

init(autoreset=True)  # Initialize colorama to work with Windows, macOS, and Linux terminals

class DirectoryTreeBuilder:
    def __init__(self):
        self.directory_tree = defaultdict(dict)

    def build_directory_tree(self, ffuf_output):
        try:
            data = json.loads(ffuf_output)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data.") from e

        if not isinstance(data, dict) or "results" not in data:
            raise ValueError("Invalid ffuf output format.")

        for result in data["results"]:
            url = result.get("url", "")
            host = result.get("host", "")
            if not url.startswith("https://"):
                continue

            parts = url.split("/")[3:]  # Skip "https:", "", and the host
            self._add_path_to_tree(host, parts, result)

    def _add_path_to_tree(self, host, parts, result):
        current_level = self.directory_tree[host]
        for i, part in enumerate(parts):
            if i == len(parts) - 1:  # Last part (file or directory)
                status = result.get("status", "")
                color = self._get_status_color(status)
                current_level[part] = {"_status": f"{color}{status}"}
            else:
                current_level = current_level.setdefault(part, {})

    def _get_status_color(self, status):
        status_code = int(status)
        if 200 <= status_code < 300:
            return Fore.GREEN
        elif 300 <= status_code < 400:
            return Fore.YELLOW
        elif 400 <= status_code < 500:
            return Fore.RED
        elif 500 <= status_code < 600:
            return Fore.BLUE
        else:
            return Fore.RESET

    def print_directory_tree(self, tree=None, indent=0, last_item=False):
        if tree is None:
            tree = self.directory_tree

        keys = sorted(tree.keys())
        for i, key in enumerate(keys):
            last_item_flag = i == len(keys) - 1
            symbol = "└── " if last_item_flag and last_item else "├── "
            current_path = f"{symbol}{key}"

            if isinstance(tree[key], dict) and "_status" in tree[key]:
                status = tree[key]["_status"]
                current_path += f" (Status: {status})"
                tree[key].pop("_status")  # Remove the "_status" key from the output

            logging.info("    " * indent + current_path)

            if isinstance(tree[key], dict):
                next_indent = indent + 1
                last_item_child = last_item_flag and not bool(tree[keys[i]])
                self.print_directory_tree(tree[key], next_indent, last_item_child)

def read_ffuf_output(json_file):
    try:
        with open(json_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{json_file}' not found.")

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(message)s")

def main():
    parser = argparse.ArgumentParser(description="Build and print a directory tree from ffuf output.")
    parser.add_argument("json_file", type=str, help="Path to the JSON file containing ffuf output.")
    args = parser.parse_args()

    try:
        ffuf_output = read_ffuf_output(args.json_file)

        tree_builder = DirectoryTreeBuilder()
        tree_builder.build_directory_tree(ffuf_output)
        tree_builder.print_directory_tree()
    except ValueError as e:
        logging.error(str(e))

if __name__ == "__main__":
    setup_logging()
    main()
```
---