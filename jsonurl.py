import urllib.parse


def decode_str(data):
    url_decoded_string = urllib.parse.unquote(data)
    return url_decoded_string


def decode_dict(d):
    if isinstance(d, dict):
        return {urllib.parse.unquote(k): decode_dict(v) for k, v in d.items()}
    elif isinstance(d, str):
        pairs = dict(urllib.parse.parse_qsl(d))
        if "&" in pairs and "=" in pairs:
            return {k: urllib.parse.unquote(v) for k, v in pairs.items()}
        else:
            return pairs
    elif isinstance(d, list):
        return [decode_dict(v) for v in d]
    else:
        return d


def encode(data):
    return urllib.parse.quote(data)
