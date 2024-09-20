import argparse
import json
from dataclasses import asdict
from pathlib import Path
from models import Chapter, Verse, Xassida
from arab_transliterator.transliterator import ArabTransliterator

transliterator = ArabTransliterator()


def parse_file(file, depth):
    """
    Parse a single xassida file or xassida translation folder
    depth == 0 means that it's the arabic text
    else it's a translation text
    """
    # parse the chapter verses and words
    verses = parse_chapter(file, depth, file.stem)
    return Chapter("", int(file.stem), verses)


def parse_chapter(file, lang, number):
    """Retrieve the lines"""
    lang = False if depth == 0 else True
    try:
        lines = file.read_bytes().decode("utf-8-sig").split("\n")
    except Exception:
        lines = file.read_bytes().decode("ISO-8859-1").split("\n")

    lines = [line + " " for line in lines]
    verses = filter(len, "".join(lines).split("##"))
    verses_data = map(lambda v: parse_verse(
        *v, number, lang), enumerate(verses))
    return list(verses_data)


def parse_verse(i, verse, chap_number, lang):
    """Parse a single verse"""
    verse = verse.strip()
    # we remove any spaces sourounding words
    words = list(filter(len, map(str.strip, verse.split())))
    verse = " ".join(words)
    verse_data = {"number": i + 1,
                  "key": f"{chap_number}:{i+1}", "text": verse}
    if not lang:
        transcription = transliterator.translate(verse)
        verse_data["transcription"] = transcription
    return Verse(**verse_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tariha", help="The tariha of the authors")
    parser.add_argument("-a", "--author", help="The author of the xassida")
    parser.add_argument("-x", "--xassida", help="The xassida")
    args = parser.parse_args()
    glob_path = f"{args.tariha}/" if args.tariha else "*/"
    glob_path += f"{args.author}/" if args.author else "*/"
    glob_path += f"{args.xassida}/**/*.txt" if args.xassida else "**/*.txt"
    # start parsing files
    parsed_folders = set()
    for file in Path("xassidas").glob(glob_path):
        depth = 1 if len(file.parent.stem) == 2 else 0
        chapter = parse_file(file, depth)
        xassida = file.absolute().parents[depth]
        parent = xassida if depth == 0 else file.parent

        if xassida.stem not in parsed_folders:
            print("Parsing xassida: ", xassida.parent.stem, "=>", xassida.stem)
        # save the parsed xassida as json

        out_file = parent / f"{xassida.stem}.json"
        existing_data = {}
        if out_file.exists():
            with out_file.open("r") as output:
                existing_data = json.load(output)

        existing_data["name"] = xassida.stem
        existing_data["chapters"] = existing_data.get("chapters", dict())
        existing_data["chapters"][file.stem] = chapter
        result = asdict(Xassida(**existing_data))
        out_file.write_text(json.dumps(result, ensure_ascii=False))
        parsed_folders.add(xassida.stem)
