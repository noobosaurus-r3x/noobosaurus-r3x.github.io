+++
author = "Noobosaurus R3x"
title = "Wordlister"
date = "2023-06-29"
description = "wordlist generator"
type = [
    "posts"
]
categories = [
    "tools"
]
tags = [
    "tool",
    "articles"
]
+++
---


This script generates a wordlist from one or more text files by extracting and sorting unique words.

---
## Usage

1. Copy and paste that small bash script and name it wordlister.sh
```bash
#!/bin/bash

# Check if text files were provided as arguments
if [ $# -eq 0 ]; then
    echo "Usage: $0 <text_file1> [<text_file2> ...]"
    exit 1
fi

# Create a wordlist file
wordlist="wordlist.txt"

# Concatenate the contents of all text files
combined_text=$(cat "$@")

# Extract the words from the combined text
words=$(echo "$combined_text" | tr -c '[:alnum:]' '\n' | tr '[:upper:]' '[:lower:]')

# Remove duplicates and sort the words
sorted_words=$(echo "$words" | sort -u)

# Write the words to the wordlist file
echo "$sorted_words" > "$wordlist"

# Count the number of words in the wordlist file
word_count=$(wc -l < "$wordlist")

echo "Created wordlist with $word_count words"
```

2. Make the script executable:
```
 chmod +x wordlister.sh
```
 ---
Run the script, providing the text files you want to process as arguments:

```
./wordlister.sh file1.txt file2.txt file3.txt

```

You can specify as many text files as you want, separated by spaces.

The script will concatenate the contents of all the provided text files, extract the words, remove duplicates, sort them, and save the resulting wordlist in a file called wordlist.txt in the same directory. It will display a message indicating the number of words in the wordlist.

