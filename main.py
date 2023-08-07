import json
import os

from jsonurl import (
    decode_dict,
    decode_str,
    encode,
    get_encoded_chars,
    is_valid_json,
    encode_dict,
    get_encoded_chars_from_dict,
)

e_dir = "encoded"
d_dir = "decoded"
os.makedirs(e_dir, exist_ok=True)
os.makedirs(d_dir, exist_ok=True)
e_files = os.listdir(e_dir)
d_files = os.listdir(d_dir)


def read_file(path):
    with open(path, "r") as file:
        return file.read()


def write_file(path, content):
    with open(path, "w") as file:
        file.write(content)


def decode_files():
    for file in e_files:
        data = read_file(os.path.join(e_dir, file))

        if is_valid_json(data):
            data_dict = json.loads(data)
            data = decode_dict(data_dict)
            data = json.dumps(data, indent=4)
        else:
            data = decode_str(data)

        ext = "json" if is_valid_json(data) else "txt"
        fn = os.path.splitext(file)[0]
        print(fn, ext)
        write_file(os.path.join(d_dir, f"{fn}.{ext}"), data)


def encode_files():
    for file in d_files:
        data = read_file(os.path.join(d_dir, file))
        fn = os.path.splitext(file)[0]
        e_file = os.path.join(e_dir, f"{fn}.txt")
        encoded_data = read_file(e_file)
        if is_valid_json(data) and is_valid_json(encoded_data):
            encoded_data = json.loads(encoded_data)
            safe = get_encoded_chars_from_dict(encoded_data)
            print(fn, f"Z{safe}Z")
            data = json.loads(data)
            data = encode_dict(data, safe)
        else:
            safe = get_encoded_chars(encoded_data)
            data = encode(data, safe)
            data = json.dumps(data, indent=4)

        write_file(e_file, data)


# Uncomment the function you want to run
decode_files()
# encode_files()
