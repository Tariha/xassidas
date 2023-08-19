import argparse
import json
from pathlib import Path


def parse_traduction(file):
    """Parse the translation for each arab verse"""
    xassida = file.parents[1]
    lang = file.parents[0].stem
    arab_file = xassida / file.name

    arab_data = json.loads(arab_file.read_text())
    # verify if this translation already exist
    if lang in arab_data["translated_lang"]:
        return

    print("Parsing the %s version of %s" % (lang, file.stem))
    traduction_data = json.loads(file.read_text())
    for i, chapter in traduction_data["chapters"].items():
        name = {"lang": lang, "translation": chapter["name"], "transcription": ""}
        arab_data["chapters"][i]["translated_names"].append(name)
        for j, verse in enumerate(traduction_data["chapters"][i]["verses"]):
            data = {"lang": lang, "text": verse["text"], "author": ""}
            arab_data["chapters"][i]["verses"][j]["translations"].append(data)

    arab_data["translated_lang"].append(lang)
    arab_file.write_text(json.dumps(arab_data, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tariha", help="The tariha of the authors")
    parser.add_argument("-a", "--author", help="The author of the xassida")
    parser.add_argument("-x", "--xassida", help="The xassida")
    args = parser.parse_args()
    glob_path = f"{args.tariha}/" if args.tariha else "*/"
    glob_path += f"{args.author}/" if args.author else "*/"
    glob_path += f"{args.xassida}/**/*.json" if args.xassida else "**/*.json"
    # start parsing translations
    for file in Path("xassidas").glob(glob_path):
        if len(file.parent.stem) == 2:
            parse_traduction(file)
