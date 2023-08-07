import json
import os

from jsonurl import decode_dict, decode_str, encode, get_encoded_chars, is_valid_json

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
            # print(file)
            data = decode_dict(data_dict)
            # print(data)
        else:
            data = decode_str(data)

        if isinstance(data, dict):
            data = json.dumps(data, indent=4)

        ext = "json" if is_valid_json(data) else "txt"
        fn = os.path.splitext(file)[0]
        print(fn, ext)
        write_file(os.path.join(d_dir, f"{fn}.{ext}"), data)


def encode_files():
    for file in d_files:
        data = read_file(os.path.join(d_dir, file))
        fn = os.path.splitext(file)[0]
        e_file = os.path.join(e_dir, f"{fn}.txt")
        decoded_data = read_file(e_file)
        safe = get_encoded_chars(decoded_data)
        print(fn, f"Z{safe}Z")
        data = encode(data, safe)
        
        write_file(e_file, data)


# Uncomment the function you want to run
# decode_files()
encode_files()

# with open("encoded/curl4.txt", "r") as file:
#     data = file.read()
#     print(get_encoded_chars(data))
