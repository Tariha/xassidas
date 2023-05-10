from pathlib import Path
from models import Author
from dataclasses import asdict
import argparse
import json


def parse_author_data(file):
    author_data = {
        "name": file.stem,
        "tariha": file.parent.stem,
        "xassidas": [],
        "infos": [],
    }
    for info in file.glob("*.md"):
        print("Adding author info")
        info_data = info.read_text()
        author_data["infos"].append({"lang": "fr", "text": info_data})

    for xassida in file.glob("*/*.json"):
        print("Adding %s => %s" % (file.stem, xassida.stem))
        xassida_data = json.loads(xassida.read_text())
        author_data["xassidas"].append(xassida_data)

    out_file = file / "xassidas.json"
    out_file.write_text(json.dumps(asdict(Author(**author_data)), ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tariha", help="The tariha of the authors")
    parser.add_argument("-a", "--author", help="The author of the xassida")
    args = parser.parse_args()
    glob_path = f"{args.tariha}/" if args.tariha else "*/"
    glob_path += f"{args.author}/" if args.author else "*/"
    # start parsing
    for file in Path("xassidas").glob(glob_path):
        parse_author_data(file)
