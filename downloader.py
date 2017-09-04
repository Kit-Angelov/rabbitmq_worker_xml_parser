# -----------------------By Kit_Angel-------------------------
# ------------------https://t.me/Kit_Angel--------------------
import requests
import os
from worker_parser_xml import config


def download_file(body, path_dir):
    local_filename = body.split('/')[-1]
    url = config.host + body
    path_download = os.path.join(path_dir, local_filename)
    r = requests.get(url, stream=True)
    with open(path_download, 'wb') as f:
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
    return path_download

