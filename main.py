import json
import os

from jsonurl import decode_fully, decode_partially, encode

e_dir = "encoded"
d_dir = "decoded"
e_files = os.listdir(e_dir)
d_files = os.listdir(d_dir)

for file in e_files:
    with open(f"{e_dir}/{file}", "r") as f:
        data = f.read()

        if data.startswith("{") and ":" in data:
            data_dict = json.loads(data)
            data = decode_partially(data_dict)
        else:
            data = decode_fully(data)

        if isinstance(data, dict):
            data = json.dumps(data, indent=4)

        ext = "json" if data.startswith("{") and data.endswith("}") else "txt"
        fn = os.path.splitext(file)[0]

        with open(f"{d_dir}/{fn}.{ext}", "w") as f:
            f.write(data)

for file in d_files:
    with open(f"{d_dir}/{file}", "r") as f:
        data = f.read()
        curl_encoded = encode(data)
        fn = os.path.splitext(file)[0]
        with open(f"{e_dir}/{fn}.txt", "w") as f:
            f.write(curl_encoded)
