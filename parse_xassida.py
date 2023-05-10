import argparse
import json
from dataclasses import asdict
from itertools import groupby
from pathlib import Path

from models import Chapter, Verse, Word, Xassida
from transliterator import ArabTransliterator

to_unicode = ArabTransliterator()


def parse_xassida(file, depth):
    """Parse a single xassida file or xassida translation folder
    depth == 0 means that it's the arabic text
    else it's a translation text
    """
    xassida = file.absolute().parents[depth]
    author = xassida.parent
    print("Parsing %s " % (file.parent))
    # parse the chapters with verses and words
    xassida_data = {"name": xassida.stem}
    chapters = parse_file(file, depth)
    xassida_data["chapters"] = list(map(lambda c: Chapter(**c), chapters))
    # save the parsed xassida as json
    result = asdict(Xassida(**xassida_data))
    file = xassida if depth == 0 else file.parent
    out_file = file / f"{xassida.stem}.json"
    out_file.write_text(json.dumps(result, ensure_ascii=False))


def parse_file(file, depth):
    """Parse the file"""
    lang = False if depth == 0 else True
    lines = file.read_bytes().decode("utf-8").split("\n")
    lines = [l + " " for l in lines]
    return parse_chapter(lines, lang)


def parse_chapter(lines, lang):
    chapters = []
    chap_number = 0
    for is_chap, vers in groupby(lines, key=lambda x: x.startswith("###")):
        # if k == True means that its a chapter
        if is_chap:
            chap_number += 1
            chapters.append({"name": next(vers)[3:].strip(), "number": chap_number})
        else:
            verses = filter(len, "".join(vers).split("##"))
            verses_data = map(
                lambda v: parse_verse(*v, chap_number, lang), enumerate(verses)
            )
            chapters[-1]["verses"] = list(verses_data)

    return chapters


def parse_verse(i, verse, chap_number, lang):
    verse = verse.strip()
    words = list(filter(len, map(str.strip, verse.split())))
    verse_data = {"number": i, "key": f"{chap_number}:{i}", "text": verse}
    if not lang:
        phonetic = to_unicode.translate(" ".join(words)).split()
        verse_data["words"] = list(
            map(lambda x: Word(*x, phonetic[x[0]]), enumerate(words))
        )
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
    for file in Path("xassidas").glob(glob_path):
        depth = 0 if file.parent.stem == file.stem else 1
        parse_xassida(file, depth)
