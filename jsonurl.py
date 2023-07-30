import json
import urllib.parse


def curl_to_json(curl_data):
    if not ("&" in curl_data and "=" in curl_data):
        unquoted = urllib.parse.unquote(curl_data)
        return unquoted
    curl_data_strip = curl_data.strip("&")
    pairs = curl_data_strip.split("&")

    json_data = {}

    for pair in pairs:
        key, value = pair.split("=", 1)
        decoded_key = urllib.parse.unquote(key)
        decoded_value = urllib.parse.unquote(value)
        try:
            decoded_key = json.loads(decoded_key)
        except json.JSONDecodeError:
            pass
        try:
            decoded_value = json.loads(decoded_value)
        except json.JSONDecodeError:
            pass

        json_data[decoded_key] = decoded_value
    return json_data


def decode_dict(d):
    if isinstance(d, dict):
        return {urllib.parse.unquote(k): decode_dict(v) for k, v in d.items()}
    elif isinstance(d, str):
        dc = dict(urllib.parse.parse_qsl(d))
        if "&" in dc and "=" in dc:
            return {k: urllib.parse.unquote(v) for k, v in dc.items()}
        else:
            return dc
    elif isinstance(d, list):
        return [decode_dict(v) for v in d]
    else:
        return d


def json_to_url_encoded(json_string):
    url_encoded_string = urllib.parse.quote(json_string)
    return url_encoded_string
