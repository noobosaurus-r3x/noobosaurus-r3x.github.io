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
