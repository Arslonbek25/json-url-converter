import json
import string
import urllib.parse


def get_encoded_chars(url):
    return "".join(
        list(dict.fromkeys([char for char in url if char in string.punctuation]))
    ).replace("%", "")


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
        # pairs = dict(urllib.parse.parse_qsl(d))
        # print(pairs)
        # if "&" in pairs and "=" in pairs:
        #     return {k: urllib.parse.unquote(v) for k, v in pairs.items()}
        # else:
        return urllib.parse.unquote(d)
    elif isinstance(d, list):
        return [decode_dict(v) for v in d]
    else:
        return d


def encode(data, safe):
    return urllib.parse.quote(data, safe=safe + " \n")


if __name__ == "__main__":
    t = encode(
        "https://www.google.com/search?q=python+url+encoding&oq=python+url+encoding&aqs=chrome..69i57j0l7.2873j0j7&sourceid=chrome&ie=UTF-8",
        safe="",
    )

    print(t)
