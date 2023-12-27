+++
author = "Noobosaurus R3x"
title = "Flask of Cookies"
date = "2023-06-29 23:58"
description = "Encode and decode Flask session cookies"
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

# Flask Of Cookies - Encode/Decode Flask Cookies

Flask Of Cookies is a Python script that allows you to encode and decode Flask session cookies. It provides a command-line interface for encoding and decoding session cookies with or without a secret key.
inspired by the `flask-session-cookie-manager` project by Wilson Sumanang and Alexandre ZANNI. 

## Features

- Encode a Flask session cookie using a secret key and session cookie structure.
- Decode a Flask session cookie with or without a secret key.

## Usage

To use Flask Of Cookies, follow these steps:

1. Copy/paste the script or download the [`FOC.py`](../../static/files/FOC.py) file.
```python
#!/usr/bin/env python3
"""Flask Of Cookies - Encode/Decode Flask Cookies"""
"""Author: Noobosaurus R3x - Inspired by flask-session-cookie-manager by Wilson Sumanang, Alexandre ZANNI"""

import argparse
import base64
import ast
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import SecureCookieSessionInterface


class MockApp:
    def __init__(self, secret_key):
        self.secret_key = secret_key


def add_padding(cookie_value):
    """Add padding to the base64-encoded cookie value"""
    missing_padding = len(cookie_value) % 4
    if missing_padding != 0:
        cookie_value += "=" * (4 - missing_padding)
    return cookie_value


def encode(secret_key, session_cookie_structure):
    """Encode a Flask session cookie"""
    try:
        app = MockApp(secret_key)
        session_cookie_structure = ast.literal_eval(session_cookie_structure)
        si = SecureCookieSessionInterface()
        s = URLSafeTimedSerializer(app.secret_key, si.salt, si.serializer)
        return s.dumps(session_cookie_structure)
    except ValueError as e:
        return f"[Encoding error] Input isn't a valid Python dictionary: {str(e)}"
    except Exception as e:
        return f"[Encoding error] {str(e)}"


def decode(session_cookie_value, secret_key=None):
    """Decode a Flask cookie"""
    try:
        if secret_key is None:
            payload = session_cookie_value

            if payload.startswith('.'):
                payload = payload[1:]

            data = payload.split(".")[0]
            data = add_padding(data)
            data = base64.urlsafe_b64decode(data)

            return data.decode('utf-8')
        else:
            app = MockApp(secret_key)
            si = SecureCookieSessionInterface()
            s = URLSafeTimedSerializer(app.secret_key, si.salt, si.serializer)
            return s.loads(session_cookie_value)
    except ValueError as e:
        return f"[Decoding error] Input isn't a valid Flask session cookie: {str(e)}"
    except Exception as e:
        return f"[Decoding error] {str(e)}"


def main():
    parser = argparse.ArgumentParser(
        description='Flask Cookie Decoder/Encoder',
        epilog="Inspired by 'Flask Session Cookie Decoder/Encoder' by Wilson Sumanang, Alexandre ZANNI"
    )
    subparsers = parser.add_subparsers(help='sub-command help', dest='subcommand')

    parser_encode = subparsers.add_parser('encode', help='encode')
    parser_encode.add_argument('-s', '--secret-key', metavar='<string>',
                               help='Secret key', required=True)
    parser_encode.add_argument('-t', '--cookie-structure', metavar='<string>',
                               help='Session cookie structure', required=True)

    parser_decode = subparsers.add_parser('decode', help='decode')
    parser_decode.add_argument('-s', '--secret-key', metavar='<string>',
                               help='Secret key', required=False)
    parser_decode.add_argument('-c', '--cookie-value', metavar='<string>',
                               help='Session cookie value', required=True)

    args = parser.parse_args()

    if args.subcommand == 'encode':
        print(encode(args.secret_key, args.cookie_structure))
    elif args.subcommand == 'decode':
        print(decode(args.cookie_value, args.secret_key))


if __name__ == "__main__":
    main()
```

2. Ensure you have Python3 installed on your system.
3. Install the required dependencies by running the following command:
`pip install flask itsdangerous`
4. Open a terminal or command prompt and navigate to the directory where `FOC.py` is located.
5. Run the script with the desired subcommand:

- To display the help message and available options, use the `-h` option:
```
python3 FOC.py -h
```

- To encode a Flask session cookie, use the `encode` subcommand:
```
python3 FOC.py encode -s <secret_key> -t <cookie_structure>
```
- Replace `<secret_key>` with your Flask secret key.
- Replace `<cookie_structure>` with the session cookie structure as a valid Python dictionary string. for example : '{"number":"326410031505","username":"admin"}'


- To decode a Flask session cookie with the secret key, use the `decode` subcommand:
```
python3 FOC.py decode -s <secret_key> -c <cookie_value>
```
- Replace `<secret_key>` with your Flask secret key.
- Replace `<cookie_value>` with the session cookie value to decode.

- To decode a Flask session cookie without the secret key, use the `decode` subcommand:
```
python3 FOC.py decode -c <cookie_value>
```
- Replace `<cookie_value>` with the session cookie value to decode.

6. The encoded or decoded result will be printed in the terminal.
---
## Acknowledgements

Flask Of Cookies was inspired by the `flask-session-cookie-manager` project by Wilson Sumanang and Alexandre ZANNI.
https://github.com/noraj/flask-session-cookie-manager


---