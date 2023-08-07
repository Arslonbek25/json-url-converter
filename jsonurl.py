import json
import string
import urllib.parse


def get_encoded_chars(url):
    return "".join(
        list(dict.fromkeys([char for char in url if char in string.punctuation]))
    ).replace("%", "")


def get_encoded_chars_from_dict(data):
    stack = list(data.values())
    encoded_values = ""
    while stack:
        value = stack.pop()
        if isinstance(value, dict):
            stack.extend(value.values())
        elif isinstance(value, list):
            stack.extend(value)
        elif isinstance(value, str):
            encoded_values += value
    return get_encoded_chars(encoded_values)


def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False


def decode_str(data):
    return urllib.parse.unquote(data)


def decode_dict(d):
    if isinstance(d, dict):
        return {urllib.parse.unquote(k): decode_dict(v) for k, v in d.items()}
    elif isinstance(d, str):
        return urllib.parse.unquote(d)
    elif isinstance(d, list):
        return [decode_dict(v) for v in d]
    else:
        return d


def encode(data, safe):
    return urllib.parse.quote(data, safe=safe + "\n")


def encode_dict(d, safe):
    if isinstance(d, dict):
        return {k: encode_dict(v, safe) for k, v in d.items()}
    elif isinstance(d, list):
        return [encode_dict(v, safe) for v in d]
    elif isinstance(d, str):
        return encode(d, safe)
    else:
        return d
