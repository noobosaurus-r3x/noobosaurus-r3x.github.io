+++
author = "Noobosaurus R3x"
title = "RedFlagger"
date = "2023-06-05"
description = "zip2john automation"
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

# RedFlagger

RedFlagger is a bash script designed to download and aggregate reports from 'https://dl.red.flag.domains/daily/' based on user-specified conditions.

It is inspired by NewRedflag, a python script written by lil-doudou.

https://github.com/lil-doudou/NewRedflag

## Usage

```./redflagger.sh [--latest|--days num] [--all] [--output filename]```



### Options

- `--latest` or `-l`: Downloads the report from 1 day ago.
- `--days num` or `-d num`: Downloads the report from 'num' days ago.
- `--all` or `-a`: Downloads all available reports.
- `--output filename` or `-o filename`: Specifies the output file to store the downloaded reports. Defaults to 'output.txt' if no filename is provided.

### Examples

Download all the reports available since 3 days ago, saving them to 'my_file.txt':

```./redflagger.sh -d 3 -a -o my_file.txt```

Download all available reports, saving them to 'my_file.txt':

```./redflagger.sh -a -o my_file.txt```

Download the reports from 3 days ago, saving them to 'my_file.txt':

```./redflagger.sh -d 3 -o my_file.txt```


The script :
```bash
#!/bin/bash

# Usage: ./redflagger.sh --latest|--days [num] --all [--output [filename]]
# Example: ./reflagger.sh -d 3 -a -o my_file.txt #This will download the report from 3 days ago and all available reports, saving them to my_file.txt
# Example2:./redflagger.sh -a -o my_file.txt #This will download all available reports, saving them to my_file.txt



output_file="output.txt"  # Default output file
while getopts ":lad:o:" opt; do
  case ${opt} in
    l ) # process option latest
      date=$(date -d "1 day ago" +%Y-%m-%d)
      ;;
    a ) # process option all
      all=true
      ;;
    d ) # process option days
      date=$(date -d "$OPTARG day ago" +%Y-%m-%d)
      ;;
    o ) # process option output
      output_file=$OPTARG
      ;;
    \? ) echo "Usage: ./script.sh [-l] [-a] [-d num] [-o filename]"
      exit 1
      ;;
  esac
done

shift $((OPTIND -1))

if [[ -z "$date" && -z "$all" ]]; then
    echo "Usage: ./script.sh [-l] [-a] [-d num] [-o filename]"
    exit 1
fi

main_url=$(curl -s 'https://dl.red.flag.domains/daily/')
if [[ $? -ne 0 ]]; then
    echo "Failed to fetch the main page. Please check your internet connection."
    exit 1
fi

links=$(echo "$main_url" | grep -oP '(?<=href=")[^"]*')

declare -A downloaded_links

for link in $links; do
    if [[ $link =~ ^[0-9]{4} ]]; then
        if [[ $link == *"$date"* || "$all" == "true" ]]; then
            
            if [[ ${downloaded_links[$link]} == "true" ]]; then
                continue
            fi

            echo "Downloading: $link"
            if ! curl -s "https://dl.red.flag.domains/daily/$link" >> "$output_file" 2>/dev/null ;
            then
                echo "Failed to download $link. Continuing with the next one."
                continue
            fi
            
            downloaded_links[$link]="true"
        fi
    fi
done

sort "$output_file" -o "$output_file"
```