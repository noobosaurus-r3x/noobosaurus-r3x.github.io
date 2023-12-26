+++
author = "Noobosaurus R3x"
title = "Crawwwler"
date = "2023-06-09"
description = "Simple Web Crawler"
type = [
    "posts"
]
categories = [
    "tools"
]
tags = [
    "tools",
    "articles"
]
+++

# Web Crawler Bash Script

This script is a simple web crawler written in Bash. It takes a URL as an argument, downloads the HTML of the page, extracts all the links, and checks the HTTP status code for each link. It then prints the URL and its HTTP status code, with URLs returning a 200 status code highlighted in green and all others in red.
---
```bash
#!/bin/bash

usage() {
  echo "Usage: $0 -u URL"
  exit 1
}

while getopts u: flag
do
  case "${flag}" in
    u) url=${OPTARG};;
    *) usage;;
  esac
done

if [ -z "$url" ]; then
  usage
fi

IMAGE="
 +-+-+-+-+-+-+-+-+-+-+-+-+
 |c|r|a|w|w|w|l|e|r|.|s|h|
 +-+-+-+-+-+-+-+-+-+-+-+-+
"

echo "$IMAGE"

response=$(curl -sL --fail "$url")
if [ $? -ne 0 ]; then
  echo "Error: failed to download HTML page"
  exit 1
fi

links=$(echo "$response" | grep -oP '(?<=<a href=")[^"]*')

check_status() {
  local url=$1

  local code=$(curl -sL -o /dev/null -w "%{http_code}" "$url")

  if [ $code -eq 200 ]; then
    printf "%-100s \e[32m%s\e[0m\n" "${url:0:100}" "$code"
  else
    printf "%-100s \e[31m%s\e[0m\n" "${url:0:100}" "$code"
  fi
}

for link in $links; do
  if [[ $link =~ ^http[s]?:// ]]; then
    absolute_url=$link
  else
    absolute_url=$(echo "$url" | awk -F/ '{OFS="/"; NF--; print $0}')"/$link"
  fi

  check_status "$absolute_url"
done | tee "results_$(echo $url | sed 's/[^A-Za-z0-9_.-]/_/g').txt"

echo "--------------------------------------------------"
echo "You can find the results here: $(readlink -f "results_$(echo $url | sed 's/[^A-Za-z0-9_.-]/_/g').txt")"
echo "--------------------------------------------------"
```



### Usage :

```./crawler.sh -u URL```

Replace URL with the website you want to crawl.

The results are saved in a text file named results_<URL>.txt, where <URL> is the URL argument with special characters replaced by underscores.
---
### Example :

```./crawler.sh -u https://noobosaurusr3x.fr```

This will download the HTML from https://noobosaurusr3x.fr, extract all the links, check their HTTP status codes, and save the results in a file named results_https_noobosaurusr3x_fr.txt.
---