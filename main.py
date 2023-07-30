import json
import os

from jsonurl import curl_to_json, decode_dict, json_to_url_encoded

encoded_dir = "encoded"
decoded_dir = "decoded"
encoded_files = os.listdir(encoded_dir)
decoded_files = os.listdir(decoded_dir)


encoded_str = "query=&hitsPerPage=1000&maxValuesPerFacet=2000&page=0&getRankingInfo=true&tagFilters=&facetFilters=%5B%5B%22departmentAliases%3A${urlencode_param(loops.department)}%22%5D%5D"
decoded = curl_to_json(encoded_str)
print(decoded)

# for file in encoded_files:
#     with open(f"{encoded_dir}/{file}", "r") as f:
#         curl_cmd = f.read()
#         if "{" in curl_cmd:
#             curl_map = json.loads(curl_cmd)
#             data = decode_dict(curl_map)
#         else:
#             data = curl_to_json(curl_cmd)
#         if isinstance(data, dict):
#             data = json.dumps(data, indent=4, ensure_ascii=True)
#         fn = os.path.splitext(file)[0]
#         with open(f"{decoded_dir}/{fn}.json", "w") as f:
#             f.write(data)

# for file in decoded_files:
#     with open(f"{decoded_dir}/{file}", "r") as f:
#         curl_cmd = f.read()
#         curl_encoded = json_to_url_encoded(curl_cmd)
#         fn = os.path.splitext(file)[0]
#         with open(f"{encoded_dir}/x-{fn}.txt", "w") as f:
#             f.write(curl_encoded)
