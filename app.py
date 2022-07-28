import os
import random
from flask import Flask, send_from_directory, abort

bana_bd = "./Bana-BinhDinh/audio_by_word"
bana_kt = "./Bana-KonTum/audio_by_word"
bana_gl = "./Bana-GiaLai/audio_by_word"

app = Flask(__name__)

@app.route('/<region_tag>/<word>', methods=['GET'])
def download(region_tag, word):
    dir = ""
    fn = ""

    if region_tag == "BD":
        dir = os.path.join(bana_bd, word)

    elif region_tag == "KT":
        dir = os.path.join(bana_kt, word)

    elif region_tag == "GL":
        dir = os.path.join(bana_gl, word)
    else:
        return abort(404)

    dir = dir.strip()
    list_files = os.listdir(dir)
    fn = random.choice(list_files)

    return send_from_directory(directory=dir, path=fn)